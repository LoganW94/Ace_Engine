#################



#######################
import pygame as PY
from Engine.ace_engine import AceEngine

AE = AceEngine.new(PY)
PY.init()

clock = PY.time.Clock()
FPS = 30


def start():

	while True:
		
		AE.get_input()

		AE.update()

		AE.render()

		clock.tick(FPS)

start()	