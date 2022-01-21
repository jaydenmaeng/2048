# import pygame package
import pygame

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
window = pygame.display.set_mode((400, 500))

# creating a bool value which checks
# if game is running
running = True

# setting variable to storecolor
color = "red"

# keep game running till running is true
while running:

	# Check for event if user has pushed
	# any event in queue
	for event in pygame.event.get():
		
		# if event is of type quit then set
		# running bool to false
		if event.type == pygame.QUIT:
			running = False
	
	# set background color to our window
	window.fill(color)
	
	# Update our window
	pygame.display.flip()
	
	# if color is red change it to green and
	# vice-versa
	if(color == "red"):
		color = "purple"
		
	else:
		color = "red"
