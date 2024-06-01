import streamlit as st
import random

from data.data_service import DataService
from game.game_manager import GameManager
from models.game_definition import GameDefinition

def game_setup():
    st.title("New Game")

    def accept_random():
        if not DataService().gameDefinition.characterDefinition:
            DataService().gameDefinition.characterDefinition = DataService().game_definition_suggestion.characterDefinition
        if not DataService().gameDefinition.year:
            DataService().gameDefinition.year = DataService().game_definition_suggestion.year
        if not DataService().gameDefinition.theme:
            DataService().gameDefinition.theme = DataService().game_definition_suggestion.theme
        if not DataService().gameDefinition.objective:
            DataService().gameDefinition.objective = DataService().game_definition_suggestion.objective
        if not DataService().gameDefinition.additionalInfo:
            DataService().gameDefinition.additionalInfo = DataService().game_definition_suggestion.additionalInfo

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("Randomize", on_click= DataService().change_game_definition_suggestion)

    with col2:
        st.button("Accept Suggestions", on_click=accept_random)

    with col3:
        st.button("Clear", on_click= lambda: DataService().gameDefinition.clear())

    st.text_area("Character Definition", value=DataService().gameDefinition.characterDefinition, key="characterDefinition", placeholder=DataService().game_definition_suggestion.characterDefinition)
    st.text_input("Year", value=DataService().gameDefinition.year, key="year", placeholder=DataService().game_definition_suggestion.year)
    st.text_input("Theme", value=DataService().gameDefinition.theme, key="theme", placeholder=DataService().game_definition_suggestion.theme)
    st.text_input("Objective", value=DataService().gameDefinition.objective, key="objective", placeholder=DataService().game_definition_suggestion.objective)
    st.text_area("Additional Info", value=DataService().gameDefinition.additionalInfo, key="additionalInfo", placeholder=DataService().game_definition_suggestion.additionalInfo)

    def on_submit():
        definition = GameDefinition(DataService().gameDefinition.characterDefinition, DataService().gameDefinition.year, DataService().gameDefinition.theme, DataService().gameDefinition.objective, DataService().gameDefinition.additionalInfo)
        GameManager().start_game(definition)

    st.button("Start Game", on_click= on_submit)

