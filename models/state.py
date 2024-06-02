class GameState:

    def __init__(self, narrative:str, location:str, dice:int = None):
        self._narrative = narrative
        self._location = location
        self._dice = dice

    def __str__(self):
        return f"""
        Narrative: {self._narrative}
        \nLocation: {self._location}
        \nDice: {self._dice}"""

    def narrative(self) -> str:
        return self._narrative

    def location(self) -> str:
        return self._location
    
    def dice(self) -> int:
        return self._dice

    def to_json(self):
        return {
            "narrative": self._narrative,
            "location": self._location
        }