import pygame
from button import button

pygame.init()

def control_mouse():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            button.check_click(mouse_pos)
    return True