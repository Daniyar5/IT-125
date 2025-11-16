import pygame
from exceptions import BangException
from background import win

pygame.init()

class NPC():
    def __init__(self, x, y, height, width, speed, skin):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.skin = skin
        
    def draw(self):
        win.blit(self.skin, (self.x, self.y))
        pygame.display.update()

    def move(self):
        self.x += self.speed

class Car(NPC):
    def __init__(self, x, y, height, width, speed, skin):
        super().__init__(x, y, height, width, speed, skin)

    def draw(self):
        return super().draw()
    
    def move(self):
        return super().move()
    
class Man(NPC):
    def __init__(self, x, y, height, width, speed, skin):
        super().__init__(x, y, height, width, speed, skin)

    def draw(self):
        return super().draw()
    
    def move(self):
        return super().move() 
        
        
