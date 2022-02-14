import pygame
import random
class Tile:
    board = [[[] for i in range(4)] for i in range(4)]
    for i in range(0, 4):
        for j in range(0, 4):
            board[i][j] = -1

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
        self.image = pygame.image.load("2048/assets/" + str(self.value) + '.png')
        self.x = random.randrange(0, 4) 
        self.y = random.randrange(0, 4) 
        if not Tile.isBoardFull():
            while Tile.board[self.x][self.y] != -1:
                self.x = random.randrange(0, 4) 
                self.y = random.randrange(0, 4) 
            Tile.board[self.x][self.y] = self.value

    def isBoardFull():
        for i in range(0, 4):
            for j in range(0, 4):
                print(str(i) + str(j) + str(Tile.board[i][j]))
                if Tile.board[i][j] == -1:
                    return False
        return True

    def display(self):
        self.window.blit(self.image, (300 + 121.25 * self.x, 300 + 121.25 * self.y))
        Tile.board[self.x][self.y] = self

    def leftArrow(self):
        pass


    def rightArrow(self):
        pass

    def upArrow(self):
        pass

    def downArrow(self):
        pass
