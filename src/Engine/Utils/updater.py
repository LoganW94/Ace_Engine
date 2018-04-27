from Engine.Utils.collision_detection import Collider

class Updater:
	def __init__(self, logger):
		self.logger = logger
		self.collider = Collider(self.logger)

	def update(self):
		"update game states"
		"update game camera location"
		"checks for collision or perhaps passes it into object's update"
		"runs through all changed objects and calls update"	