#################
'''


'''
#######################
import pygame as PY
from Engine.ace_engine import AceEngine

PY.init()

game_name = "Test Engine"
key_file = "Game/Files/default_keys.json"

def start():
	AE = AceEngine.new(PY, key_file, game_name)

	clock = PY.time.Clock()
	FPS = 30

	while True:
		
		AE.get_input()

		AE.update()

		AE.render()

		clock.tick(FPS)

start()	