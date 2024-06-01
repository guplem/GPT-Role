class GameDefinition:
    def __init__(self,  character_definition, year, theme, objective, additional_info):
        self.characterDefinition = character_definition
        self.year = year
        self.theme = theme
        self.objective = objective
        self.additionalInfo = additional_info

    def __str__(self):
        return f"""
        Character definition: {self.characterDefinition}
        \nYear: {self.year}
        \nTheme: {self.theme}
        \nObjective: {self.objective}
        \nAdditionalInfo: {self.additionalInfo}"""

    def clear(self):
        self.characterDefinition = ""
        self.year = ""
        self.theme = ""
        self.objective = ""
        self.additionalInfo = ""