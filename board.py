import pygame
import variables

pygame.init()
window = pygame.display.set_mode((1000, 800))
running = True

pygame.draw.rect(window, variables.DEFAULT_DARK, pygame.Rect(30, 30, 60, 60), 2, 3)

while running:

	# check for event if user has pushed any event in queue
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT: # terminate
			running = False
	
	# set background color 
	window.fill(variables.DEFAULT)
	fontObj = pygame.font.SysFont("arial", 50)
	textSurfaceObj = fontObj.render('2048', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center  = (100, 80)
	window.blit(textSurfaceObj, textRectObj)
	
	for x in range (0, 4):
		for y in range (0, 4):
			rect = pygame.Rect(300 + 115 * x, 300 + 115 * y, 100, 100)
			pygame.draw.rect(window, variables.DEFAULT_DARK, rect, 0, 0, 3, 3, 3, 3)
	pygame.display.update()
	
	# update window
	pygame.display.flip()