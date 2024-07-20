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


# noinspection PyMethodMayBeStatic
class DataService(metaclass=Singleton):

    def __init__(self):
        st.session_state.gameDefinition = None
        st.session_state.gameStarted = False
        st.session_state.last_response = GameMasterResponse(GameState("Welcome to the game"))
        st.session_state.history = []
        st.session_state.game_definition_suggestion = random.choice(example_game_definitions)
        load_dotenv()
        st.session_state.key = os.getenv("OPENAI_API_KEY")
        st.session_state.llm_model = "gpt-4o-mini"

    def get_api_key(self) -> Optional[str]:
        return st.session_state.key

    def set_api_key(self, value:Optional[str]) -> None:
        st.session_state.key = value

    def get_llm_model(self) -> str:
        return st.session_state.llm_model

    def set_llm_model(self, value:str) -> None:
        st.session_state.llm_model = value

    def save_game_master_response(self, response:GameMasterResponse, player_action:Optional[str]) -> None:
        st.session_state.gameStarted = True
        st.session_state.last_response = response
        self.__save_history(player_action, response.new_state().narrative())

    def __save_history(self, action:Optional[str], summary:str) -> None:
        turn = Turn(action, summary)
        st.session_state.history.append(turn)

    def history(self) -> [Turn]:
        return st.session_state.history

    def last_response(self) -> GameMasterResponse:
        return st.session_state.last_response

    def game_definition(self) -> Optional[GameDefinition]:
        return st.session_state.gameDefinition

    def game_started(self) -> bool:
        return st.session_state.gameStarted

    def change_game_definition_suggestion(self) -> None:
        st.session_state.game_definition_suggestion = random.choice(example_game_definitions)

    def game_definition_suggestion(self) -> GameDefinition:
        return st.session_state.game_definition_suggestion

    def reset_game(self) -> None:
        st.session_state.gameDefinition = None
        st.session_state.gameStarted = False
        st.session_state.last_response = GameMasterResponse(GameState("Welcome to the game"))
        st.session_state.history = []

    def start_game(self, game_definition) -> None:
        st.session_state.gameDefinition = game_definition
        st.session_state.gameStarted = True

    def save_game(self) -> str:
        game_data = {
            "game_definition": st.session_state.gameDefinition.to_json(),
            "game_started": st.session_state.gameStarted,
            "last_response": st.session_state.last_response.to_json(),
            "history": [history.to_json() for history in st.session_state.history]
        }
        return json.dumps(game_data)
    
    def load_game(self, uploaded_file) -> None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        game_data = json.loads(string_data)
        st.session_state.gameDefinition = GameDefinition.from_json(game_data["game_definition"])
        st.session_state.gameStarted = game_data["game_started"]
        st.session_state.last_response = GameMasterResponse.from_json(game_data["last_response"])
        st.session_state.history = [Turn.from_json(turn) for turn in game_data["history"]]