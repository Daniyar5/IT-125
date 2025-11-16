import pygame
from exceptions import BangException
from NPC import Car, Man
from player import Player
from game import get_game_state
from window import win

pygame.init()

cars_left = [
    pygame.image.load('sprites/Play/car_red_left.png'),
    pygame.image.load('sprites/Play/car_purple_left.png'),
    pygame.image.load('sprites/Play/car_green_left.png')
]

cars_right = [
    pygame.image.load('sprites/Play/car_red_right.png'),
    pygame.image.load('sprites/Play/car_purple_right.png'),
    pygame.image.load('sprites/Play/car_green_right.png')
]

man = pygame.image.load('sprites/Play/man_stand.png')

manAnim = [
    pygame.image.load('sprites/Play/man_up.png'),
    pygame.image.load('sprites/Play/man_left.png'),
    pygame.image.load('sprites/Play/man_down.png'),
    pygame.image.load('sprites/Play/man_right.png')
]


start_position = -180

car_1 = Car(skin = cars_left[0],height = 46, width = 100, speed = 5, x = start_position, y = 60)
car_2 = Car(skin = cars_right[1],height = 46, width = 100, speed = 10, x = start_position, y = 170)
car_3 = Car(skin = cars_right[2],height = 46, width = 100, speed = 12, x = start_position, y = 230)
car_4 = Car(skin = cars_left[2],height = 46, width = 100, speed = 6, x = start_position, y = 100)

all_cars = [car_1, car_2, car_3, car_4]

man_1 = Man(start_position, 5, 44, 20, 8, man)

player_1 = Player('Dani', cars_left[0], 480, 237, 46, 100, 5)

font = pygame.font.SysFont('Arial', 24)

class StartPlay:
    def __init__(self):
        self.ripMan = False
        self.point = 0
        self.already_scored = False
        self.man_anim_count = 0

    def moveCars(self):
        for car in all_cars:
            car.move()

            if car.x > 610:
                car.x = start_position

    def drawCars(self):
        for car in all_cars:
            car.draw()
        pygame.display.update()

    def moveMen(self):
        man_1.move()

        if man_1.x > 610:
            man_1.x = start_position
            man_1.y = 5
            self.already_scored = False

        if player_1.x <= man_1.x + 100 and player_1.y <= 40:
            if man_1.y <= 30:
                man_1.y += 8

        if player_1.x < man_1.x + man_1.width and player_1.x + player_1.width > man_1.x:
            if player_1.y < man_1.y + man_1.height and player_1.y + player_1.height > man_1.y:
                self.ripMan = True
                if self.already_scored == False:
                    self.point += 1
                    self.already_scored = True

        if self.ripMan == True:
            man_1.x -= 15
            man_1.y += 10
            if man_1.y >= 320 or man_1.x - man_1.width < -20:
                self.ripMan = False
                man_1.x = start_position
                man_1.y = 5
                self.already_scored = False
        
    def drawPoint(self):
        text_point = font.render(f"Point: {self.point}", True, (0, 191, 255))
        win.blit(text_point, (5, 5))

    def drawMen(self):
        man_1.draw()
        if self.ripMan == True:
            man_1.skin = manAnim[self.man_anim_count]
            if self.man_anim_count == 3:
                self.man_anim_count = 0
            else:
                self.man_anim_count += 1
        
        if self.ripMan == False:
            man_1.skin = man

    def drawPlayers(self):
        player_1.drawPlayer()
        pygame.display.update()

    def check_collisions(self):
        game_state = get_game_state()
        for car in all_cars:
            if player_1.x < car.x + car.width and player_1.x + player_1.width > car.x:
                if player_1.y + 16 < car.y + car.height and player_1.y + player_1.height > car.y + 16:
                    game_state.fail = True
                    game_state.start = False
                    self.point = 0
                    for car in all_cars:
                        car.x = start_position

startPlay = StartPlay()