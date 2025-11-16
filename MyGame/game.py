import pygame
from exceptions import BangException

pygame.init()

class GameState:
    def __init__(self):
        self.start = False
        self.menu = True
        self.ext = False
        self.fail = False

game_state = GameState()

def get_game_state():
    return game_state

