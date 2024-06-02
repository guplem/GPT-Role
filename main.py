import streamlit as st

from data.data_service import DataService
from widgets.menu import menu

st.set_page_config(
    page_title="GPT-Role | Settings",
    page_icon="⚙️",
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

st.title("GPT-Role")
st.write("Welcome to GPT-Role, a game where you and an AI will create a story together.")

st.divider()

key = st.text_input("OpenAI API key", value=DataService().api_key(), type="password")

if key is None or len(key) < 5:
    st.warning("Please provide an OpenAI API key to start the game.")

if st.button("Save"):
    DataService().set_api_key(key)
    if key is not None and len(key) > 5:
        st.switch_page("pages/game.py")
