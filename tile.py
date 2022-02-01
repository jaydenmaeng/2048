import pygame

class Tile:
    def __init__(self, value):
        self.value = value
        
    def spawnRandom(self, window):
        image = pygame.image.load("2048/" + str(self.value) + '.png')
        window.blit(image, (300, 300))