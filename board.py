import pygame
import variables
import random
from movement import *
from tile import Tile

def main():
	pygame.init()
	window = pygame.display.set_mode((1000, 800))
	
	running = True
	pygame.draw.rect(window, variables.DEFAULT_DARK, pygame.Rect(30, 30, 60, 60), 2, 3)
	gameBoard = reset(window)
	setUp(window)
	displayBoard(window, gameBoard)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # terminate
				running = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				newBoard = move(deepCopy(gameBoard), event.key)
				if newBoard != gameBoard:
					gameBoard = spawnTile(newBoard)
					displayBoard(window, gameBoard)
		# set background color 
		window.fill(variables.DEFAULT)
		board = pygame.Rect(285, 285, 500, 500)
		pygame.draw.rect(window, variables.DEFAULT_DARK, board, 0, 0, 3, 3, 3, 3)

		image = pygame.image.load("assets/logo_small.png")
		window.blit(image, (280, 55))

		for x in range (0, 4):
			for y in range (0, 4):
				rect = pygame.Rect(300 + 121.25 * x, 300 + 121.25 * y, 106.25, 106.25)
				pygame.draw.rect(window, variables.DEFAULT_TAN, rect, 0, 0, 3, 3, 3, 3)

		# Drawing Rectangle
		pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(670, 70, 80, 60), 0, 0, 3, 3, 3, 3)
		fontObj2 = pygame.font.SysFont("arial bold", 20)
		textSurfaceObj2 = fontObj2.render('Score', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
		textRectObj2 = textSurfaceObj2.get_rect()
		textRectObj2.center  = (710, 80)
		window.blit(textSurfaceObj2, textRectObj2)

		fontObj2 = pygame.font.SysFont("arial bold", 40)
		textSurfaceObj2 = fontObj2.render(str(getScore()), True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
		textRectObj2 = textSurfaceObj2.get_rect()
		textRectObj2.center  = (710, 110)
		window.blit(textSurfaceObj2, textRectObj2)

		# display board
		if not gameOverCheck(window, gameBoard):
			displayBoard(window, gameBoard)
		pygame.display.update()
		pygame.display.flip()
	pygame.quit()

def setUp(window):
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
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center  = (700, 130)
	window.blit(textSurfaceObj2, textRectObj2)

	pygame.display.flip()

def deepCopy(board):
	ret = [[[] for i in range(4)] for i in range(4)]
	for i in range(4):
		for j in range(4):
			ret[i][j] = board[i][j]
	return ret

def displayBoard(window, board):
	for i in range(4):
		for j in range(4):
			if board[i][j] != None:
				tile = board[i][j]
				image = pygame.image.load("assets/" + str(Tile.getValue(tile)) + ".png")
				window.blit(image, (300 + 121.25 * i, 300 + 121.25 * j))
	pygame.display.flip()

def findInBoard(board, tile):
	for i in range(4):
		for j in range(4):
			if board[i][j] == tile:
				return [i, j]
	return [0, 0]

def gameOverCheck(window, board):
	if isBoardFull(board):
		pygame.draw.rect(window, variables.DEFAULT_TAN, pygame.Rect(285, 285, 500, 500), 0, 0, 3, 3, 3, 3)
		fontObj = pygame.font.SysFont("arial bold", 70)
		textSurfaceObj = fontObj.render('You lose!', True, variables.DEFAULT_DARK2, variables.DEFAULT_TAN)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center  = (550, 400)
		window.blit(textSurfaceObj, textRectObj)
		return True
	return False

def reset(window):
	board = [[[] for i in range(4)] for j in range(4)]
	for i in range(0, 4):
		for j in range(0, 4):
			board[i][j] = None
	board = spawnTile(board)
	board = spawnTile(board)
	displayBoard(window, board)
	return board

def printBoard(board):
	for i in range(4):
		for j in range(4):
			print(str(i) + ", " + str(j) + ": " + str(Tile.getValue(board[i][j])))
	return [0, 0]

main()