import streamlit as st

from game.game_manager import GameManager


def game_situation():

    st.title(GameManager().get_current_state().location)
    st.write(GameManager().get_current_state().narrative)
    st.divider()
    st.title("Characters in this location:")
    for character in GameManager().get_characters_in_current_location():
        st.write(character.name)
