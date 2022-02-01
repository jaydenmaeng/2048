import pygame

class Tile:
    board = list(list())
    
    def __init__(self, window, value):
        self.window = window
        self.value = value
        
    def spawnRandom(self):
        image = pygame.image.load("2048/" + str(self.value) + '.png')
        self.window.blit(image, (300, 300))