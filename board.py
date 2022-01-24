import pygame
import variables

pygame.init()
window = pygame.display.set_mode((600, 800))
running = True

pygame.draw.rect(window, variables.DEFAULT_DARK, pygame.Rect(30, 30, 60, 60), 2, 3)

while running:

	# check for event if user has pushed any event in queue
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT: # terminate
			running = False
	
	# set background color 
	window.fill(variables.DEFAULT)
	pygame.draw.rect(window, variables.DEFAULT_DARK, pygame.Rect(30, 30, 60, 60))
	
	# update window
	pygame.display.flip()