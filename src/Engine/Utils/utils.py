"class for managing the saving and loading gamestates, and whatever else I can't think of at the moment"

from Engine.Utils.loadmaps import MapLoader
from Engine.Utils.loadassets import AssetLoader
from Engine.Utils.loadsounds import SoundLoader

class Utils:

	def __init__(self, logger):
		"loads in all related classes"
		self.log = logger
		self.mLoad = MapLoader(self.log)
		self.iLoad = AssetLoader(self.log)
		self.sLoad = SoundLoader(self.log)
		
		self.m = None
		self.i = None
		self.s = None

	def mload(self, folder):
		"loads all maps"
		self.mLoad.load_items(folder)

	def mReturn(self):
		"returns array of loaded files"
		self.m = self.mLoad.return_file()
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