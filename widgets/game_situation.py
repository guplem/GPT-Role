import streamlit as st

from data.data_service import DataService
from game.game_manager import GameManager

situations = {
    "conflict": "🎲",
    "trivial_action": "☑️",
    "impossible_action": "🙅🏽‍♂️",
    "role_playing": "💬",
    "story_telling": "📖",
    "game_question": "❔",
    "conflict_arise": "⛰️"
}


def game_state():
    st.title(GameManager().get_current_state().location())
    st.write(GameManager().get_current_state().narrative())
    st.divider()
    st.title("Characters in this location:")
    for character in GameManager().get_characters_in_current_location():
        st.write(character.name())
    if GameManager().get_current_state().dice() is not None:
        st.write(f"You rolled: {GameManager().get_current_state().dice()}")

    if GameManager().get_current_state().action() is not None:
        st.image(situations[GameManager().get_current_state().action()], width=400)

    with st.form(key="action_form", border=False):
        action = ""
        st.text_input("What will you do?", value=action, key="action")
        st.form_submit_button("Send", on_click=on_submit)


def on_submit():
    GameManager().perform_action(st.session_state.action)
    st.session_state.action = ""
