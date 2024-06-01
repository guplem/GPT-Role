from dotenv import load_dotenv

from game.game_manager import GameManager

load_dotenv()

# Instantiate GameManager
if GameManager.get_instance() is None:
    GameManager()
