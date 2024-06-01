import streamlit as st

from game.game_manager import GameManager

def game_setup():
    st.write("Game Setup")
    st.button("Start Game", on_click=GameManager().start_game)