import streamlit as st
import json

from data.data_service import DataService
from widgets.menu import menu

st.set_page_config(
    page_title="GPT-Role | History",
    page_icon="📖",
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
menu()

if DataService().game_started() is False:
    st.title("Welcome to GPT-Role")
    st.write("Currently there is no game in progress.")
    if st.button("Start a new game"):
        st.switch_page("pages/game.py")
    uploaded_file = st.file_uploader("Upload a previous game file")
    if uploaded_file is not None:
        # To read file as bytes:
        DataService().load_game(uploaded_file)
else:

    st.title("Game Description")
    st.write(DataService().game_definition().as_markdown())

    st.markdown("######")
    st.divider()
    st.markdown("######")

    if DataService().history() is not None:
        st.title("History")
        for summary in reversed(DataService().history()):
            if summary.player_action() is not None:
                st.markdown(
                "##### Player Action\n" + summary.player_action()
                )
            st.markdown(
            "##### Game Master\n" + summary.game_master_response()
            )
            st.divider()
        
        left_co, right_col = st.columns(2)
        with left_co:
            st.download_button(
                label="Save Game",
                file_name="GPT-Role_game.json",
                mime="application/json",
                data=DataService().save_game()
            )
        with right_col:
            uploaded_file = st.file_uploader("Upload a previous game file")
            if uploaded_file is not None:
                # To read file as bytes:
                DataService().load_game(uploaded_file)

    else:
        st.write("No history yet, start playing!")
