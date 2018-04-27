from Engine.Utils.loader import Loader
"loads all image files"
class AssetLoader(Loader):
	
	def __init__(self, logger):
		self.log = logger
		Loader.__init__(self.log)
