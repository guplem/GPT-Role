import streamlit as st
import llm as llm

# Streamlit app
st.title("Chat with GPT-4")

# Initialize session state for storing the API key and chat history
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = None
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input for API key
if st.session_state['api_key'] is None:
    st.session_state['api_key'] = st.text_input("Enter your OpenAI API key:", type="password")
    st.stop()

# User input
user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        # Append user input to chat history
        st.session_state['chat_history'].append(f"You: {user_input}")

        # Get response from GPT-4
        with st.spinner("Generating response..."):
            # response = llm.call(user_input, st.session_state['api_key'])
            # st.session_state['chat_history'].append(f"ChatGPT: {response}")
            st.session_state['chat_history'].append(f"ChatGPT: Hosla")

# Display chat history
for message in st.session_state['chat_history']:
    st.write(message)