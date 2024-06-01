from typing import Optional

from data.compression_service import CompressionService
from models.character import Character
from models.game_definition import GameDefinition
from models.state import GameState
from utils.singleton import Singleton

class DataService(metaclass=Singleton):

    def __init__(self):
        self.gameDefinition:Optional[GameDefinition] = None
        self.gameStarted:bool = False
        self.state:GameState = GameState("Welcome to the game", "prologue")
        self.characters:[Character] = []
        self.summaries:[str] = []

    def update_characters(self, characters_updates:[Character]) -> None:
        # Replace all characters with the same name with the new ones
        for character in characters_updates:
            self.characters = [character if c.name == character.name else c for c in self.characters]

        # Add new characters
        for character in characters_updates:
            if character not in self.characters:
                self.characters.append(character)

    def save_summary(self, summary:str) -> None:
        self.summaries.append(summary)

        if len(self.summaries) > 100:
            self.summaries = CompressionService.compress_summaries(self.summaries)

    def get_characters_of_location(self, location:str) -> [Character]:
        return [character for character in self.characters if character.location == location]
