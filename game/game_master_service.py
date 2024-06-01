import random

from openai import OpenAI
from openai.types.chat import ChatCompletion

from data.data_service import DataService
from game.game_master_prompt import GameMasterPrompt
from models.character import Character
from models.game_definition import GameDefinition
from models.game_master_response import GameMasterResponse
from models.state import GameState
from utils.singleton import Singleton

model = "gpt-3.5-turbo"


class GameMasterService(metaclass=Singleton):
    TOOLS = [
        {"type": "function",
         "function": {
             "name": "conflict",
             "description": GameMasterPrompt.CONFLICT
         }},
        {"type": "function",
         "function": {
             "name": "trivial_action",
             "description": GameMasterPrompt.TRIVIAL_ACTION
         }},
        {"type": "function",
         "function": {
             "name": "role_playing",
             "description": GameMasterPrompt.ROLE_PLAYING
         }},
        {"type": "function",
         "function": {
             "name": "story_telling",
             "description": GameMasterPrompt.STORY_TELLING
         }},
    ]

    game_definition: GameDefinition
    client: OpenAI
    _instance = None

    def start_game(self, game_definition: GameDefinition) -> GameMasterResponse:
        print(DataService().API_KEY)
        self.client = OpenAI(api_key=DataService().API_KEY)
        self.game_definition = game_definition
        initial_context = self.__initialize_game_context()
        return GameMasterResponse(initial_context, [], GameState(initial_context, "start"))

    def perform_action(self, action: str, relevant_characters: [Character], state: GameState,
                       game_definition: GameDefinition, summaries: [str]) -> GameMasterResponse:
        result = self.call_llm(action, game_definition, "\n".join(summaries), relevant_characters)
        if relevant_characters is not None:
            relevant_characters = self.update_characters("\n".join(summaries)+result, relevant_characters, state.location())
        return GameMasterResponse(result, relevant_characters, GameState(result, "Action"))

    def call_llm(self, prompt: str, game_definition: GameDefinition, summary: str,
                 relevant_characters: [Character]) -> str:
        # This is effectively telling ChatGPT what we're going to use its JSON output for.
        # The request to the ChatGPT API.
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"{GameMasterPrompt.DECIDE_ACTION_BOT_ROLE} {GameMasterPrompt.GAME_MECHANICS}"
                            f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                            f"{GameMasterPrompt.year(self.game_definition.year())}"
                            f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                            f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                            f"{GameMasterPrompt.character_definition(relevant_characters)}."},
                {"role": "user", "content": f"{prompt}"}
            ],
            tools=self.TOOLS,
            tool_choice="required"
        )

        response2 = getattr(self, response.choices[0].message.tool_calls[0].function.name)(prompt, summary)
        return response2.choices[0].message.content

    def conflict(self, prompt: str, summary: str) -> ChatCompletion:
        dice = random.randint(1, 20)
        print("[GAME_MASTER_SERVICE] Executing conflict", dice)
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE}"
                        f"{GameMasterPrompt.GAME_MECHANICS}"
                        f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                        f"{GameMasterPrompt.year(self.game_definition.year())}"
                        f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                        f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                        f"{GameMasterPrompt.character_definition(self.game_definition.character_definition())}"
                        f"{GameMasterPrompt.relevant_characters(self.game_definition.relevant_characters())}."
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice} \nUsing less than 3 sentences, how does the story continue?"}]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return response

    def trivial_action(self, prompt: str, summary: str) -> ChatCompletion:
        dice = random.randint(1, 20)
        print("[GAME_MASTER_SERVICE] Executing conflict", dice)
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.TRIVIAL_ACTION} "
                        f"{GameMasterPrompt.GAME_MECHANICS}"
                        f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                        f"{GameMasterPrompt.year(self.game_definition.year())}"
                        f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                        f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                        f"{GameMasterPrompt.character_definition(self.game_definition.character_definition())}."
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nUsing less than 3 sentences, how does the story continue?"}]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return response

    def role_playing(self, prompt: str, summary: str) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing role play")

        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_ROLE_PLAYING_ROLE}"
                        f"{GameMasterPrompt.GAME_MECHANICS}"
                        f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                        f"{GameMasterPrompt.year(self.game_definition.year())}"
                        f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                        f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                        f"{GameMasterPrompt.character_definition(self.game_definition.character_definition())}."
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nUsing less than 3 sentences, how does the story continue?"}]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return response

    def story_telling(self, prompt: str, summary: str) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing story telling")

        messages = [
            {
                "role": "system",
                "content": f"{GameMasterPrompt.GAME_MASTER_STORY_TELLING_ROLE}"
                           f"{GameMasterPrompt.GAME_MECHANICS}"
                           f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                           f"{GameMasterPrompt.year(self.game_definition.year())}"
                           f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                           f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                           f"{GameMasterPrompt.character_definition(self.game_definition.character_definition())}."
            },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nUsing less than 3 sentences, how does the story continue?"}]
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response

    def __initialize_game_context(self) -> str:
        print("[GAME_MASTER_SERVICE] Executing initialize game")

        messages = [
            {
                "role": "system",
                "content": f"{GameMasterPrompt.GAME_MASTER_INITIALIZE_CONTEXT}"
                           f"{GameMasterPrompt.GAME_MECHANICS}"
                           f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                           f"{GameMasterPrompt.year(self.game_definition.year())}"
                           f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                           f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                           f"{GameMasterPrompt.character_definition(self.game_definition.character_definition())}."
            },
        ]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )

        return response.choices[0].message.content
    
    def update_characters(self, answer, characters: [Character], location) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Updating characters")
        # Use chat gpt to see if a character from the list should be updated because of the action in the answer

        characters = [character.__dict__ for character in characters]
        messages = [
            {
                "role": "system",
                "content": "You are bot in charge of updating a list of dictionaries with new information. "
                           "You always receive a list of dictionaries with characters and you have to update them based on new information. "
                           "Only update description if there is something relevant to be added/removed/updated from the current character description."
                           "You can only answer with the list of characters. "
                           "It is possible that some parts of the json need to be updated while keeping meaningful information."
                           "If it appears a character that is not in the list it needs to be created considering the following attributes: {name:str, description:str, location:str, inventory:[str]}. All attributes are mandatory."
                           "The character can be created only if the name, description and location are explicitly said on the text."
                           f"The current location is: {location}."
            },
            {"role": "user",
             "content": f"This is my list of characters: {characters}\nThis is the new information: {answer}."},
        ]
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )
        print(response.choices[0].message.content)
        return [Character(**character) for character in eval(response.choices[0].message.content)]
# Path: models/game_master_response.py
