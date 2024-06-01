import streamlit as st

from data.data_service import DataService
from game.game_manager import GameManager

st.title("Game Data Page")
if st.button("Rebuild Page"):
    st.rerun()
st.divider()
st.write("Setup Done: ", GameManager().is_game_started())

def print_game_definition():
    print(f"Current Game Definition: {DataService().gameDefinition.__str__()}")

st.write("Game Definition: ", DataService().gameDefinition.__str__())
