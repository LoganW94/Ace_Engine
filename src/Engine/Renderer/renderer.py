from Engine.Renderer.screen import Screen
from Engine.Renderer.camera import Camera


"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
light_blue = (0,0,100)
medium_blue = (0,0,195)
grey = (200,200,200)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

gw = 960
gh = 640


class Renderer:

	def __init__(self, logger):
		self.log = logger
		self.gs = Screen.new(gw,gh,green,"Test Engine")
		self.cam = Camera

	def render(self):
		"draws to screen"		
