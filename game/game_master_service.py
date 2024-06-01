from openai import OpenAI
import random

from models.game_master_response import GameMasterResponse
from models.state import GameState
from utils.singleton import Singleton
from game.game_master_utils import game_master_setup as prompts


class GameMasterService(metaclass=Singleton):

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
        game_mecanics = prompts.game_mecanics
        world_info = "You are in a fantasy world called Aerthoria, a land of magic and mystery. The world is populated by dwarfs, elves, humans, and orcs. The capital city is Eldoria, a bustling metropolis where adventurers gather to seek quests and treasures. The world is threatened by an ancient evil known as the Shadow King, who seeks to plunge Aerthoria into eternal darkness."
        character_info = "The player is Aeric a farmer that works for the local lord. He is a skilled archer and has a loyal dog named Bran. Aeric is on a quest to find the lost sword of King Aldric, a legendary weapon that can defeat the Shadow King."
        tools = prompts.tools
        
        client = OpenAI()
        # The request to the ChatGPT API.
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": f"{prompts.pick_function} {game_mecanics}\n{world_info}. {character_info}."},
                {"role": "user", "content": f"{prompt}"}
            ],
            tools = tools,
            tool_choice="required"
        )

        def conflict():
            dice = random.randint(1, 20)
            messages = [
                {"role": "system", "content": f"{prompts.conflict} {game_mecanics}\n{world_info}. {character_info}."},
                {"role": "user", "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice} \nHow does the story continue?"}]
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = messages,
            )
            return response, dice
        def role_playing():
            dice = random.randint(1, 20)
            print("Hosla roleplaying", dice)
            return response
        def story_telling():
            dice = random.randint(1, 20)
            print("storypoling", dice)
            return response
        
        response2, dice =globals().get(response.choices[0].message.tool_calls[0].function.name)()
        return response2.choices[0].message.content
    def is_game_started(self)-> bool:
        return DataService().is_game_started()