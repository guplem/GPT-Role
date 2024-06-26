from __future__ import annotations

import json
from typing import Optional

class Turn:

    def __init__(self, player_action: Optional[str], game_master_response: str):
        self._player_action: Optional[str] = player_action
        self._game_master_response: str = game_master_response


    def player_action(self) -> Optional[str]:
        return self._player_action


    def game_master_response(self) -> str:
        return self._game_master_response

    def to_json(self):
        return {
            "player_action": self._player_action,
            "gm_response": self._game_master_response
        }

    @staticmethod
    def from_json(data: dict) -> Turn:
        return Turn(
            data["player_action"],
            data["gm_response"]
        )

    def to_json_string(self):
        return json.dumps(self.to_json())