
from Engine.Collision.collision_detection import Collider

class Updater:
	def __init__(self, logger):
		self.logger = logger
		self.collider = Collider(self.logger)


	def update(self, new_input):
		"#TODO figure out how this is to work"

	def return_delta(self):
		""
					