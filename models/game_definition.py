class GameDefinition:
    def __init__(self,  character_definition, year, theme, objective, additional_info):
        self._characterDefinition = character_definition
        self._year = year
        self._theme = theme
        self._objective = objective
        self._additionalInfo = additional_info

    def __str__(self):
        return f"""
        Character definition: {self._characterDefinition}
        Year: {self._year}
        Theme: {self._theme}
        Objective: {self._objective}
        AdditionalInfo: {self._additionalInfo}
        """

    def character_definition(self) -> str:
        return self._characterDefinition

    def objectives(self) -> str:
        return self._objective

    def theme(self) -> str:
        return self._theme

    def year(self) -> str:
        return self._year

    def additional_info(self) -> str:
        return self._additionalInfo
