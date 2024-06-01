import streamlit as st

from game.game_manager import GameManager

st.title("Game Data Page")
st.write("Setup Done: ", GameManager().is_game_started())
