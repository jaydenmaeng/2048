import pygame
import random
import variables
class Tile:
    board = [[[] for i in range(4)] for i in range(4)]
    for i in range(0, 4):
        for j in range(0, 4):
            board[i][j] = None

    def __init__(self, window, value=-1):
        self.window = window
        if value == -1:
            temp = random.randrange(0, 10)
            if temp == 0:
                self.value = 4
            else:
                self.value = 2
        else:
            self.value = value
        self.image = pygame.image.load("assets/" + str(self.value) + '.png')
        self.x = random.randrange(0, 4) 
        self.y = random.randrange(0, 4) 
        if not Tile.isBoardFull():
            while Tile.board[self.x][self.y] != None:
                self.x = random.randrange(0, 4) 
                self.y = random.randrange(0, 4) 
            Tile.board[self.x][self.y] = self

    def __str__(self):
        if self != None:
            return str(self.x) + ", " + str(self.y) + ": " + str(Tile.getValue(self.board[self.x][self.y]))

    def printBoard():
        for i in range(4):
            for j in range(4):
                if Tile.board[i][j] != None:
                    print(str(Tile.board[i][j]))
                else:
                    print(str(i) + ", " + str(j) + ": None")
        print("----------")

    def remove(self):
        self.image.fill(variables.TRANSPARENT)
        Tile.board[Tile.getX(self)][Tile.getY(self)] = None
        self = None

    def getValue(self):
        if self != None:
            return self.value
        return -1

    def updateValue(self):
        if self != None:
            self.value = self.getValue() * 2

    def updateX(self, x):
        self.x = x

    def updateY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def isBoardFull():
        for i in range(0, 4):
            for j in range(0, 4):
                if Tile.board[i][j] == None:
                    return False
        return True

    def display(self):
        if self != None:
            self.image = pygame.image.load("assets/" + str(self.value) + '.png')
            self.window.blit(self.image, (300 + 121.25 * self.x, 300 + 121.25 * self.y))
            Tile.board[self.x][self.y] = self