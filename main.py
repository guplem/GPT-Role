from dotenv import load_dotenv

from game.game_manager import GameManager

st.write("Hello World!")

load_dotenv()

# Instantiate GameManager
if GameManager.get_instance() is None:
    GameManager()
