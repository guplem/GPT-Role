# A class that contains the game step (true/false) depending on the seup if done or not

class GameMasterService:
    def __init__(self):
        self.setup_done = False

    def start_game(self):
        self.setup_done = True

    def is_setup_done(self):
        return self.setup_done