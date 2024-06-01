class GameDefinition:
    def __init__(self,  character_definition, year, theme, objective, additional_info):
        self.characterDefinition = character_definition
        self.year = year
        self.theme = theme
        self.objective = objective
        self.additionalInfo = additional_info

    # to string method
    def __str__(self):
        return f"Game Definition: {self.characterDefinition}, {self.year}, {self.theme}, {self.objective}, {self.additionalInfo}"