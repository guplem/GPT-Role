import os
import random
from typing import Optional
from io import StringIO
import json
import streamlit as st

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
        self.__llm_model = "gpt-3.5-turbo"

    # noinspection PyMethodParameters
    @st.cache_data
    def api_key(_self) -> Optional[str]:
        print('Returning non-cached API-KEY value and caching it.')
        return DataService().__API_KEY

    def set_api_key(self, key:Optional[str]) -> None:
        self.api_key.clear()
        self.__API_KEY = key

    # noinspection PyMethodParameters
    @st.cache_data
    def llm_model(_self) -> str:
        print('Returning non-cached LLM model value and caching it.')
        return DataService().__llm_model

    def set_llm_model(self, key:str) -> None:
        self.llm_model.clear()
        self.__llm_model = key

    def save_game_master_response(self, response:GameMasterResponse, player_action:Optional[str]) -> None:
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

    def save_game(self) -> str:
        game_data = {
            "game_definition": self.__gameDefinition.to_json(),
            "game_started": self.__gameStarted,
            "last_response": self.__last_response.to_json(),
            "history": [history.to_json() for history in self.__history]
        }
        return json.dumps(game_data)
    
    def load_game(self, uploaded_file) -> None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        game_data = json.loads(string_data)
        self.__gameDefinition = GameDefinition.from_json(game_data["game_definition"])
        self.__gameStarted = game_data["game_started"]
        self.__last_response = GameMasterResponse.from_json(game_data["last_response"])
        self.__history = [Turn.from_json(turn) for turn in game_data["history"]]