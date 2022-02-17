from decimal import ROUND_DOWN
from multiprocessing.sharedctypes import Value
import pygame
import random
from tile import Tile

class Score:
    score = 0

def checkWin(board):
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] != None:
                if Tile.getValue(board[i][j]) >= 2048:
                    return True
    return False

def isBoardFull(board):
	for i in range(0, 4):
		for j in range(0, 4):
			if board[i][j] == None:
				return False
			if j != 3 and board[i][j] == board[i][j+1] or \
                i != 3 and board[i][j] == board[i + 1][j]:
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
            updateScore(value)
    return board

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

def updateScore(value):
    Score.score += value

def getScore():
    return Score.score

def upArrow(board):
	board = shiftUp(board)
	for i in range(0, 4):
		for j in range(0, 3):
			t = board[i][j]
			t1 = board[i][j + 1]
			if t != None and t1 != None and Tile.getValue(t) == Tile.getValue(t1):
				board[i][j] = Tile(Tile.getX(t), Tile.getY(t), Tile.getValue(t) * 2)
				board[i][j + 1] = None
				j = 0, updateScore(Tile.getValue(t) * 2)
	board = shiftUp(board)
	return board

def downArrow(board):
	board = shiftDown(board)
	for i in range(0, 4):
		for j in range(3, 0, -1):
			t = board[i][j]
			t1 = board[i][j - 1]
			if t != None and t1 != None and Tile.getValue(t) == Tile.getValue(t1):
				board[i][j] = Tile(Tile.getX(t), Tile.getY(t), Tile.getValue(t) * 2)
				board[i][j - 1] = None
				j = 0, updateScore(Tile.getValue(t) * 2)
	board = shiftDown(board)
	return board

def leftArrow(board):
    board = rotate(board)
    board = upArrow(board)
    board = rotate(board)
    board = rotate(board)
    board = rotate(board)
    return board

def rightArrow(board):
    board = rotate(board)
    board = upArrow(board)
    board = shiftDown(board)
    board = rotate(board)
    board = rotate(board)
    board = rotate(board)
    return board

def shiftUp(board):
    for i in range(0, 4):
        row = []
        count = 0
        for j in range(0, 4):
            t = board[i][j]
            if t != None:
                row.append(t)
                count  += 1
        board[i] = row
        board[i].extend([None] * (4 - count))
    return board

def shiftDown(board):
    for i in range(0, 4):
        row = []
        count = 0
        for j in range(0, 4):
            t = board[i][j]
            if t != None:
                row.append(t)
                count  += 1
        board[i] = [None] * (4 - count)
        board[i].extend(row)
    return board

def rotate(board):
    return [[board[j][i] for j in range(4)] for i in range(3, -1, -1)]