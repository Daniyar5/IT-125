import pygame
from exceptions import BangException
from menu import get_menu_state
from game import get_game_state
from startPlay import player_1
from fail import get_fail_state

pygame.init()

class Control:
    def __init__(self):
        self.lastSwitchTime = 0
        self.cooldownTime = 300

    def menu(self):
        keys = pygame.key.get_pressed()
        menu_state = get_menu_state()
        game_state = get_game_state()
        currentTime = pygame.time.get_ticks()
        
        if menu_state.p == False and menu_state.c == False and menu_state.e == False:
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                menu_state.p = True
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                menu_state.p = True
        if  currentTime - self.lastSwitchTime >= self.cooldownTime:
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if menu_state.p == True:
                    menu_state.p = False
                    menu_state.c = True
                    menu_state.e = False
                    self.lastSwitchTime = currentTime
                elif menu_state.c == True:
                    menu_state.p = False
                    menu_state.c = False
                    menu_state.e = True
                    self.lastSwitchTime = currentTime
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                if menu_state.e == True:
                    menu_state.p = False
                    menu_state.c = True
                    menu_state.e = False
                    self.lastSwitchTime = currentTime
                elif menu_state.c:
                    menu_state.p = True
                    menu_state.c = False
                    menu_state.e = False
                    self.lastSwitchTime = currentTime

        if keys[pygame.K_f]:
            if menu_state.p == True:
                menu_state.p = False
                game_state.start = True
                game_state.menu = False
                self.lastSwitchTime = 0
            elif menu_state.c == True:
                self.lastSwitchTime = 0
            elif menu_state.e == True:
                game_state.menu = False
                game_state.ext = True
                self.lastSwitchTime = 0
            
    
    def player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if player_1.y >= 40:
                player_1.y -= player_1.speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if player_1.y <= 290 - player_1.height:
                player_1.y += player_1.speed

    def fail(self):
        keys = pygame.key.get_pressed()
        fail_state = get_fail_state()
        game_state = get_game_state()
        currentTime = pygame.time.get_ticks()

        if  currentTime - self.lastSwitchTime >= self.cooldownTime:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if fail_state.p == True:
                    fail_state.p = False
                    fail_state.m = True
                    self.lastSwitchTime = currentTime
                elif fail_state.m == True:
                    fail_state.m = False
                    fail_state.r = True
                    self.lastSwitchTime = currentTime
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if fail_state.r == True:
                    fail_state.r = False
                    fail_state.m = True
                    self.lastSwitchTime = currentTime
                elif fail_state.m == True:
                    fail_state.m = False
                    fail_state.p = True
                    self.lastSwitchTime = currentTime

            if keys[pygame.K_f]:
                if fail_state.r == True:
                    game_state.start = True
                    game_state.fail = False
                    self.lastSwitchTime = 0
                elif fail_state.m == True:
                    game_state.menu = True
                    game_state.fail = False
                    game_state.start = False
                    self.lastSwitchTime = 0

control = Control()