"input handler"
import json

class EventHandler:

	def __init__(self, logger, PY, file):
		"sets up class variable"
		"on instanciation it should be passed a json file containing valid keystrokes"
		self.logger = logger
		self.PY = PY
		self.file = file
		self.new_input = None

		"temp until dynamic list is added"
		self.keys = self.load_keys()
		

	def load_keys(self):
		key_list = json.load(open(self.file))
		key_list = key_list["KEYS"]
		return key_list

	def get_input(self):
		"this may cause an issue since it is calling init() every frame"
		self.PY.init()

		"need to stop input after releasing key"
		 
		for event in self.PY.event.get():
			if event.type == self.PY.QUIT:
				self.PY.quit()
				quit()
				break
			if event.type == self.PY.KEYDOWN:
				key = self.PY.key.name(event.key)
				if key in self.keys:
					self.new_input = self.keys[key]
				else:
					print(key)
			if event.type == self.PY.KEYUP:
				key = self.PY.key.name(event.key)
				if key in self.keys:
					self.new_input = None

	def return_input(self):
		return self.new_input		