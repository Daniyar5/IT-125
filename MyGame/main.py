import pygame
from background import drawBg, moveBg
from menu import drawMenu
from control import control, get_game_state
from startPlay import startPlay
from fail import drawFail

pygame.init()

run = True
while run:
    pygame.time.delay(35)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game_state = get_game_state()

    drawBg()

    if game_state.menu == True:
        control.menu()
        drawMenu()
    elif game_state.start == True:
        moveBg()
        startPlay.check_collisions()
        startPlay.moveMen()
        startPlay.moveCars()
        control.player()
        startPlay.drawPoint()
        startPlay.drawPlayers()
        startPlay.drawCars()
        startPlay.drawMen()
    elif game_state.fail == True:
        control.fail()
        drawFail()
    elif game_state.ext == True:
        run = False


