from __future__ import annotations

class GameDefinition:
    def __init__(self,  character_definition, year, theme, objective, additional_info):
        self._character_definition = character_definition
        self._year = year
        self._theme = theme
        self._objective = objective
        self._additionalInfo = additional_info

    def __str__(self) -> str:
        return f"""
        Character definition: {self._character_definition}
        \nYear: {self._year}
        \nTheme: {self._theme}
        \nObjective: {self._objective}
        \nAdditionalInfo: {self._additionalInfo}
        """

    def character_definition(self) -> str:
        return self._character_definition

    def objectives(self) -> str:
        return self._objective

    def theme(self) -> str:
        return self._theme

    def year(self) -> str:
        return self._year

    def additional_info(self) -> str:
        return self._additionalInfo

    def to_json(self) -> dict:
        return {
            "characterDefinition": self._character_definition,
            "year": self._year,
            "theme": self._theme,
            "objective": self._objective,
            "additionalInfo": self._additionalInfo
        }

    @staticmethod
    def from_json(data: dict) -> GameDefinition:
        return GameDefinition(
            data["characterDefinition"],
            data["year"],
            data["theme"],
            data["objective"],
            data["additionalInfo"]
        )

    def as_markdown(self) -> str:
        return f"""
        **Character Definition:** {self._character_definition}
        \n**Year:** {self._year}
        \n**Theme:** {self._theme}
        \n**Objective:** {self._objective}
        \n**Additional Info:** {self._additionalInfo}
        """