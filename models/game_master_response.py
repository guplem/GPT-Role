from models.state import GameState


class GameMasterResponse:

    def __init__(self, new_state:GameState, dice:int = None, gm_role:str = None):
        self._new_state:GameState = new_state
        self._dice = dice
        self._gm_role = gm_role

    def __str__(self):
        return f"""
        Dice: {self._dice}
        \nAction: {self._gm_role}
        \nNew state: {self._new_state.__str__()}"""

    def new_state(self) -> GameState:
        return self._new_state

    def to_json(self):
        return {
            "dice": self._dice,
            "action": self._gm_role,
            "new_state": self._new_state.to_json()
        }
    
    def from_json(json):
        return GameMasterResponse(
            GameState.from_json(json["new_state"]),
            json["dice"],
            json["action"]
        )

    def dice(self) -> int:
        return self._dice

    def action(self) -> str:
        return self._gm_role