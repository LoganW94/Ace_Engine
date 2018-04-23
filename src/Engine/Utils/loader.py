
class Loader:
	"parent class for loading in game assets"
	def __init__(self, logger):
		self.logger = logger
		self.files = None
		self.folder = None

	def load_items(self, folder):
		"will search given folder and load all items into files list"

	def return_file(self):
		"returns list of all files"
		if (self.files != None):
			return self.files
		else:
			self.logger.report("no files to return")	
