# A class that contains the game step (true/false) depending on the seup if done or not

class GameManager:

    _instance = None
    @staticmethod
    def get_instance():
        if not GameManager._instance:
            GameManager()
        return GameManager._instance

    def __init__(self):
        if not GameManager._instance:
            GameManager._instance = self
        else:
            raise Exception("You cannot create another GameManager class")
        self.setup_done = False

    def start_game(self):
        self.setup_done = True

    def is_setup_done(self):
        return self.setup_done