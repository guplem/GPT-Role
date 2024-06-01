# A class that contains the game step (true/false) depending on the seup if done or not

from models.game_definition import GameDefinition
from utils.singleton import Singleton


class DataService(metaclass=Singleton):

    def __init__(self):
        self.gameDefinition = None
        self.gameStarted = False

    def set_game_started(self, game_started:bool) -> None:
        self.gameStarted = game_started

    def is_game_started(self) -> bool:
        return self.gameStarted

    def set_game_definition(self, game_definition: GameDefinition) -> None:
        self.gameDefinition = game_definition
