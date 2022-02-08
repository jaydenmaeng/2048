import pygame
import variables
import tile

def main():
	pygame.init()
	window = pygame.display.set_mode((1000, 800))
	running = True

	pygame.draw.rect(window, variables.DEFAULT_DARK, pygame.Rect(30, 30, 60, 60), 2, 3)

	tile1 = tile.Tile(window)
	tile2 = tile.Tile(window)
	# tile3 = tile.Tile(window, 32)
	print(str(tile1.x) + " " + str(tile1.y))
	print(str(tile2.x) + " " + str(tile2.y))
		
	while running:

		# check for event if user has pushed any event in queue
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT: # terminate
				running = False
			if event.type == pygame.K_LEFT:
				tile.leftArrow()
		
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
	
	# set background color 
	window.fill(variables.DEFAULT)
	fontObj = pygame.font.SysFont("arial", 75)
	textSurfaceObj = fontObj.render('2048', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center  = (100, 80)
	window.blit(textSurfaceObj, textRectObj)
	
	pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(675, 100, 110, 60), 0, 0, 3, 3, 3, 3)
	fontObj2 = pygame.font.SysFont("arial bold", 25)
	textSurfaceObj2 = fontObj2.render('Best', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center  = (730, 115)
	window.blit(textSurfaceObj2, textRectObj2)

	pygame.display.update()
		
	# update window 
	pygame.display.flip()
		
