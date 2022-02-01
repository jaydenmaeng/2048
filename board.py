import pygame
import variables
from tile import Tile

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
  
	# Drawing Rectangle
	pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(590, 100, 80, 60), 0, 0, 3, 3, 3, 3)

	fontObj2 = pygame.font.SysFont("arial bold", 20)
	textSurfaceObj2 = fontObj2.render('Score', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center  = (610, 130)
	window.blit(textSurfaceObj2, textRectObj2)

	pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(680, 100, 100, 60), 0, 0, 3, 3, 3, 3)
	fontObj2 = pygame.font.SysFont("arial bold", 20)
	textSurfaceObj2 = fontObj2.render('Best', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center  = (700, 130)
	window.blit(textSurfaceObj2, textRectObj2)

	tile = Tile(2)
	tile.spawnRandom()
	tile.spawnRandom()

	pygame.display.update()
	
	# update window 
	pygame.display.flip()