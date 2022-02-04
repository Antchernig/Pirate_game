import pygame, sys
from settings import *
from level import Level
from game_data import level_0

# Pygame setup
pygame.init()
# screen parameters
screen = pygame.display.set_mode((screen_width, screen_height))
# frame rate (fps)
clock = pygame.time.Clock()
# level that we use as a layout
level = Level(level_0, screen)

# main game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('grey')
	level.run()

	pygame.display.update()
	clock.tick(60)