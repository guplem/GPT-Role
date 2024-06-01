import random

from openai import OpenAI
from openai.types.chat import ChatCompletion

from data.data_service import DataService
from game.game_master_prompt import GameMasterPrompt
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

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameMasterService, cls).__new__(cls)
        return cls._instance

    def start_game(self, game_definition) -> GameMasterResponse:
        # TODO: Implement the start_game method
        return GameMasterResponse("Welcome Message", [], GameState("Game Started", "start"))

    def call_llm(self, prompt) -> None:
        # This is effectively telling ChatGPT what we're going to use its JSON output for.
        client = OpenAI()
        # The request to the ChatGPT API.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"{GameMasterPrompt.DECIDE_ACTION_BOT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{GameMasterPrompt.WORLD_INFO}. {GameMasterPrompt.CHARACTER_INFO}."},
                {"role": "user", "content": f"{prompt}"}
            ],
            tools=self.TOOLS,
            tool_choice="required"
        )

        response2 = getattr(self, response.choices[0].message.tool_calls[0].function.name)(prompt)
        return response2.choices[0].message.content

    def is_game_started(self) -> bool:
        return DataService().is_game_started()

    @staticmethod
    def conflict(prompt) -> ChatCompletion:
        dice = random.randint(1, 20)
        print("[GAME_MASTER_SERVICE] Executing conflict", dice)
        client = OpenAI()
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{GameMasterPrompt.WORLD_INFO}. {GameMasterPrompt.CHARACTER_INFO}."},
            {"role": "user",
             "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice} \nHow does the story continue?"}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response

    @staticmethod
    def role_playing(prompt) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing role play")
        client = OpenAI()
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{GameMasterPrompt.WORLD_INFO}. {GameMasterPrompt.CHARACTER_INFO}."},
            {"role": "user",
             "content": f"{prompt}\nHow does the story continue?"}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response

    @staticmethod
    def story_telling(prompt) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing story telling")
        client = OpenAI()
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{GameMasterPrompt.WORLD_INFO}. {GameMasterPrompt.CHARACTER_INFO}."},
            {"role": "user",
             "content": f"{prompt}\nHow does the story continue?"}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response
