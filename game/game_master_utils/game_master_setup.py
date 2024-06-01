# Define game mecanics
game_mecanics = """The game mechanis are: 
        - Actions and outcomes are determined by rolling dice.
        - Checks and Saves: Players roll dice to perform checks (e.g., skill checks, attack rolls) against a target number (difficulty class, DC). Saving throws are used to avoid or mitigate harm.
        - Modifiers: Dice rolls are often modified by character attributes and skills. For example, a high strength score might add a bonus to a melee attack roll."""

pick_function = "This is a dice based role game you have to decide what action should be taken. The game master in responsible to creat the world, make sure the players play by the rules and manage the game narrative and NPCs."
conflict = "This is a dice based role game and we are in a conflict action as game master. The game master in responsible to create the world, make sure the players play by the rules and manage the game narrative and NPCs."

# Define chat gpt tools
tools = [
            {"type": "function",
            "function": {
            "name": "conflict",
            "description": """
                - Turn-Based: Conflict is typically turn-based, with each player and NPC acting in a determined order (initiative).
                - Actions: On their turn, characters can perform actions such as attacking, casting spells, using items or doing any action that can be useful during the conflict.
                - Hit Points: Characters have hit points (HP) representing their health. Damage reduces HP, and reaching zero HP can result in incapacitation or death."""
            }},
            {"type": "function",
            "function": {
            "name": "role_playing",
            "description": """
                - Character Interaction: Players interact with each other and NPCs, often speaking in character and making decisions based on their character's personality and motivations.
                - Problem-Solving: Players solve puzzles, navigate social interactions, and make strategic decisions to advance the story."""
            }},
            {"type": "function",
            "function": {
            "name": "story_telling",
            "description": """
                - Narrative: The game progresses through a collaborative narrative, with the GM guiding the story and players contributing through their actions and decisions.
                - Flexibility: The story can evolve in unpredictable ways based on player choices, making each game unique."""
            }},
        ]