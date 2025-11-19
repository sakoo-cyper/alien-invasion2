class GameState:

    def __init__(self , ai_game):
        self.settings = ai_game.settings
        self.reset_state()
        self.active_flag = True

    def reset_state(self):
        self.ship_left = self.settings.ship_limit
        