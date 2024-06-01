import random

from openai import OpenAI
from openai.types.chat import ChatCompletion

from data.data_service import DataService
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

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameMasterService, cls).__new__(cls)
        return cls._instance

    def start_game(self, game_definition:GameDefinition) -> GameMasterResponse:
        # TODO: Implement the start_game method
        return GameMasterResponse("Welcome Message", [], GameState("Game Started", "start"))

    def perform_action(self, action:str, relevant_characters:[Character], state:GameState, game_definition:GameDefinition, summaries:[str]) -> GameMasterResponse:

        result = self.call_llm(action, game_definition, "\n".join(summaries), relevant_characters)

        return GameMasterResponse(result, [], GameState(result, "Action"))


    def call_llm(self, prompt:str, game_definition:GameDefinition, summary:str, relevant_characters:[Character]) -> str:
        # This is effectively telling ChatGPT what we're going to use its JSON output for.
        client = OpenAI()
        # The request to the ChatGPT API.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"{GameMasterPrompt.DECIDE_ACTION_BOT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{game_definition.theme} {game_definition.objective}. {game_definition.characterDefinition} {game_definition.additionalInfo}."},
                {"role": "user", "content": f"{prompt}"}
            ],
            tools=self.TOOLS,
            tool_choice="required"
        )

        response2 = getattr(self, response.choices[0].message.tool_calls[0].function.name)(prompt, summary)
        return response2.choices[0].message.content

    @staticmethod
    def conflict(prompt:str, game_definition:GameDefinition, summary:str, relevant_characters:[Character]) -> ChatCompletion:
        dice = random.randint(1, 20)
        print("[GAME_MASTER_SERVICE] Executing conflict", dice)
        client = OpenAI()
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{game_definition.theme} {game_definition.objective}. {game_definition.characterDefinition} {game_definition.additionalInfo}."},
            {"role": "assistant",
            "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice} \nUsing less than 3 sentences, how does the story continue?"}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response

    @staticmethod
    def role_playing(prompt:str, game_definition:GameDefinition, summary:str, relevant_characters:[Character]) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing role play")
        client = OpenAI()
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{game_definition.theme} {game_definition.objective}. {game_definition.characterDefinition} {game_definition.additionalInfo}."},
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nUsing less than 3 sentences, how does the story continue?"}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response

    @staticmethod
    def story_telling(prompt:str, game_definition:GameDefinition, summary:str, relevant_characters:[Character]) -> ChatCompletion:
        print("[GAME_MASTER_SERVICE] Executing story telling")
        client = OpenAI()
        messages = [
            {"role": "system",
             "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{game_definition.theme} {game_definition.objective}. {game_definition.characterDefinition} {game_definition.additionalInfo}."},
            {"role": "assistant",
             "content": f"In this world, the things that have happened before are:\n{summary}"},
            {"role": "user",
             "content": f"{prompt}\nUsing less than 3 sentences, how does the story continue?"}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response