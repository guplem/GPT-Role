class GameState:

    def __init__(self, narrative:str):
        self._narrative = narrative


    def __str__(self):
        return f"""
        Narrative: {self._narrative}"""

    def narrative(self) -> str:
        return self._narrative

    def to_json(self):
        return {
            "narrative": self._narrative
        }