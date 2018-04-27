"input handler"

import pygame

class EventHandler:

	def __init__(self, logger):
		"sets up class variable"
		"on instanciation it should be passed a json file containing valid keystrokes"
		self.logger = logger
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
		"temp code from old game"
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				key = pygame.key.name(event.key)
				if key in self.keys:
					self.new_input = self.keys[key]
				else:
					print(key)	

		return(self.new_input)

