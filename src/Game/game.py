

class Game:
	def __init__(self, PY):
		"setup game vars"
        self.init_objs = []
		self.key_file = "Pong/keys.json"
		self.game_name = "Pong"
		self.game_size = (720, 480)
		self.states = ["start", "restart", "levelup"]
		self.current_state = self.states[0]


    def update(self):
        "placeholder" 
        print("update") 
