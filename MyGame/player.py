import pygame
from exceptions import BangException
from background import win

pygame.init()

class Player:
    def __init__(self, name, skin, x, y, height, width, speed):
        self.name = name
        self.skin = skin
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed

    def drawPlayer(self):
        win.blit(self.skin, (self.x, self.y))
        pygame.display.update()

    def get_rect(self):
        return pygame.rect(self.x, self.y, self.width, self.height)