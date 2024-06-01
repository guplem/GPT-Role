# A class that contains the game step (true/false) depending on the seup if done or not
import streamlit as st

class DataService:
    SETUP_DONE = "setup_done"

    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataService, cls).__new__(cls)
        return cls._instance

    def set_game_started(self, game_started:bool) -> None:
        st.session_state[self.SETUP_DONE] = game_started

    def is_game_started(self) -> bool:
        return st.session_state.get(self.SETUP_DONE, False)
