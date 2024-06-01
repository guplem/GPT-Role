import streamlit as st

from game.game_manager import GameManager
from widgets.game_setup import game_setup
from widgets.game_situation import game_situation

# If the game Master has the setup done
if not GameManager().is_game_started():
    game_setup()

else:
    game_situation()