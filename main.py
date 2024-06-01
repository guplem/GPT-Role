import streamlit as st
from game.game_manager import GameManager

st.write("Hello World!")

# Instantiate GameManager
if GameManager.get_instance() is None:
    GameManager()