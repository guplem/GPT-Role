import streamlit as st

from game.game_manager import GameManager
from models.game_definition import GameDefinition

characterDefinition = ""
year = ""
theme = ""
objective = ""
additionalInfo = ""

def game_setup():
    st.write("Game Setup")

    st.text_area("Character Definition", value=characterDefinition, key="characterDefinition")
    st.text_input("Year", value=year, key="year")
    st.text_input("Theme", value=theme, key="theme")
    st.text_input("Objective", value=objective, key="objective")
    st.text_area("Additional Info", value=additionalInfo, key="additionalInfo")

    def on_submit():
        definition = GameDefinition(st.session_state.characterDefinition, st.session_state.year, st.session_state.theme, st.session_state.objective, st.session_state.additionalInfo)
        GameManager().start_game(definition)

    st.button("Start Game", on_click= on_submit)

