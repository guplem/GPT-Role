from models.character import Character
from models.state import GameState


class GameMasterResponse:

    def __init__(self, summary:str, characters_updates:[Character], new_state:GameState):
        self._summary:str = summary
        self._characters_updates:[Character] = characters_updates
        self._new_state:GameState = new_state

    def __str__(self):
        return f"""
        Summary: {self._summary}
        \nNew state: {self._new_state.__str__()}
        \nCharacters updates: {self._characters_updates}"""

    def summary(self) -> str:
        return self._summary

    def characters_updates(self) -> [Character]:
        return self._characters_updates

    def new_state(self) -> GameState:
        return self._new_state

    def to_json(self):
        return {
            "summary": self._summary,
            "charactersUpdates": [character.to_json() for character in self._characters_updates],
            "newState": self._new_state.to_json()
        }