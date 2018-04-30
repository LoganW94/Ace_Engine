#################
'''

A test game of pong to help flesh out the Ace Engine
and to act as a proof of concept.

'''
#######################

import pygame as PY
from Engine.ace_engine import AceEngine
from Pong.game import Game

PY.init()
clock = PY.time.Clock()
FPS = 30

G = Game(PY)

AE = AceEngine.new(PY, G)
		

def start():	

	while True:
		
		AE.get_input()

		AE.update()

		AE.render()
		
		clock.tick(FPS)

start()	