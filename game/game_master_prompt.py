class GameMasterPrompt:
    CONFLICT = """
        - Turn-Based: Combat is typically turn-based, with each player and NPC acting in a determined order (initiative).
        - Actions: On their turn, characters can perform actions such as attacking, casting spells, or using items.
        - Hit Points: Characters have hit points (HP) representing their health. Damage reduces HP, and reaching zero HP can result in incapacitation or death.
    """

    ROLE_PLAYING = """
        - Character Interaction: Players interact with each other and NPCs, often speaking in character and making decisions based on their character's personality and motivations.
        - Problem-Solving: Players solve puzzles, navigate social interactions, and make strategic decisions to advance the story.
    """

    STORY_TELLING = """
        - Narrative: The game progresses through a collaborative narrative, with the GM guiding the story and players contributing through their actions and decisions.
        - Flexibility: The story can evolve in unpredictable ways based on player choices, making each game unique.
    """

    GAME_MECHANICS = """
    The game mechanis are: 
        - Actions and outcomes are determined by rolling dice.
        - Checks and Saves: Players roll dice to perform checks (e.g., skill checks, attack rolls) against a target number (difficulty class, DC). Saving throws are used to avoid or mitigate harm.
        - Modifiers: Dice rolls are often modified by character attributes and skills. For example, a high strength score might add a bonus to a melee attack roll.
    """

    DECIDE_ACTION_BOT_ROLE = """
        This is a dice based role game you have to decide what action should be taken. The game master in responsible to creat the world, make sure the players play by the rules and manage the game narrative and NPCs.
    """

    GAME_MASTER_CONFLICT_ROLE = """
        This is a dice based role game and we are in a conflict action as game master. The game master in responsible to create the world, make sure the players play by the rules and manage the game narrative and NPCs.
    """

    GAME_MASTER_ROLE_PLAYING_ROLE = """
        This is a role game and we are in a role playing action as game master. The game master in responsible to interpretate the NPCs of the world and provide to the players with interesting and engaging interactions. 
    """

    GAME_MASTER_STORY_TELLING_ROLE = """
        This is a story telling game and we are in a story telling action as game master. The game master in responsible to create the world and describe it to the players, manage the game narrative and NPCs.
    """

    @staticmethod
    def character_definition(character_definition: str | None) -> str:
        if character_definition is None:
            return ""
        return f"Playable character that will appear in this game are defined as: {character_definition}"

    @staticmethod
    def objectives(objectives: str | None) -> str:
        if objectives is None:
            return ""
        return f"The main objective of the game is {objectives}"

    @staticmethod
    def theme(theme: str | None) -> str:
        if theme is None:
            return "The main theme of the whole story is zombie apocalypse"
        return f"The main theme of the whole story is {theme}"

    @staticmethod
    def year(year: str | None) -> str:
        if year is None:
            return ""
        return f"The story takes place in the year {year}."

    @staticmethod
    def additional_info(info) -> str:
        return f"Additional information: {info}"
