import pygame
import variables

pygame.init()
window = pygame.display.set_mode((1000, 800))
running = True

while running:

	# check for event if user has pushed any event in queue
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT: # terminate
			running = False
	
	# set background color 
	window.fill(variables.DEFAULT)
	fontObj = pygame.font.SysFont("arial", 200)
	textSurfaceObj = fontObj.render('2048', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center  = (500, 400)
	window.blit(textSurfaceObj, textRectObj)
	pygame.display.update()
	
	# update window
	pygame.display.flip()
	
	#change