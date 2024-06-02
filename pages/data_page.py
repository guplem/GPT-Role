import streamlit as st

from data.data_service import DataService


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

st.title("Game Description")
st.write(DataService().game_definition().__str__())

st.divider()

st.title("History")
for summary in DataService().history().reverse():
    st.write(summary)
