class GameState:

    def __init__(self, narrative:str, location:str):
        self._narrative = narrative
        self._location = location

    def __str__(self):
        return f"""
        Narrative: {self._narrative}
        \nLocation: {self._location}"""

    def narrative(self) -> str:
        return self._narrative

    def location(self) -> str:
        return self._location

    def to_json(self):
        return {
            "narrative": self._narrative,
            "location": self._location
        }