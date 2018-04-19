import pygame
from Engine.ace_engine import AceEngine

pygame.init()
clock = pygame.time.Clock()
FPS = 25
	

def start():

	while True:


		clock.tick(FPS)

start()		