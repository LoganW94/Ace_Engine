from Engine.Utils.loader import Loader
"loads all image files"
class SoundLoader(Loader):
	
	def __init__(self, logger):
		self.log = logger
		Loader.__init__(self, self.log)
