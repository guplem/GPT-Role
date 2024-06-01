from dotenv import load_dotenv

from data.data_service import DataService
from game.game_manager import GameManager

load_dotenv()

# Instantiate GameManager
GameManager()
DataService()