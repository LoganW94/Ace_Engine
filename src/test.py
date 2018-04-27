#################



#######################
import pygame
from Engine.ace_engine import AceEngine

AE = AceEngine.new()
pygame.init()

clock = pygame.time.Clock()
FPS = 30


def start():

	while True:

		AE.get_input()

		AE.update()

		AE.render()

		clock.tick(FPS)

start()	