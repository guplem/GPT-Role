import os
import random
from typing import Optional

from dotenv import load_dotenv

from data.example_game_definitions import example_game_definitions
from models.game_definition import GameDefinition
from models.game_master_response import GameMasterResponse
from models.state import GameState
from models.turn import Turn
from utils.singleton import Singleton

class DataService(metaclass=Singleton):

    def __init__(self):
        self.__gameDefinition:Optional[GameDefinition] = None
        self.__gameStarted:bool = False
        self.__last_response:GameMasterResponse = GameMasterResponse(GameState("Welcome to the game"))
        self.__history:[Turn] = []
        load_dotenv()
        self.__API_KEY = os.getenv("OPENAI_API_KEY")

    def api_key(self) -> Optional[str]:
        return self.__API_KEY

    def set_api_key(self, key:str):
        self.__API_KEY = key

    def save_game_master_response(self, response:GameMasterResponse, player_action:Optional[str]):
        self.__gameStarted = True
        self.__last_response = response
        self.__save_history(player_action, response.new_state().narrative())


    def __save_history(self, action:Optional[str], summary:str) -> None:
        turn = Turn(action, summary)
        self.__history.append(turn)

    def history(self) -> [Turn]:
        return self.__history

    def last_response(self) -> GameMasterResponse:
        return self.__last_response

    def game_definition(self) -> Optional[GameDefinition]:
        return self.__gameDefinition

    def game_started(self) -> bool:
        return self.__gameStarted

    __game_definition_suggestion: GameDefinition = random.choice(example_game_definitions)

    def change_game_definition_suggestion(self) -> None:
        self.__game_definition_suggestion = random.choice(example_game_definitions)

    def game_definition_suggestion(self) -> GameDefinition:
        return self.__game_definition_suggestion

    def reset_game(self) -> None:
        self.__gameDefinition = None
        self.__gameStarted = False
        self.__last_response = GameMasterResponse(GameState("Welcome to the game"))
        self.__history = []

    def start_game(self, game_definition) -> None:
        self.__gameDefinition = game_definition
        self.__gameStarted = True