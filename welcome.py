import pygame
import variables

pygame.init()
window = pygame.display.set_mode((1000, 800))
running = True
start_button = pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(450, 440, 100, 60), 0, 0, 3, 3, 3, 3)

while running:

	# check for event if user has pushed any event in queue
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT: # terminate
			running = False

		x, y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if start_button.collidepoint(x, y):
					import board
					board.main()

	
	# set background color 
	window.fill(variables.DEFAULT)

	image = pygame.image.load("assets/logo.png")
	window.blit(image, (280, 160))

	fontObj2 = pygame.font.SysFont("arial", 25)
	textSurfaceObj2 = fontObj2.render('By Justin Hwang, David Lee, Jayden Maeng, & Vincent Kim', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center  = (500, 380)
	window.blit(textSurfaceObj2, textRectObj2)

	fontObj3 = pygame.font.SysFont("arial bold", 40)
	textSurfaceObj3 = fontObj3.render('Start', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
	pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(450, 430, 100, 60), 0, 0, 3, 3, 3, 3)
	textRectObj3 = textSurfaceObj3.get_rect()
	textRectObj3.center  = (500, 460)
	window.blit(textSurfaceObj3, textRectObj3)

	fontObj4 = pygame.font.SysFont("arial bold", 40)
	textSurfaceObj4 = fontObj4.render('Use Arrow Keys to Move Tiles', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
	pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(450, 430, 100, 60), 0, 0, 3, 3, 3, 3)
	textRectObj4 = textSurfaceObj3.get_rect()
	textRectObj4.center  = (500, 500)
	window.blit(textSurfaceObj4, textRectObj4)



	pygame.display.update()
	
	# update window 
	pygame.display.flip()

pygame.quit()


pygame.display.update()


	
	# update window
pygame.display.flip()
	
	#change