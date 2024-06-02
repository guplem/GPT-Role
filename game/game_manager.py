from data.data_service import DataService
from game.game_master_service import GameMasterService
from models.game_definition import GameDefinition
from models.game_master_response import GameMasterResponse
from utils.singleton import Singleton

class GameManager (metaclass=Singleton):

    @staticmethod
    def start_game(game_definition: GameDefinition) -> None:
        print ("Starting game...")
        DataService().gameStarted = True
        DataService().gameDefinition = game_definition

        response:GameMasterResponse = GameMasterService().start_game(game_definition)

        DataService().set_new_game_master_response(response, None)


    @staticmethod
    def perform_action(action: str) -> None:
        print ("Performing action: " + action)
        response:GameMasterResponse = GameMasterService().perform_action(action, DataService().history())

        DataService().set_new_game_master_response(response, action)

    @staticmethod
    def reset_game() -> None:
        print ("Resetting game...")
        DataService().reset_game()
