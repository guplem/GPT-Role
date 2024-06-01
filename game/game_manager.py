from data.data_service import DataService
from game.game_master_service import GameMasterService
from models.character import Character
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

        DataService().state = response.newState
        DataService().update_characters(response.charactersUpdates)
        DataService().save_summary(response.summary)

    @staticmethod
    def get_current_state() -> GameState:
        return DataService().state

    @staticmethod
    def perform_action(action: str) -> None:
        print ("Performing action: " + action)
        relevant_characters:[Character] = GameManager().get_characters_in_current_location()
        response:GameMasterResponse = GameMasterService().perform_action(action, relevant_characters, DataService().state, DataService().gameDefinition, DataService().summaries)

        DataService().state = response.newState
        DataService().update_characters(response.charactersUpdates)
        DataService().save_summary(response.summary)

    @staticmethod
    def get_characters_in_current_location() -> [Character]:
        return DataService().get_characters_of_location(DataService().state.location)
