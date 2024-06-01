from data.data_service import DataService
from models.game_definition import GameDefinition
from utils.singleton import Singleton

class GameManager (metaclass=Singleton):

    @staticmethod
    def start_game(game_definition: GameDefinition) -> None:
        print ("Starting game...")
        DataService().set_game_started(True)
        DataService().set_game_definition(game_definition)

    @staticmethod
    def is_game_started()-> bool:
        return DataService().is_game_started()