# A class that contains the game step (true/false) depending on the seup if done or not
import streamlit as st

from data.data_service import DataService


class GameManager:

    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance


    def start_game(self) -> None:
        print ("Start Game")
        DataService().set_game_started(True)

    def is_game_started(self)-> bool:
        return DataService().is_game_started()