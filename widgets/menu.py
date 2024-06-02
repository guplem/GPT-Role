import streamlit as st


def menu():
    st.sidebar.page_link("main.py", label="Setting")
    st.sidebar.page_link("pages/game.py", label="Game")
    st.sidebar.page_link("pages/history.py", label="History")

