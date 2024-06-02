import streamlit as st

from data.data_service import DataService
from widgets.game_setup_widget import game_setup
from widgets.game_situation import game_state


st.set_page_config(
    page_title="GPT-Role | Game",
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

key = DataService().api_key()
if key is None or len(key) < 5:
    st.warning("Please provide an OpenAI API key to start the game.")
    if st.button("Go to Settings"):
        st.switch_page("main.py")
    st.stop()

else:

    # If the game Master has the setup done
    if not DataService().game_started():
        game_setup()

    else:
        game_state()


    # st.markdown('#')
    # st.markdown('#')
    # st.divider()
    # st.button("Reset Game", on_click=GameManager().reset_game)