from openai import OpenAI

from game.game_master_prompt import GameMasterPrompt

from data.data_service import DataService


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
                 "description": GameMasterPrompt.CONFLICT
             }},
            {"type": "function",
             "function": {
                 "name": "role_playing",
                 "description": GameMasterPrompt.ROLE_PLAYING
             }},
            {"type": "function",
             "function": {
                 "name": "story_telling",
                 "description": GameMasterPrompt.STORY_TELLING
             }},
        ]

        client = OpenAI()
        # The request to the ChatGPT API.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"{GameMasterPrompt.DECIDE_ACTION_BOT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{GameMasterPrompt.WORLD_INFO}. {GameMasterPrompt.CHARACTER_INFO}."},
                {"role": "user", "content": f"{prompt}"}
            ],
            tools=tools,
            tool_choice="required"
        )

        import random
        def conflict():
            dice = random.randint(1, 20)
            messages = [
                {"role": "system",
                 "content": f"{GameMasterPrompt.GAME_MASTER_CONFLICT_ROLE} {GameMasterPrompt.GAME_MECHANICS}\n{GameMasterPrompt.WORLD_INFO}. {GameMasterPrompt.CHARACTER_INFO}."},
                {"role": "user",
                 "content": f"{prompt}\nI rolled a d20 dice and I got this number: {dice} \nHow does the story continue?"}]
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
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

        response2, dice = globals().get(response.choices[0].message.tool_calls[0].function.name)()
        return response2.choices[0].message.content

    def is_game_started(self) -> bool:
        return DataService().is_game_started()
