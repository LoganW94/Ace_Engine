############################
"the renderer should pre render the frame as an image"
"to then send to pygame, instead of sending each object in the frame"
"this should alow for more controll of the image"
"As well as added effects down the line"
############################

from Engine.Renderer.screen import Screen
from Engine.Renderer.camera import Camera

"colors"
#TODO import from text doc
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


class Renderer:

	def __init__(self, logger, PY, game_name, game_size):
		self.log = logger
		self.PY = PY
		self.gs = Screen.new(self.PY, game_size, green, game_name)
		self.cam = Camera(game_size)

	def render(self, delta):
		self.gs.fill(white)



		self.PY.display.flip()