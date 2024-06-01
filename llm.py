import openai
from openai import OpenAI

def call(context, prompt, api_key):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a Dungeon Master, {context}"},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content