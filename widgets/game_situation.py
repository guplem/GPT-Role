import streamlit as st

from game.game_manager import GameManager


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
        st.write(f"Current situation: {GameManager().get_current_state().action()}")

    action = ""
    st.text_input("Action", value=action, key="action")
    def on_submit():
        GameManager().perform_action(st.session_state.action)
        st.session_state.action = ""

    st.button("Perform Action", on_click=on_submit)
