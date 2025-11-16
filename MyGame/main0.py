import pygame
import random

clock = pygame.time.Clock()

pygame.init()

win = pygame.display.set_mode((600, 300))
pygame.display.set_caption("CarDrive")

# icon = pygame.image.load('car.ico')
# pygame.display.set_icon(icon)

play = [
    pygame.image.load('sprites/Menu/play1.png'),
    pygame.image.load('sprites/Menu/play2.png')
        ]
control = [
    pygame.image.load('sprites/Menu/control1.png'),
    pygame.image.load('sprites/Menu/control2.png')
        ]
exit = [
    pygame.image.load('sprites/Menu/exit1.png'),
    pygame.image.load('sprites/Menu/exit2.png')
        ]
button_play = [
    pygame.image.load('sprites/Fail/play_blue_0.png'),
    pygame.image.load('sprites/Fail/play_blue_1.png')
]
button_reset = [
    pygame.image.load('sprites/Fail/reset_blue_0.png'),
    pygame.image.load('sprites/Fail/reset_blue_1.png')
]
button_menu = [
    pygame.image.load('sprites/Fail/menu_blue_0.png'),
    pygame.image.load('sprites/Fail/menu_blue_1.png')
]

text = [
    pygame.image.load('sprites/Text/text_hint_1.png'),
    pygame.image.load('sprites/Text/text_hint_2.png'),
    pygame.image.load('sprites/Text/text_control.png')
    ]
road = pygame.image.load('sprites/Play/road.png')

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

fail_bg = pygame.image.load('sprites/Fail/fail_bg.png')
fail_text = [pygame.image.load('sprites/Fail/text_fail_1.png'),
             pygame.image.load('sprites/Fail/text_fail_2.png'),
             pygame.image.load('sprites/Fail/text_fail_3.png')
             ]
man = [
    pygame.image.load('sprites/Play/man_stand.png'),
    pygame.image.load('sprites/Play/man_run_1.png'),
    pygame.image.load('sprites/Play/man_run_2.png')
]

manAnim = [
    pygame.image.load('sprites/Play/man_up.png'),
    pygame.image.load('sprites/Play/man_left.png'),
    pygame.image.load('sprites/Play/man_down.png'),
    pygame.image.load('sprites/Play/man_right.png')
]

man_anim_count = 0

class NPC():
    def __init__(self, x, y, height, width, speed, skin):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.skin = skin
        
    def drawCar(self):
        win.blit(self.skin, (self.x, self.y))

class Men():
    def __init__(self, x, y, skin):
        self.x = x
        self.y = y
        self.skin = skin
        self.height = 44
        self.width = 20

    def drawMan(self):
        win.blit(self.skin, (self.x, self.y))

man_1 = Men(-100, 5, man[man_anim_count])

car_1 = NPC(skin = cars_left[0],height = 46, width = 100, speed = 5, x = -110, y = 60)
car_2 = NPC(skin = cars_right[1],height = 46, width = 100, speed = 10, x = -110, y = 170)
car_3 = NPC(skin = cars_right[2],height = 46, width = 100, speed = 12, x = -110, y = 230)
car_4 = NPC(skin = cars_left[2],height = 46, width = 100, speed = 6, x = -110, y = 100)

player = cars_left[0]
player_x = 480
player_y = 237
player_height = 46
player_width = 100
player_speed = 5

road_x = 0

cooldownTime = 300
lastSwitchTime = 0

playButton = False
controlButton = False
exitButton = False

stat_b_p = False
stat_b_r = False
stat_b_m = False

Menu = True
Start = False
Fail = False
Control = False
RipMan = False

point = 0
font = pygame.font.SysFont('Arial', 24)
    
def drawWindow():
    if Menu == True:
        win.blit(road, (road_x, 0))
        win.blit(road, (road_x - 600, 0))
        win.blit(play[playButton], (100, 50))
        win.blit(control[controlButton], (100, 115))
        win.blit(exit[exitButton], (100, 180))
        win.blit(text[0],(10, 265))
    elif Start == True:
        win.blit(road, (road_x, 0))
        win.blit(road, (road_x - 600, 0))
        car_1.drawCar()
        car_2.drawCar()
        car_3.drawCar()
        car_4.drawCar()
        man_1.drawMan()
        win.blit(player, (player_x, player_y))
        win.blit(text_point, (5, 5))
    elif Fail == True:
        win.blit(fail_bg, (100, 50))
        fail_bg.blit(fail_text[0], (110, 25))
        fail_bg.blit(fail_text[1], (175, 50))
        fail_bg.blit(fail_text[2], (112, 75))
        win.blit(text[1], (10, 265))
        fail_bg.blit(button_play[stat_b_p], (70, 125))
        fail_bg.blit(button_menu[stat_b_m], (170, 125))
        fail_bg.blit(button_reset[stat_b_r], (270, 125))
    elif Control == True:
        win.blit(road, (road_x, 0))
        win.blit(road, (road_x - 600, 0))
        win.blit(text[2], (0, 0))

    pygame.display.update()

run = True
while run:
    currentTime = pygame.time.get_ticks()
    pygame.time.delay(35)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    # man_1.x = random.randint(10, 580)
    NPC_y_left = random.randint(60, 120)
    NPC_y_right = random.randint(160, 250)
    NPC_image_left = random.choice(cars_left)
    NPC_image_right = random.choice(cars_right)
    NPC_spawn_x = random.randint(-200, -110)

    if Menu == True:
        Start = False
        Fail = False
    if Fail == True:
        Start = False
        Menu = False
    if Start == True:
        Menu = False
        Fail = False

    text_point = font.render(f"Point: {point}", True, (0, 191, 255))

    keys = pygame.key.get_pressed()
    if Menu == True:
        if  currentTime - lastSwitchTime > cooldownTime:
            if keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_UP] or keys[pygame.K_w] and playButton == False and controlButton == False and exitButton == False:
                lastSwitchTime = currentTime
                playButton = True
            if keys[pygame.K_DOWN] and playButton or keys[pygame.K_s] and playButton:
                lastSwitchTime = currentTime
                controlButton = True
                playButton = False
                exitButton = False
            if keys[pygame.K_UP]  and controlButton or keys[pygame.K_w] and controlButton:
                lastSwitchTime = currentTime
                playButton = True
                controlButton = False
                exitButton = False
            if keys[pygame.K_DOWN]  and controlButton or keys[pygame.K_s] and controlButton:
                lastSwitchTime = currentTime
                exitButton = True
                controlButton = False
                playButton = False
            if keys[pygame.K_UP] and exitButton or keys[pygame.K_w] and exitButton:
                lastSwitchTime = currentTime
                controlButton = True
                exitButton = False
                playButton = False         

    if keys[pygame.K_f] and playButton == True:
        playButton = False
        controlButton = False
        exitButton = False
        Menu = False
        Start = True
    elif keys[pygame.K_f] and exitButton:
        run = False
    if keys[pygame.K_f] and controlButton == True:
        Control = True

    if RipMan == True:
        man_1.y += 12
        man_1.x -= man_1_x
        man_1.skin = manAnim[man_anim_count]
        if man_anim_count == 3:
            man_anim_count = 0
        else:
            man_anim_count += 1
        if man_1.y >= 300:
            man_1.x = random.randint(20, 600)
            man_1.x *= -1
            man_1.y = 5
            man_anim_count = 0
            man_1.skin = man[man_anim_count]
            RipMan = False

    if Start == True:
        road_x += 8
        if road_x >= 600:
            road_x = 0
        man_1.x += 8
        if man_1.x >= 600:
            man_1.x = random.randint(20, 600)
            man_1.x *= -1
        if player_x <= man_1.x + 100 and player_y <= 40:
            if man_1.y < 30:
                man_1.y += 8
        if player_x <= man_1.x + man_1.width and player_x >= man_1.x + man_1.width -20  and player_y <= man_1.y + man_1.height:
            man_1_x = random.randint(14, 20)
            point += 1 
            RipMan = True

        if keys[pygame.K_UP] and player_y >= 40 or keys[pygame.K_w] and player_y >= 40:
            player_y -= player_speed
        elif keys[pygame.K_DOWN] and player_y <= 300 - player_height - 5 or keys[pygame.K_s] and player_y <= 300 - player_height - 5:
            player_y += player_speed

        if car_1.x < 600 + car_1.width:
            car_1.x += car_1.speed
        else:
            car_1.y = NPC_y_left
            car_1.skin = NPC_image_left
            car_1.x = -110

        if car_2.x < 600 + car_2.width:
            car_2.x += car_2.speed
        else:
            car_2.y = NPC_y_right
            car_2.skin = NPC_image_right
            car_2.x = -110
            
        if car_3.x < 600 + car_3.width:
            car_3.x += car_3.speed
        else:
            car_3.y = NPC_y_right
            car_3.skin = NPC_image_right
            car_3.x = -110

        if car_4.x < 600 + car_4.width:
            car_4.x += car_4.speed
        else:
            car_4.y = NPC_y_left
            car_4.skin = NPC_image_left
            car_4.x = -110

    if car_1.x > player_x - player_width and car_1.x < player_x + player_width - 10 and car_1.y > player_y - player_height + 16 and car_1.y + 16 < player_y + player_height:
        Fail = True
    if car_2.x > player_x - player_width and car_2.x < player_x + player_width - 10 and car_2.y > player_y - player_height + 16 and car_2.y + 16 < player_y + player_height:
        Fail = True
    if car_3.x > player_x - player_width and car_3.x < player_x + player_width - 10 and car_3.y > player_y - player_height + 16 and car_3.y + 16 < player_y + player_height:
        Fail = True
    if car_4.x > player_x - player_width and car_4.x < player_x + player_width - 10 and car_4.y > player_y - player_height + 16 and car_4.y + 16 < player_y + player_height:
        Fail = True

    if Fail == True:
        if  currentTime - lastSwitchTime > cooldownTime:
            if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] and stat_b_p == False and stat_b_m == False and stat_b_r == False:
                lastSwitchTime = currentTime
                stat_b_p = True
            if keys[pygame.K_RIGHT] and stat_b_p == True or keys[pygame.K_d] and stat_b_p == True:
                lastSwitchTime = currentTime
                stat_b_m = True
                stat_b_p = False
                stat_b_r = False
            elif keys[pygame.K_RIGHT] and stat_b_m == True or keys[pygame.K_d] and stat_b_m == True:
                lastSwitchTime = currentTime
                stat_b_r = True
                stat_b_m = False
                stat_b_p = False
            elif keys[pygame.K_LEFT] and stat_b_r == True or keys[pygame.K_a] and stat_b_r == True:
                lastSwitchTime = currentTime
                stat_b_m = True
                stat_b_r = False
                stat_b_p = False
            elif keys[pygame.K_LEFT] and stat_b_m == True or keys[pygame.K_a] and stat_b_m == True:
                lastSwitchTime = currentTime
                stat_b_p = True
                stat_b_m = False
                stat_b_r = False

    if keys[pygame.K_f] and stat_b_r == True:
        stat_b_r = False
        stat_b_m = False
        stat_b_p = False
        Fail = False
        point = 0
        player_y = 237
        car_1.x = -110
        car_2.x = -110
        car_3.x = -110
        car_4.x = -110
        Start = True
    if keys[pygame.K_f] and stat_b_m == True:
        stat_b_m = False
        stat_b_r = False
        stat_b_p = False
        Fail = False
        point = 0
        player_y = 237
        car_1.x = -110
        car_2.x = -110
        car_3.x = -110
        car_4.x = -110
        Menu = True

    clock.tick(30)
    drawWindow()

pygame.quit()
