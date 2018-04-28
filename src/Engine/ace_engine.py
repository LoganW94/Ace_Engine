import pygame
from Engine.Renderer.renderer import Renderer
from Engine.Input.handler import EventHandler
from Engine.Utils.utils import Utils
from Engine.Logs.logger import Logger
from Engine.Utils.updater import Updater


class AceEngine:

	@staticmethod
	def new(PY):
		"Instances"	
		AE = AceEngine()
		AE.PY = PY
		AE.log = Logger()
		AE.uts = Utils(AE.log)
		AE.ren = Renderer(AE.log, AE.PY)
		AE.eve = EventHandler(AE.log, AE.PY)
		AE.up = Updater(AE.log)
		
		"variables"
		AE.new_input = None
		
		return AE

	def get_input(self):
		self.new_input = self.eve.get_input()

	def update(self):
		"will pass all new input into the updater"
		self.up.update()

	def render(self):
		"will render updated objects to screen"
		self.ren.render()				
