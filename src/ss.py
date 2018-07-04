#***********#
#***********#
import pygame as PY
from Engine.ace_engine import AceEngine
from StarSurvival.game import Game

PY.init()
clock = PY.time.Clock()
FPS = 30

G = Game(PY)

AE = AceEngine.new(PY, G)

G.engine = AE

def start():

	while True:
	
		G.get_input()	
	
		G.update()

		G.render()

		clock.tick(FPS)

start()		
