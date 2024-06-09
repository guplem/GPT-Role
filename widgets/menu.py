import streamlit as st


def menu():
    st.sidebar.page_link("main.py", label="Settings")
    st.sidebar.page_link("pages/game.py", label="Game")
    st.sidebar.page_link("pages/history.py", label="History")

