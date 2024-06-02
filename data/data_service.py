import os
import random
from typing import Optional

from dotenv import load_dotenv

from data.example_game_definitions import example_game_definitions
from models.game_definition import GameDefinition
from models.state import GameState
from models.turn import Turn
from utils.singleton import Singleton

class DataService(metaclass=Singleton):

    def __init__(self):
        self.gameDefinition:Optional[GameDefinition] = None
        self.gameStarted:bool = False
        self.state:GameState = GameState("Welcome to the game")
        self.summaries:[Turn] = []
        load_dotenv()
        self.API_KEY = os.getenv("OPENAI_API_KEY")

    def save_summary(self, action:Optional[str], summary:str) -> None:
        turn = Turn(action, summary)
        self.summaries.append(turn)

    game_definition_suggestion: GameDefinition = random.choice(example_game_definitions)

    def change_game_definition_suggestion(self):
        self.game_definition_suggestion = random.choice(example_game_definitions)

    def reset(self):
        self.gameDefinition = None
        self.gameStarted = False
        self.state = GameState("Welcome to the game")
        self.summaries = []

