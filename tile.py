import pygame
import random
import variables
class Tile:

    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        self.age = 0

    def __str__(self):
        if self != None:
            return str(self.x) + ", " + str(self.y) + ": " + str(self.value)

    def getValue(self):
        if self != None:
            return self.value
        return -1

    def updateValue(self):
        if self != None:
            self = Tile(self.getX(), self.getY, self.getValue() * 2)

    def updateX(self, x):
        self.x = x

    def updateY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age
