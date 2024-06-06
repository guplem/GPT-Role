from __future__ import annotations

from models.state import GameState

class GameMasterResponse:

    def __init__(self, new_state:GameState, dice:int = None, gm_role:str = None):
        self._new_state:GameState = new_state
        self._dice = dice
        self._gm_role = gm_role

    def __str__(self) -> str:
        return f"""
        Dice: {self._dice}
        \nAction: {self._gm_role}
        \nNew state: {self._new_state.__str__()}"""

    def new_state(self) -> GameState:
        return self._new_state

    def to_json(self) -> dict:
        return {
            "dice": self._dice,
            "action": self._gm_role,
            "new_state": self._new_state.to_json()
        }

    @staticmethod
    def from_json(data: dict) -> GameMasterResponse:
        return GameMasterResponse(
            GameState.from_json(data["new_state"]),
            data["dice"],
            data["action"]
        )

    def dice(self) -> int:
        return self._dice

    def action(self) -> str:
        return self._gm_role