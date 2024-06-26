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
    "conflict_arise": "🔥"
}


def game_state():
    emoji = situations.get(DataService().last_response().action(), "🌍")

    title = DataService().history()[-1].player_action() or "World setup..."
    st.header(emoji + " " + title)
    if DataService().last_response().dice() is not None:
        st.write(f"You rolled a d20 and got a {DataService().last_response().dice()}")
    st.write(DataService().last_response().new_state().narrative())
    st.divider()

    with st.form(key="action_form", border=False):
        action = ""
        st.text_input("What will you do?", value=action, key="action")
        st.form_submit_button("Send", on_click=on_submit)


def on_submit():
    GameManager().perform_action(st.session_state.action)
    st.session_state.action = ""
