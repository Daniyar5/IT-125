import pygame
from exceptions import BangException
from window import win

pygame.init()

play = [
    pygame.image.load('sprites/Menu/play1.png'),
    pygame.image.load('sprites/Menu/play2.png')
        ]
control = [
    pygame.image.load('sprites/Menu/control1.png'),
    pygame.image.load('sprites/Menu/control2.png')
        ]
ext = [
    pygame.image.load('sprites/Menu/exit1.png'),
    pygame.image.load('sprites/Menu/exit2.png')
        ]
text = pygame.image.load('sprites/Text/text_hint_1.png')

class MenuState:
    def __init__(self):
        self.p = True
        self.c = False
        self.e = False

menu_state = MenuState()

def drawMenu():
    win.blit(play[menu_state.p], (100, 50))
    win.blit(control[menu_state.c], (100, 115))
    win.blit(ext[menu_state.e], (100, 180))
    win.blit(text,(10, 265))
    pygame.display.update()

def get_menu_state():
    return menu_state