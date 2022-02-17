import pygame
import variables
import random
from tile import Tile

def main():
	pygame.init()
	window = pygame.display.set_mode((1000, 800))
	gameBoard = [[[] for i in range(4)] for i in range(4)]
	for i in range(0, 4):
		for j in range(0, 4):
			gameBoard[i][j] = None
	
	running = True
	pygame.draw.rect(window, variables.DEFAULT_DARK, pygame.Rect(30, 30, 60, 60), 2, 3)

	spawnTile(gameBoard)
	spawnTile(gameBoard)
	# tile3 = Tile(window, 32)
	# print(tile1)
	# print(tile2)

	while running:

		# check for event if user has pushed any event in queue
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT: # terminate
				running = False
			if event.type == pygame.KEYDOWN:
				newBoard = move(deepCopy(gameBoard), event.key)
				if newBoard != gameBoard:
					spawnTile(newBoard)
					gameBoard = newBoard
					displayBoard(window, gameBoard)
		
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

		# display board
		displayBoard(window, gameBoard)

		# update window 
		pygame.display.update()
			
		# update window 
		pygame.display.flip()
	pygame.quit()

def move(board, key):
	if key == pygame.K_LEFT:
		return leftArrow(board)
	elif key == pygame.K_RIGHT:
		return rightArrow(board)
	elif key == pygame.K_UP:
		return upArrow(board)
	elif key == pygame.K_DOWN:
		return downArrow(board)
	else:
		return board

def deepCopy(board):
	ret = [[[] for i in range(4)] for i in range(4)]
	for i in range(4):
		for j in range(4):
			ret[i][j] = board[i][j]
	return ret

def leftArrow(board):
	shiftLeft(board)
	for j in range(0, 4):
		for i in range(0, 3):
			t = board[i][j]
			t1 = board[i + 1][j]
			if t != None and t1 != None and Tile.getValue(t) == Tile.getValue(t1):
				board[i][j] = Tile(Tile.getX(t), Tile.getY(t), Tile.getValue(t) * 2)
				board[i + 1][j] = None
				i = 0
	shiftLeft(board)
	return board

def rightArrow(board):
	shiftRight(board)
	for j in range(0, 4):
		for i in range(3, 0, -1):
			t = board[i][j]
			t1 = board[i - 1][j]
			if t != None and t1 != None and Tile.getValue(t) == Tile.getValue(t1):
				board[i][j] = Tile(Tile.getX(t), Tile.getY(t), Tile.getValue(t) * 2)
				# Tile.updateValue(board[i][j])
				board[i - 1][j] = None
				i = 0
	shiftRight(board)
	return board

def upArrow(board):
	shiftUp(board)
	for i in range(0, 4):
		for j in range(0, 3):
			t = board[i][j]
			t1 = board[i][j + 1]
			if t != None and t1 != None and Tile.getValue(t) == Tile.getValue(t1):
				board[i][j] = Tile(Tile.getX(t), Tile.getY(t), Tile.getValue(t) * 2)
				board[i][j + 1] = None
				j = 0
	shiftUp(board)
	return board

def downArrow(board):
	shiftDown(board)
	for i in range(0, 4):
		for j in range(3, 0, -1):
			t = board[i][j]
			t1 = board[i][j - 1]
			if t != None and t1 != None and Tile.getValue(t) == Tile.getValue(t1):
				board[i][j] = Tile(Tile.getX(t), Tile.getY(t), Tile.getValue(t) * 2)
				board[i][j - 1] = None
				j = 0
	shiftDown(board)
	return board

def shiftLeft(board):
	for j in range(0, 4):
		row = []
		count = 0
		for i in range(0, 4):
			t = board[i][j]
			if t != None:
				row.append(t)
				count += 1
		for temp in row:
			p = 0
			while board[p][j] != temp:
				p += 1
			Tile.updateX(temp, p)
		row.extend([None] * (4 - count))
		for i in range(0, 4):
			board[i][j] = row[i]

def shiftRight(board):
	for j in range(0, 4):
		row = []
		count = 0
		for i in range(0, 4):
			t = board[i][j]
			if t != None:
				row.append(t)
				count += 1
		for temp in row:
			p = 3
			while board[p][j] != temp:
				p -= 1
			Tile.updateX(temp, p)
		temp = [None] * (4 - count)
		temp.extend(row)
		for i in range(0, 4):
			board[i][j] = temp[i]

def shiftUp(board):
	for i in range(0, 4):
		col = []
		count = 0
		for j in range(0, 4):
			t = board[i][j]
			if t != None:
				col.append(t)
				count += 1
		for temp in col:
			p = 0
			while board[i][p] != temp:
				p += 1
			Tile.updateY(temp, p)
		board[i] = col
		board[i].extend([None] * (4 - count))

def shiftDown(board):
	for i in range(0, 4):
		col = []
		count = 0
		for j in range(0, 4):
			t = board[i][j]
			if t != None:
				col.append(t)
				count += 1
		for temp in col:
			p = 3
			while board[i][p] != temp:
				p -= 1
			Tile.updateY(temp, p)
		board[i] = [None] * (4 - count)
		board[i].extend(col)

def isBoardFull(board):
	for i in range(0, 4):
		for j in range(0, 4):
			if board[i][j] == None:
				return False
	return True

def spawnTile(board, value = -1):
	if value == -1:
		temp = random.randrange(0, 10)
		if temp == 0:
			value = 4
		else:
			value = 2
		x = random.randrange(0, 4) 
		y = random.randrange(0, 4) 

		if not isBoardFull(board):
			while board[x][y] != None:
				x = random.randrange(0, 4)
				y = random.randrange(0, 4)
			board[x][y] = Tile(x, y, value)
	return board[x][y]

def displayBoard(window, board):
	for i in range(4):
		for j in range(4):
			tile = board[i][j]
			if tile != None:
				if Tile.getAge(tile) < 3:
					image = pygame.image.load("assets/" + str(Tile.getValue(tile)) + ".png")
					image = pygame.transform.scale(image, (106.25 + Tile.getAge(tile) * 7, 106.25 + Tile.getAge(tile) * 7))
					Tile.setAge(tile, Tile.getAge(tile) + 1)
					window.blit(image, (300 + 121.25 * Tile.getX(tile) - 0.5 * Tile.getAge(tile), \
						300 + 121.25 * Tile.getY(tile) - 0.5 * Tile.getAge(tile)))
				elif Tile.getAge(tile) < 6:
					image = pygame.image.load("assets/" + str(Tile.getValue(tile)) + ".png")
					image = pygame.transform.scale(image, (106.25 + (6 - Tile.getAge(tile)) * 7, 106.25 + (6 - Tile.getAge(tile)) * 7))
					Tile.setAge(tile, Tile.getAge(tile) + 1)
					window.blit(image, (300 + 121.25 * Tile.getX(tile) - 0.5 * Tile.getAge(tile), \
						300 + 121.25 * Tile.getY(tile) - 0.5 * Tile.getAge(tile)))
				else:
					image = pygame.image.load("assets/" + str(Tile.getValue(tile)) + ".png")
					window.blit(image, (300 + 121.25 * Tile.getX(tile), \
						300 + 121.25 * Tile.getY(tile)))

# def displayBoard(window, oldBoard, newBoard = []):
# 	if newBoard == []:
# 		newBoard = deepCopy(oldBoard)
# 	for i in range(4):
# 		for j in range(4):
# 			if oldBoard[i][j] != None:
# 				tile = oldBoard[i][j]
# 				# coord = findInBoard(newBoard, tile)
# 				# newX = coord[0]
# 				# newY = coord[1]
# 				image = pygame.image.load("2048/assets/" + str(Tile.getValue(tile)) + '.png')
# 				window.blit(image, (300 + 121.25 * Tile.getX(tile), \
# 					300 + 121.25 * Tile.getY(tile)))
# 				# if newX != i:
# 				# 	temp = 0
# 				# 	while temp <= 10:
# 				# 		window.blit(image, (300 + 121.25 * Tile.getX(tile) + 12.125 * temp, \
# 				# 			300 + 121.25 * Tile.getY(tile)))
# 				# 		# animate
# 				# 		if newX > i:
# 				# 				temp += 1
# 				# 		else:
# 				# 			temp -= 1
# 				# elif newY != j:
# 				# 	temp = 0
# 				# 	while temp <= 10:
# 				# 		window.blit(image, (300 + 121.25 * Tile.getX(tile), \
# 				# 			300 + 121.25 * Tile.getY(tile) + 12.125 * temp))
# 				# 		# animate
# 				# 		if newY > j:
# 				# 				temp += 1
# 				# 		else:
# 				# 			temp -= 1
# 				# else:
# 				# 	window.blit(image, (300 + 121.25 * Tile.getX(tile), \
# 				# 		300 + 121.25 * Tile.getY(tile)))

def findInBoard(board, tile):
	for i in range(4):
		for j in range(4):
			if board[i][j] == tile:
				return [i, j]
	return [0, 0]

def printBoard(board):
	for i in range(4):
		for j in range(4):
			if board[i][j] != None:
				print(str(board[i][j]))
			else:
				print(str(i) + ", " + str(j) + ": None")
	print("----------")

main()