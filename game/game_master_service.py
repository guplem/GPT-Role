from openai import OpenAI

class GameMasterService:

    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameMasterService, cls).__new__(cls)
        return cls._instance


    def call_llm(self, prompt) -> None:
        # This is effectively telling ChatGPT what we're going to use its JSON output for.
        tools = [
            {"type": "function",
            "function": {
            "name": "conflict",
            "description": """
                - Turn-Based: Combat is typically turn-based, with each player and NPC acting in a determined order (initiative).
                - Actions: On their turn, characters can perform actions such as attacking, casting spells, or using items.
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

        world_info = "You are in a fantasy world called Aerthoria, a land of magic and mystery. The world is populated by dwarfs, elves, humans, and orcs. The capital city is Eldoria, a bustling metropolis where adventurers gather to seek quests and treasures. The world is threatened by an ancient evil known as the Shadow King, who seeks to plunge Aerthoria into eternal darkness."
        character_info = "The player is Aeric a farmer that works for the local lord. He is a skilled archer and has a loyal dog named Bran. Aeric is on a quest to find the lost sword of King Aldric, a legendary weapon that can defeat the Shadow King."

        game_mecanics = """The game mechanis are: 
        - Actions and outcomes are determined by rolling dice.
        - Checks and Saves: Players roll dice to perform checks (e.g., skill checks, attack rolls) against a target number (difficulty class, DC). Saving throws are used to avoid or mitigate harm.
        - Modifiers: Dice rolls are often modified by character attributes and skills. For example, a high strength score might add a bonus to a melee attack roll."""

        client = OpenAI()
        # The request to the ChatGPT API.
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": f"This is a dice based role game you have to decide what action should be taken. The game master in responsible to creat the world, make sure the players play by the rules and manage the game narrative and NPCs. {game_mecanics}\n{world_info}. {character_info}."},
                {"role": "user", "content": f"{prompt}"}
            ],
            tools = tools,
            tool_choice="required"
        )

        import random
        def conflict():
            dice = random.randint(1, 20)
            messages = [
                {"role": "system", "content": f"This is a dice based role game and we are in a conflict action as game master. The game master in responsible to create the world, make sure the players play by the rules and manage the game narrative and NPCs. {game_mecanics}\n{world_info}. {character_info}."},
                {"role": "user", "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice} \nHow does the story continue?"}]
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = messages,
            )
            return response, dice
        def role_playing():
            dice = random.randint(1, 20)
            print("Hosla roleplaying", dice)
            return response
        def story_telling():
            dice = random.randint(1, 20)
            print("storypoling", dice)
            return response
        
        response2, dice =globals().get(response.choices[0].message.tool_calls[0].function.name)()
        return response2.choices[0].message.content
    def is_game_started(self)-> bool:
        return DataService().is_game_started()