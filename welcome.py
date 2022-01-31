import pygame
import variables

pygame.init()
window = pygame.display.set_mode((600, 800))
running = True

while running:

	# check for event if user has pushed any event in queue
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT: # terminate
			running = False
	
	# set background color 
	window.fill(variables.DEFAULT)
	
	# update window
	pygame.display.flip()
	
	#change