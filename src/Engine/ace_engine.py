import pygame
from Engine.Renderer.renderer import Renderer
from Engine.Input.handler import EventHandler
from Engine.Utils.utils import Utils
from Engine.Logs.logger import Logger


class AceEngine:

	@staticmethod
	def new():

		"classes"	
		AE = AceEngine()
		AE.log = Logger()
		AE.uts = Utils(AE.log)
		AE.ren = Renderer(AE.log)
		AE.eve = EventHandler(AE.log)
		AE.up = Updater(AE.log)
		
		"variables"
		AE.new_input
		
		return AE

	def get_input(self):
		AE.eve.get_input()

	def update(self):
		"will pass all new input into the updater"
		AE.up.update()

	def render(self):
		"will render updated objects to screen"
		AE.ren.draw()				
