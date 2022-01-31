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
	fontObj = pygame.font.SysFont("arial bold", 80)
	textSurfaceObj = fontObj.render('2048', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center  = (380, 80)
	window.blit(textSurfaceObj, textRectObj)
	board = pygame.Rect(285, 285, 500, 500)
	pygame.draw.rect(window, variables.DEFAULT_DARK, board, 0, 0, 3, 3, 3, 3)

	for x in range (0, 4):
		for y in range (0, 4):
			rect = pygame.Rect(300 + 121.25 * x, 300 + 121.25 * y, 106.25, 106.25)
			pygame.draw.rect(window, variables.DEFAULT_TAN, rect, 0, 0, 3, 3, 3, 3)
	pygame.display.update()
	
	# update window
	pygame.display.flip()