import streamlit as st

from game.game_manager import GameManager
from widgets.game_setup import build
from widgets.game_situation import GameSituation

st.title("Game Page")

# If the game Master has the setup done
#if st.session_state.game_manager.is_setup_done():
if not GameManager.get_instance().is_setup_done():

    build()

else:

    GameSituation().build()