import pygame
from exceptions import BangException
from window import win

pygame.init()

bg = pygame.image.load('sprites/Fail/fail_bg.png')

text = [
    pygame.image.load('sprites/Fail/text_fail_1.png'),
    pygame.image.load('sprites/Fail/text_fail_2.png'),
    pygame.image.load('sprites/Fail/text_fail_3.png'),
    pygame.image.load('sprites/Text/text_hint_2.png')
]
play = [
    pygame.image.load('sprites/Fail/play_blue_0.png'),
    pygame.image.load('sprites/Fail/play_blue_1.png')
]
reset = [
    pygame.image.load('sprites/Fail/reset_blue_0.png'),
    pygame.image.load('sprites/Fail/reset_blue_1.png')
]
menu = [
    pygame.image.load('sprites/Fail/menu_blue_0.png'),
    pygame.image.load('sprites/Fail/menu_blue_1.png')
]

class FailState:
    def __init__(self):
        self.p = False
        self.r = True
        self.m = False

fail_state = FailState()

def drawFail():
    win.blit(bg, (100, 50))
    bg.blit(text[0], (110, 25))
    bg.blit(text[1], (175, 50))
    bg.blit(text[2], (112, 75))
    win.blit(text[3], (10, 265))
    bg.blit(play[fail_state.p], (70, 125))
    bg.blit(menu[fail_state.m], (170, 125))
    bg.blit(reset[fail_state.r], (270, 125))
    pygame.display.update()

def get_fail_state():
    return fail_state