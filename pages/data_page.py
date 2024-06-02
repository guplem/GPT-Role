import streamlit as st
from streamlit.commands.page_config import InitialSideBarState

from data.data_service import DataService
from game.game_manager import GameManager


st.set_page_config(
    page_title="GPT-Role",
    page_icon="🎲",
    menu_items={"About":
       "## Authors\n"
       "- [Guillem Poy](https://github.com/guplem)\n"
       "- [Sergi Romero](https://github.com/sergiromero)\n"
       "- [Oriol Hinojo](https://github.com/hinox13)\n"
       "## Repository\n"
       "[Link to the repository](https://github.com/guplem/GPT-Role)\n"
       "\n"
    },
    initial_sidebar_state="collapsed"
)

st.title("Game Data Page")
if st.button("Rebuild Page"):
    st.rerun()
st.divider()
st.write("Setup Done: ", GameManager().is_game_started())

st.title("Game Definition")
st.write(DataService().gameDefinition.__str__())

st.title("Current State")
st.write(DataService().state.__str__())

st.title("Summary")
for summary in DataService().summaries:
    st.write(summary)
