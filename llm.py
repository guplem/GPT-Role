import openai

# Function to call the OpenAI API
def call(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Use the appropriate model
        prompt=prompt,
        max_tokens=2000,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()