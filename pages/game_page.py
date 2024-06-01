from game.game_manager import GameManager
from widgets.game_setup_widget import game_setup
from widgets.game_situation import game_state

# If the game Master has the setup done
if not GameManager().is_game_started():
    game_setup()

else:
    game_state()