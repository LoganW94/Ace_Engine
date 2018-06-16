from StarSurvival.gui import Gui
from StarSurvival.states import States

class Game:
	def __init__(self, PY):
                self.PY = PY
                self.engine = None
                self.game_objs = []
                self.key_file = "StarSurvival/Files/keys.json"
                self.game_name = "Star Survival"
                self.game_size = (960,720)
                self.gui = Gui(PY, self.game_size)
                self.states = States()

	def update(self):
                self.engine.update()
            
