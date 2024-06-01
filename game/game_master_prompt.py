class GameMasterPrompt:
    CONFLICT = """
        Players try to perform an action. Some kind of actions can be explore, combat, try to influence an NPC, look for clues or secrets, etc.
    """

    TRIVIAL_ACTION = """
        Players perform an action that is easy to accomplish. The current character has the necessary skills and tools to perform the action without problems.
    """


    ROLE_PLAYING = """
        Players interact with NPCs and other characters and have conversation with them.
    """

    STORY_TELLING = """
        Players ask information about the world, the environment and the NPCs.
    """

    GAME_MECHANICS = """
    The game mechanics are: 
        - Actions and outcomes are determined by rolling dice.
        - Checks and Saves: Players roll dice to perform checks (e.g., skill checks, attack rolls) against a target number (difficulty class, DC). Saving throws are used to avoid or mitigate harm.
        - Modifiers: Dice rolls are often modified by character attributes and skills. For example, a high strength score might add a bonus to a melee attack roll.
    """

    DECIDE_ACTION_BOT_ROLE = """
        This is a dice based role game you have to decide what action should be taken. The game master in responsible to creat the world, make sure the players play by the rules and manage the game narrative and NPCs.
    """

    GAME_MASTER_CONFLICT_ROLE = """
        This is a dice based role game and we are in a conflict action as game master. The game master in responsible to make sure the players play by the rules.
        The result of the action should be determined by rolling dice. The game master should describe the action and the result of the action.
        When the dice is rolled the successfulness of the action is determined by the number rolled returning successful results when number is close to 20 and with very unsuccessfull results when number is close to 0. For intermediate numbers close to 10 the action must end in a neutral result.
        Resolutions of the conflict should only contain involuntarily actions of the player. Never add player voluntary actions.
    """

    GAME_MASTER_ROLE_PLAYING_ROLE = """
        This is a role game and we are in a conversation as game master. The game master in responsible to play as the NPCs of the world and provide to the players with interesting and engaging interactions.
        You must respond with interesting dialogs of the NPCs. Structure the response as a dialog with the structure "{npc_name}: {dialog}".
        Respond only with NPCs dialogs or conversation related aspects. Do not provide any other information or player responses.
    """

    GAME_MASTER_STORY_TELLING_ROLE = """
        This is a story telling game and we are in a story telling action as game master. 
        The game master in responsible to create the world and describe it to the players. It must provide accurate description of the environmnt and the involved NPCs.
    """

    GAME_MASTER_INITIALIZE_CONTEXT = """
        This is a story telling game and we are in a story telling action as game master. The game master in responsible to create the world and describe it to the players. Take into account the player objectives but dont be too explicit about them.
        Provide the user with a context of the world, where he is, what time is it and what is around him. Tell the player the history of it's character. End the narration encouraging player to take an action. 
        Place the player into a specific scene (with more characters if needed) and set up the scene for the player to take an action.
        Allways ask player what he wants to do next.
        Use between 5 or 6 sentences.
    """

    GAME_MASTER_TRIVIAL_ACTION_ROLE = """
        This is a role game and you are the game master. The game master in responsible to explain the result of the action to the player.
        The action is trivial and the player has the necessary skills and tools to perform the action without problems. Allways succeed.
        Respond to the action with a short description of the result of the action and ask the user what he wants to do next.
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
    
    @staticmethod
    def relevant_characters(characters) -> str:
        if characters is None:
            return ""
        characters = "\n".join([f"- Character name: {character.name}\n- Character description: {character.description}\n- Character items: {character.inventory}" for character in characters])
        return f"The story characters that are found on the current location are: {characters}"
