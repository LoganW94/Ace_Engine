from Engine.Utils.loader import Loader

class MapLoader(Loader):

	def __init__(self, logger):
		self.log = logger
		Loader.__init__(self.log)
		