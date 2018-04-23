import pygame
from Renderer.renderer import Renderer
from Input.handler import Handler
from Utils.utils import Utils
from Logs.logger import Logger

class AceEngine:

	@staticmethod
	def new():	
		AE = AceEngine()
		AE.logger = Logger()
		AE.renderer = Renderer(AE.logger)
		AE.in_handler = Handler(AE.logger)
		AE.utils = Utils(AE.logger)
		
		return AE
