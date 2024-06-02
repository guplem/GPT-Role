class GameState:

    def __init__(self, narrative:str, location:str, dice:int = None, action:str = None):
        self._narrative = narrative
        self._location = location
        self._dice = dice
        self._action = action

    def __str__(self):
        return f"""
        Narrative: {self._narrative}
        \nLocation: {self._location}
        \nDice: {self._dice}
        \nAction: {self._action}"""

    def narrative(self) -> str:
        return self._narrative

    def location(self) -> str:
        return self._location
    
    def dice(self) -> int:
        return self._dice
    
    def action(self) -> str:
        return self._action

    def to_json(self):
        return {
            "narrative": self._narrative,
            "location": self._location,
            "dice": self._dice,
            "action": self._action
        }