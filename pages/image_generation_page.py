import streamlit as st
from openai import OpenAI
from streamlit.commands.page_config import InitialSideBarState

st.set_page_config(
    page_title="GPT-Role",
    page_icon="🎲",
    menu_items={"About":
       "## Authors\n"
       "- [Guillem Poy](https://github.com/guplem)\n"
       "- [Sergi Romero](https://github.com/sergiromero)\n"
       "- [Oriol Hinojo](https://github.com/hinox13)\n"
       "## Repository\n"
       "[Link to the repository](https://github.com/guplem/GPT-Role)\n"
       "\n"
    },
    initial_sidebar_state="collapsed"
)

def generate_image(prompt:str, model:str, size:str):
    client = OpenAI()
    response = client.images.generate(
      model=model,
      prompt=prompt,
      size=size,
      quality="standard",
      n=1,
    )
    return response.data[0].url

st.title("GPT-Image")
st.write("Welcome to GPT-Image, pick what model do you want to use and what resolution you want to generate.")

model_col, size_col = st.columns(2)
with model_col:
    model = st.selectbox("Model", ["dall-e-3", "dall-e-2"])
with size_col:
    if model == "dall-e-2":
        size = st.selectbox("Size", ["256x256", "512x512", "1024x1024"])
    else:
        size = st.selectbox("Size", ["1024x1024", "1024x1792", "1792x1024"])

st.text_area("Image prompt", key="prompt", placeholder="A koala dancing ballet with a tutu")

if st.button("Generate Image"):
    st.write("Fetching image from the API...")
    prompt = st.session_state.prompt
    image = generate_image(prompt, model, size)
    if image:
        st.image(image, caption="Generated Image", width = 400)
