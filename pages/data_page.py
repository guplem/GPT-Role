import streamlit as st

from data.data_service import DataService
from game.game_manager import GameManager

st.title("Game Data Page")
if st.button("Rebuild Page"):
    st.rerun()
st.divider()
st.write("Setup Done: ", GameManager().is_game_started())

st.title("Game Definition")
st.write(DataService().gameDefinition.__str__())

st.title("Current State")
st.write(DataService().state.__str__())

st.title("Characters")
for character in DataService().characters:
    st.write(character.__str__())

st.title("Summary")
for summary in DataService().summaries:
    st.write(summary)
