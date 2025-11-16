import pygame
from exceptions import BangException
from window import win

pygame.init()

road = pygame.image.load('sprites/Play/road.png')
road_x = 0

class BG:
    def __init__(self):
        self.road = pygame.image.load('sprites/Play/road.png')
        self.x = 0
        self.speed = 8

    def drawBg(self):
        win.blit(self.road, (self.x, 0))
        win.blit(self.road, (self.x - 600, 0))
        pygame.display.update()

    def moveBg(self):
        self.x += self.speed

        if self.x >= 600:
            self.x = 0

bg = BG()

def drawBg():
    bg.drawBg()
    pygame.display.update()

def moveBg():
    bg.moveBg()