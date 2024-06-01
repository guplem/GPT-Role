import openai
from openai import OpenAI

def call(world_info, summaries, context, prompt, api_key):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a Dungeon Master of a role game about {world_info}.\n The summary of the story is the following: {summaries}."},
            {"role": "assistant", "content": "I am a player and I am ready to play"},
            {"role": "user", "content": "Now it's my turn and {prompt}"}
            
        ]
    )
    return completion.choices[0].message.content