from loadmaps import MapLoader
from loadassets import AssetLoader
from loadsounds import SoundLoader

class Utils:
"class for managing the saving and loading gamestates, and whatever else I can't think of at the moment"
	def __init__(self, logger):
		"loads in all related classes"
		self.logger = logger
		self.mLoad = MapLoader(self.logger)
		self.iLoad = AssetLoader(self.logger)
		self.sLoad = SoundLoader(self.logger)

		self.m = None
		self.i = None
		self.s = None

	def mload(self, folder):
		"loads all maps"

	def mReturn(self):
		"returns array of loaded files"
		return self.m

	def iload(self, folder):
		"loads all maps"

	def iReturn(self):
		"returns array of loaded files"
		return self.i
		
	def sload(self, folder):
		"loads all maps"

	def sReturn(self):
		"returns array of loaded files"
		return self.s
			