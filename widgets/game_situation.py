import streamlit as st

from game.game_manager import GameManager

situations = {
    "conflict": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjZzM240M2Izdnc4aDJzZGo3cnBzYzl0NnQ1Y3l6NzdkN2t3NnU2eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/U7GRtzqJMyVEs/200.webp",
    "trivial_action": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW81MmZycnBqZ3h6aTFzZzJpNDl5eGJ0Z3dhZWIxaW1vNHd0Nnc4dyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/mG7xN3NU7WeUUGiKjM/giphy.gif",
    "impossible_action": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGN5aW0zMGx5enlmNWswYjgwYmFqaGlsenBpdWp4Z2pzYTk4OWozNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5KzHjkoXE2z0TgeKpj/giphy.webp",
    "role_playing": "https://media.giphy.com/media/LkgBmwuzPAgpEFVYbg/giphy.gif?cid=ecf05e47n8j0mgkjz5881cmjnm13peqyu5mwcn6rz02zstfz&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "story_telling": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGdpcHVpdzFycjF6N28xM3F2OGw4d3Qxb20wNGI1ajNkNDVvcGZpeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/25KEhzwCBBFPb79puo/giphy.webp",
    "game_question": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmVuemgwczB2dG9oNTAxZnpiMXhna3Y3Y21yd2l2ampwNnlrMjJ2OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tU2mV8ALzJEdXAAwRo/giphy.webp",
    "conflict_arise": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW81MmZycnBqZ3h6aTFzZzJpNDl5eGJ0Z3dhZWIxaW1vNHd0Nnc4dyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/mG7xN3NU7WeUUGiKjM/giphy.gif"

}

def game_state():

    st.title(GameManager().get_current_state().location())
    st.write(GameManager().get_current_state().narrative())
    st.divider()
    st.title("Characters in this location:")
    for character in GameManager().get_characters_in_current_location():
        st.write(character.name())
    if GameManager().get_current_state().dice() is not None:
        st.write(f"You rolled: {GameManager().get_current_state().dice()}")

    if GameManager().get_current_state().action() is not None:
        st.image(situations[GameManager().get_current_state().action()], width=400)

    action = ""
    st.text_input("Action", value=action, key="action")
    def on_submit():
        GameManager().perform_action(st.session_state.action)
        st.session_state.action = ""

    st.button("Perform Action", on_click=on_submit)
