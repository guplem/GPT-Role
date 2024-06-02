from data.data_service import DataService
from game.game_master_service import GameMasterService
from models.game_definition import GameDefinition
from models.game_master_response import GameMasterResponse
from models.state import GameState
from utils.singleton import Singleton

class GameManager (metaclass=Singleton):


    @staticmethod
    def is_game_started()-> bool:
        return DataService().gameStarted

    @staticmethod
    def start_game(game_definition: GameDefinition) -> None:
        print ("Starting game...")
        DataService().gameStarted = True
        DataService().gameDefinition = game_definition

        response:GameMasterResponse = GameMasterService().start_game(game_definition)

        DataService().state = response.new_state()
        DataService().save_summary(None, response.new_state().narrative())

    @staticmethod
    def get_current_state() -> GameState:
        return DataService().state

    @staticmethod
    def perform_action(action: str) -> None:
        print ("Performing action: " + action)
        response:GameMasterResponse = GameMasterService().perform_action(action, DataService().summaries)

        DataService().state = response.new_state()
        DataService().save_summary(action, response.new_state().narrative())

    @staticmethod
    def reset_game() -> None:
        print ("Resetting game...")
        DataService().reset()
