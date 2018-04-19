import pygame
from renderer import Renderer
from handler import Handler

class AceEngine:

	@staticmethod
	def new():	
		AE = AceEngine()
		AE.renderer = Renderer()
		AE.handler = Handler()
		return AE
