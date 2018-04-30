from Engine.Renderer.renderer import Renderer
from Engine.Input.handler import EventHandler
from Engine.Utils.utils import Utils
from Engine.Logs.logger import Logger
from Engine.Utils.updater import Updater


class AceEngine:

	@staticmethod
	def new(PY, G):
		AE = AceEngine()
		PY.init()
		AE.G = G
		AE.PY = PY	
		AE.log = Logger()
		AE.uts = Utils(AE.log)
		AE.eve = EventHandler(AE.log, AE.PY, AE.G.key_file)
		AE.up = Updater(AE.log, AE.G.init_objs)
		AE.ren = Renderer(AE.log, AE.PY, AE.G.game_name, AE.G.game_size)		
				
		return AE

	def get_input(self):
		self.eve.get_input()

	def update(self):
		"will pass all new input into the updater"
		self.up.update(self.eve.return_input())
		self.G.update()

	def render(self):
		"will render updated objects to screen"
		self.ren.render(self.up.return_delta())				
