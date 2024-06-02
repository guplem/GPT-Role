import streamlit as st

from data.data_service import DataService
from game.game_manager import GameManager
from models.game_definition import GameDefinition

def game_setup():
    st.title("New Game")

    def accept_suggestion():
        if not st.session_state["characterDefinition"]:
            st.session_state["characterDefinition"] = DataService().game_definition_suggestion().character_definition()
        if not st.session_state["year"]:
            st.session_state["year"] = DataService().game_definition_suggestion().year()
        if not st.session_state["theme"]:
            st.session_state["theme"] = DataService().game_definition_suggestion().theme()
        if not st.session_state["objective"]:
            st.session_state["objective"] = DataService().game_definition_suggestion().objectives()
        if not st.session_state["additionalInfo"]:
            st.session_state["additionalInfo"] = DataService().game_definition_suggestion().additional_info()

    def clear():
        st.session_state["characterDefinition"] = ""
        st.session_state["year"] = ""
        st.session_state["theme"] = ""
        st.session_state["objective"] = ""
        st.session_state["additionalInfo"] = ""


    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("New Suggestion", on_click= DataService().change_game_definition_suggestion)

    with col2:
        st.button("Accept Suggestions", on_click= accept_suggestion)

    with col3:
        st.button("Clear", on_click= clear)

    st.text_area("Character Definition", key="characterDefinition", placeholder=DataService().game_definition_suggestion().character_definition())
    st.text_input("Year", key="year", placeholder=DataService().game_definition_suggestion().year())
    st.text_input("Theme", key="theme", placeholder=DataService().game_definition_suggestion().theme())
    st.text_input("Objective", key="objective", placeholder=DataService().game_definition_suggestion().objectives())
    st.text_area("Additional Info", key="additionalInfo", placeholder=DataService().game_definition_suggestion().additional_info())

    def on_submit():
        GameManager().start_game(GameDefinition(st.session_state["characterDefinition"], st.session_state["year"], st.session_state["theme"], st.session_state["objective"], st.session_state["additionalInfo"]))

    st.button("Start Game", on_click= on_submit)

