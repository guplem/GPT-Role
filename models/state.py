class GameState:

    def __init__(self, narrative:str, location:str):
        self.narrative = narrative
        self.location = location

    def __str__(self):
        return f"""
        Narrative: {self.narrative}
        \nLocation: {self.location}"""