import streamlit as st

from data.data_service import DataService
from models.turn import Turn


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

if DataService().game_started() is False:
    st.title("Welcome to GPT-Role")
    st.write("Currently there is no game in progress.")
    if st.button("Start a new game"):
        st.switch_page("pages/game_page.py")
    st.stop()


st.title("Game Description")
st.write(DataService().game_definition().__str__())

st.divider()

if DataService().history() is not None:
    reversed_history:[Turn] = DataService().history().reverse()
    if reversed_history is not None:
        st.title("History")
        for summary in reversed_history:
            st.write(summary.player_action())
            st.write(summary.game_master_response())
            st.divider()
    else:
        st.write("No history yet, start playing!")