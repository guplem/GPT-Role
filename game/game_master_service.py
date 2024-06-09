import random
from typing import Optional
from openai import OpenAI
from openai.types.chat import ChatCompletion
from data.data_service import DataService
from game.game_master_prompt import GameMasterPrompt
from models.game_definition import GameDefinition
from models.game_master_response import GameMasterResponse
from models.state import GameState
from models.turn import Turn
from utils.singleton import Singleton

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
        {"type": "function",
         "function": {
             "name": "game_question",
             "description": GameMasterPrompt.GAME_QUESTION
         }},
        {"type": "function",
         "function": {
             "name": "impossible_action",
             "description": GameMasterPrompt.IMPOSSIBLE_ACTION
         }},
        {"type": "function",
         "function": {
             "name": "conflict_arise",
             "description": GameMasterPrompt.CONFLICT_ARISE
         }},
    ]

    game_definition: GameDefinition
    client: OpenAI
    _instance = None

    def start_game(self, game_definition: GameDefinition) -> GameMasterResponse:
        self.client = OpenAI(api_key=DataService().api_key())
        self.game_definition = game_definition
        initial_context = self.__initialize_game_context()
        return GameMasterResponse(GameState(initial_context))

    def perform_action(self, action: str, history: [Turn]) -> GameMasterResponse:
        result, dice, gm_role = self.call_llm(action, history)
        # if relevant_characters is not None:
        #     relevant_characters = self.update_characters("\n".join(summaries)+result, relevant_characters, state.location())
        return GameMasterResponse(GameState(result), dice, gm_role)

    def call_llm(self, prompt: str, history: [Turn]) -> (str, Optional[int], str):
        summary = ("[\n".join([summary.to_json_string() +",\n" for summary in history])) + "]"
        # This is effectively telling ChatGPT what we're going to use its JSON output for the request to the ChatGPT API
        function_chosen = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=[
                {
                    "role": "system",
                    "content":
                        f"{GameMasterPrompt.DECIDE_ACTION_BOT_ROLE}"
                        f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                        f"{GameMasterPrompt.year(self.game_definition.year())}"
                        f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                        f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                        f"{GameMasterPrompt.language(self.game_definition.language())}"
                        f"In this world, the things that have happened before are: " + summary
                },
                {"role": "user", "content": f"{prompt}"}
            ],
            tools=self.TOOLS,
            tool_choice="required"
        )

        function_name = function_chosen.choices[0].message.tool_calls[0].function.name

        game_master_response, dice = getattr(self, function_name)(prompt, summary)
        return game_master_response.choices[0].message.content, dice, function_name

    def conflict(self, prompt: str, summary: str) -> (ChatCompletion, Optional[int]):
        dice = random.randint(1, 20)
        print("[GAME_MASTER_SERVICE] Executing conflict", dice)
        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.BASE_PROMPT}"
                    f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE}"
                    f"{GameMasterPrompt.GAME_MECHANICS}"
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice}"}]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )
        return response, dice

    def trivial_action(self, prompt: str, summary: str) -> (ChatCompletion, Optional[int]):
        print("[GAME_MASTER_SERVICE] Executing trivial_action")
        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.BASE_PROMPT}"
                    f"{GameMasterPrompt.TRIVIAL_ACTION} "
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}"}]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )
        return response, None

    def role_playing(self, prompt: str, summary: str) -> (ChatCompletion, Optional[int]):
        print("[GAME_MASTER_SERVICE] Executing role play")

        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.BASE_PROMPT}"
                    f"{GameMasterPrompt.GAME_MASTER_ROLE_PLAYING_ROLE}"
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}"}]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )
        return response, None

    def story_telling(self, prompt: str, summary: str) -> (ChatCompletion, Optional[int]):
        print("[GAME_MASTER_SERVICE] Executing story telling")

        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.BASE_PROMPT}"
                    f"{GameMasterPrompt.GAME_MASTER_STORY_TELLING_ROLE}"
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
            },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}"}]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )
        return response, None

    def __initialize_game_context(self) -> str:
        print("[GAME_MASTER_SERVICE] Executing initialize game")

        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.GAME_MASTER_INITIALIZE_CONTEXT}"
                    f"{GameMasterPrompt.theme(self.game_definition.theme())}"
                    f"{GameMasterPrompt.year(self.game_definition.year())}"
                    f"{GameMasterPrompt.objectives(self.game_definition.objectives())}"
                    f"{GameMasterPrompt.additional_info(self.game_definition.additional_info())}"
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
            },
        ]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )

        return response.choices[0].message.content

    def game_question(self, prompt: str, summary: str) -> (ChatCompletion, Optional[int]):
        print("[GAME_MASTER_SERVICE] Executing game_question")
        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.GAME_MASTER_GAME_QUESTION_ROLE}"
                    f"{GameMasterPrompt.GAME_MECHANICS}"
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}"}]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )
        return response, None

    def impossible_action(self, prompt: str, summary: str) -> (ChatCompletion, Optional[int]):
        print("[GAME_MASTER_SERVICE] Executing impossible_action")
        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.GAME_MASTER_IMPOSSIBLE_ACTION_ROLE}"
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
             },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}"}]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )
        return response, None

    def conflict_arise(self, prompt: str, summary: str) -> (ChatCompletion, Optional[int]):
        print("[GAME_MASTER_SERVICE] Executing conflict_arise")
        messages = [
            {
                "role": "system",
                "content":
                    f"{GameMasterPrompt.BASE_PROMPT}"
                    f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ARISE_ROLE}"
                    f"{GameMasterPrompt.GAME_MECHANICS}"
                    f"{GameMasterPrompt.language(self.game_definition.language())}"
            },
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}"}]
        response = self.client.chat.completions.create(
            model=DataService().llm_model(),
            messages=messages,
        )
        return response, None
