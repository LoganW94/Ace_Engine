from Engine.Utils.collision_detection import Collider

class Updater:
	def __init__(self, logger, init_objs):
		self.logger = logger
		self.collider = Collider(self.logger)
		self.objs = init_objs

		self.delta = []

	def update(self, new_input, new_objs=None):
		"update game states"
		"update game camera location"
		"checks for collision or perhaps passes it into object's update"
		"runs through all changed objects and calls update"
		"only runs on objects that need updated and adds them to delta"

		self.delta = []

		for x in self.objs:
			x.update(new_input, self.objs)
			self.delta.append(x)

	def return_delta(self):
		return self.delta			