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
	fontObj = pygame.font.SysFont("times new roman", 200)
	textSurfaceObj = fontObj.render('2048', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center  = (490, 300)
	window.blit(textSurfaceObj, textRectObj)

	fontObj2 = pygame.font.SysFont("arial", 25)
	textSurfaceObj2 = fontObj2.render('By Justin Hwang, David Lee, Jayden Maeng, & Vincent Kim', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center  = (100, 250)
	window.blit(textSurfaceObj2, textRectObj2)



	pygame.display.update()


	
	# update window
	pygame.display.flip()
	
	#change