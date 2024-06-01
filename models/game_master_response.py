from models.character import Character
from models.state import GameState


class GameMasterResponse:

    def __init__(self, summary:str, characters_updates:[Character], new_state:GameState):
        self.summary:str = summary
        self.charactersUpdates:[Character] = characters_updates
        self.newState:GameState = new_state

    def __str__(self):
        return f"""
        Summary: {self.summary}
        \nNew state: {self.newState.__str__()}
        \nCharacters updates: {self.charactersUpdates}"""