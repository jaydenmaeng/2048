import pygame
import variables
from tile import Tile

def main():
		
	pygame.init()
	window = pygame.display.set_mode((1000, 800))
	running = True
	pygame.draw.rect(window, variables.DEFAULT_DARK, pygame.Rect(30, 30, 60, 60), 2, 3)

	tile1 = Tile(window)
	tile2 = Tile(window)
	# tile3 = Tile(window, 32)
	# print(tile1)
	# print(tile2)

	while running:

		# check for event if user has pushed any event in queue
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT: # terminate
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					leftArrow()
					Tile.printBoard()
				if event.key == pygame.K_RIGHT:
					rightArrow()
					Tile.printBoard()
				if event.key == pygame.K_UP:
					upArrow()
					Tile.printBoard()
				if event.key == pygame.K_DOWN:
					downArrow()
					Tile.printBoard()
		
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
		textSurfaceObj2 = fontObj2.render('Score:', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
		textRectObj2 = textSurfaceObj2.get_rect()
		textRectObj2.center  = (610, 130)
		window.blit(textSurfaceObj2, textRectObj2)

		pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(680, 100, 100, 60), 0, 0, 3, 3, 3, 3)
		fontObj2 = pygame.font.SysFont("arial bold", 20)
		textSurfaceObj2 = fontObj2.render('Best:', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
		textRectObj2 = textSurfaceObj2.get_rect()
		textRectObj2.center  = (700, 130)
		window.blit(textSurfaceObj2, textRectObj2)

		# spawn two tiles
		tile1.display()
		tile2.display()

		pygame.display.update()
			
		# update window 
		pygame.display.flip()
	pygame.quit()
		
def leftArrow():
	shiftLeft()
	for j in range(0, 4):
		for i in range(0, 3):
			t = Tile.board[i][j]
			if t == Tile.board[i + 1][j] and t != None:
				Tile.updateValue(Tile.board[i][j])
				Tile.display(Tile.board[i][j])
				Tile.remove(Tile.board[i + 1][j])
				Tile.display(Tile.board[i + 1][j])
				i = 0
	shiftLeft()

def rightArrow():
	shiftRight()
	for j in range(0, 4):
		for i in range(3, 0, -1):
			t = Tile.board[i][j]
			if t == Tile.board[i - 1][j] and t != None:
				Tile.updateValue(Tile.board[i][j])
				Tile.display(Tile.board[i][j])
				Tile.remove(Tile.board[i - 1][j])
				Tile.display(Tile.board[i - 1][j])
				i = 3
	shiftRight()

def upArrow():
	shiftUp()
	for i in range(0, 4):
		for j in range(0, 3):
			t = Tile.board[i][j]
			t1 = Tile.board[i][j + 1]
			if t != None and t1 != None and Tile.getValue(t) == Tile.getValue(t1):
				Tile.updateValue(Tile.board[i][j])
				Tile.display(Tile.board[i][j])
				Tile.remove(Tile.board[i][j + 1])
				Tile.display(Tile.board[i][j + 1])
				j = 0
	shiftUp()

def downArrow():
	shiftDown()
	for i in range(0, 4):
		for j in range(3, 0, -1):
			t = Tile.board[i][j]
			if t == Tile.board[i][j - 1] and t != None:
				Tile.updateValue(Tile.board[i][j])
				Tile.display(Tile.board[i][j])
				Tile.remove(Tile.board[i][j - 1])
				Tile.display(Tile.board[i][j - 1])
				j = 3
	shiftDown()

def shiftLeft():
	for j in range(0, 4):
		row = []
		count = 0
		for i in range(0, 4):
			t = Tile.board[i][j]
			if t != None:
				row.append(t)
				count += 1
		for temp in row:
			p = 0
			while Tile.board[p][j] != temp:
				p += 1
			Tile.updateX(temp, p)
		row.extend([None] * (4 - count))
		for i in range(0, 4):
			Tile.board[i][j] = row[i]


def shiftRight():
	for j in range(0, 4):
		row = []
		count = 0
		for i in range(3, -1, -1):
			t = Tile.board[i][j]
			if t != None:
				row.append(t)
				count += 1
		for temp in row:
			p = 3
			while Tile.board[p][j] != temp:
				p -= 1
			Tile.updateX(temp, p)
		temp = [None] * (4 - count)
		temp.extend(row)
		for i in range(0, 4):
			Tile.board[i][j] = temp[i]

def shiftUp():
	for i in range(0, 4):
		col = []
		count = 0
		for j in range(0, 4):
			t = Tile.board[i][j]
			if t != None:
				col.append(t)
				count += 1
		for temp in col:
			p = 0
			while Tile.board[i][p] != temp:
				p += 1
			Tile.updateY(temp, p)
		Tile.board[i] = col
		Tile.board[i].extend([None] * (4 - count))

def shiftDown():
	for i in range(0, 4):
		col = []
		count = 0
		for j in range(3, -1, -1):
			t = Tile.board[i][j]
			if t != None:
				col.append(t)
				count += 1
		for temp in col:
			p = 3
			while Tile.board[i][p] != temp:
				p -= 1
			Tile.updateY(temp, p)
		Tile.board[i] = [None] * (4 - count)
		Tile.board[i].extend(col)

def rotateLeft():
	temp = [[[] for i in range(4)] for i in range(4)]
	for i in range(4):
		for j in range(4):
			temp[j][3 - i] = Tile.board[i][j]
	Tile.board = temp
main()