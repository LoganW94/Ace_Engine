"input handler"

class EventHandler:

	def __init__(self, logger, PY):
		"sets up class variable"
		"on instanciation it should be passed a json file containing valid keystrokes"
		self.logger = logger
		self.PY = PY
		self.new_input = None

		"temp until dynamic list is added"
		self.keys = {
		"w":"UP",
		"s":"DOWN",
		"a":"LEFT",
		"d":"RIGHT",
		"return": "RETURN",
		"escape": "MENU"}
		
	def get_input(self):
		"this may cause an issue since it is calling init() every frame"
		self.PY.init() 
		for event in self.PY.event.get():
			if event.type == self.PY.QUIT:
				self.PY.quit()
			if event.type == self.PY.KEYDOWN:
				key = self.PY.key.name(event.key)
				if key in self.keys:
					self.new_input = self.keys[key]
				else:
					print(key)	

		return(self.new_input)

