import random

from openai import OpenAI
from openai.types.chat import ChatCompletion

from game.game_master_prompt import GameMasterPrompt
from models.character import Character
from models.game_definition import GameDefinition
from models.game_master_response import GameMasterResponse
from models.state import GameState


class GameMasterService:
    TOOLS = [
        {"type": "function",
         "function": {
             "name": "conflict",
             "description": GameMasterPrompt.CONFLICT
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
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameMasterService, cls).__new__(cls)
        return cls._instance

    def start_game(self, game_definition: GameDefinition) -> GameMasterResponse:
        self.game_definition = game_definition
        return GameMasterResponse("Welcome Message", [], GameState("Game Started", "start"))

    def perform_action(self, action: str, relevant_characters: [Character], state: GameState,
                       game_definition: GameDefinition, summaries: [str]) -> GameMasterResponse:
        result = self.call_llm(action, "\n".join(summaries))

        return GameMasterResponse(result, [], GameState(result, "Action"))

    def call_llm(self, prompt: str, summary: str) -> str:
        # This is effectively telling ChatGPT what we're going to use its JSON output for.
        client = OpenAI()
        # The request to the ChatGPT API.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"{GameMasterPrompt.DECIDE_ACTION_BOT_ROLE} {GameMasterPrompt.GAME_MECHANICS}"
                            f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                            f"{GameMasterPrompt.year(self.game_definition.year())}"
                            f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                            f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                            f"{GameMasterPrompt.character_definition(self.game_definition.character_definition())}."},
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
        client = OpenAI()
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} "
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
             "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice} \nUsing less than 3 sentences, how does the story continue?"}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response

    def role_playing(self, prompt: str, summary: str) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing role play")
        client = OpenAI()
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
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response

    def story_telling(self, prompt: str, summary: str) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing story telling")
        client = OpenAI()
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
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response
