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
	textRectObj.center  = (490, 250)
	window.blit(textSurfaceObj, textRectObj)

	fontObj2 = pygame.font.SysFont("arial", 25)
	textSurfaceObj2 = fontObj2.render('By Justin Hwang, David Lee, Jayden Maeng, & Vincent Kim', True, variables.DEFAULT_DARK2, variables.DEFAULT)
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center  = (500, 400)
	window.blit(textSurfaceObj2, textRectObj2)

bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

clicked = False
counter = 0
class button: 
	button_col = (255, 0, 0)
	width = 180
	height = 70
	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(window, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(window, self.hover_col, button_rect)
		else:
			pygame.draw.rect(window, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(window, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(window, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(window, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(window, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action



again = button(75, 200, 'Play Again?')
quit = button(325, 200, 'Quit?')
down = button(75, 350, 'Down')
up = button(325, 350, 'Up')


run = True
while run:

	screen.fill(bg)

	if again.draw_button():
		print('Again')
		counter = 0
	if quit.draw_button():
		print('Quit')
	if up.draw_button():
		print('Up')
		counter += 1
	if down.draw_button():
		print('Down')
		counter -= 1

	counter_img = font.render(str(counter), True, red)
	screen.blit(counter_img, (280, 450))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()


pygame.display.update()


	
	# update window
pygame.display.flip()
	
	#change