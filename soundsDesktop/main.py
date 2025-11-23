import pygame
from control import control_mouse
from button import button
from win import win

pygame.init()

run = True
while run:
    run = control_mouse()
    win.fill((0, 0, 0))
    button.drawButton()
    pygame.display.update()

pygame.quit()