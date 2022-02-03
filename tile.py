import pygame
import random
class Tile:
    board = [[[] for i in range(4)] for i in range(4)]

    def __init__(self, window, value):
        self.window = window
        self.value = value
        self.spawnRandom()

    def isBoardFull(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.board[i][j] == None:
                    return False
        return True

    def spawnRandom(self):
        self.image = pygame.image.load("2048/assets/" + str(self.value) + '.png')
        self.x = random.randrange(0, 4) 
        self.y = random.randrange(0, 4) 
        # if not self.isBoardFull():
        # while(self.board[x][y] != None):
        self.board[self.x][self.y] = self

    def leftArrow(self):
        pass


    def rightArrow(self):

    def upArrow(self):

    def downArrow(self):
