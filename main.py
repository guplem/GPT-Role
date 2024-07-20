import streamlit as st

from data.data_service import DataService
from widgets.menu import menu

st.set_page_config(
    page_title="GPT-Role | Settings",
    page_icon="⚙️",
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
menu()

st.title("GPT-Role")
st.write("Welcome to GPT-Role, a game where you and an AI will create a story together.")

st.divider()

def update_key():
    key = st.session_state.api_key
    DataService().set_api_key(key)

st.text_input(
    "OpenAI API key",
    value=DataService().api_key(),
    type="password",
    key="api_key",
    on_change=update_key
)

current_key = DataService().api_key()
if current_key is None or len(current_key) < 5:
    st.warning("Please provide an OpenAI API key to start the game.")

def update_model():
    model = st.session_state.model
    DataService().set_llm_model(model)

model_options = ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o"]

st.selectbox(
    "What OpenAI model do you want to use?",
    index=model_options.index(DataService().llm_model()),
    options=model_options,
    on_change=update_model,
    key="model"
)

# st.write("Your key:", DataService().api_key())
# st.write("You selected:", DataService().llm_model())

if (current_key is not None and len(current_key) >= 5) and DataService().llm_model is not None:
    st.divider()
    st.write("You are ready to play!")
    if st.button("Go to the game"):
        st.switch_page("pages/game.py")
