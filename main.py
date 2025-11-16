import pygame

pygame.init()
win = pygame.display.set_mode((600, 300))

pygame.display.set_caption("CarDrive")

road = pygame.image.load('image/road.png')
car_1 = pygame.image.load('image/redCar.png')
car_2 = pygame.image.load('image/blueCar.png')
car_3 = pygame.image.load('image/whiteCar.png')
end = pygame.image.load('image/end.png')
play = pygame.image.load('image/play.png')
tutor = pygame.image.load('image/Tutor.png')
exit = pygame.image.load('image/exit.png')
frame = pygame.image.load('image/frame.png')
tutorText = pygame.image.load('image/control.png')
text_f = pygame.image.load('image/text_f.png')

x = 490
y = 230
width = 100
haight = 53
speed = 5

x_1 = -100
y_1 = 50

x_2 = -100
y_2 = 200

frame_x = 100
frame_y = 25

loss = False
movline = False
menu = True
run = True
control = True

def drawWindow():
    win.blit(road, (0, 0))
    win.blit(car_1, (x, y))
    win.blit(car_2, (x_1, y_1))
    win.blit(car_3, (x_2, y_2))
    if loss == True:
        win.blit(end, (0, 0))
    
    pygame.display.update()

while menu:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            run = False
    
    win.blit(road, (0, 0))
    win.blit(play, (100,25))
    win.blit(tutor, (100,90))
    win.blit(exit, (100,155))
    win.blit(text_f, (0, 0))
    win.blit(frame, (frame_x,frame_y))
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and frame_y > 25:
        frame_y -= 65
    if keys[pygame.K_DOWN] and frame_y < 155:
        frame_y += 65
    if keys[pygame.K_f]:
        if frame_y == 25:
            menu = False
        if frame_y == 90:

            while control:
                pygame.time.delay(100)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        control = False
                        menu = False
                        run = False

                win.blit(road, (0, 0))
                win.blit(tutorText, (0, 0))
                pygame.display.update()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    control = False

        if frame_y == 155:
            menu = False
            run = False

while run:
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if x_1 <= 600:
        x_1 += 3
    elif x_1 >= 600:
        x_1 = -100
    else:
        x_1 = -100

    if x_2 <= 600:
        x_2 += 5
    elif x_2 >= 600:
        x_2 = -100
    else:
        x_2 = -100

    if x_2 >= x - width and x_2 <= x + width and y_2 >= y - haight and y_2 <= y + haight or x_1 >= x - width and x_1 <= x + width and y_1 >= y - haight and y_1 <= y + haight:
            loss = True
            while loss:
                pygame.time.delay(100)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loss = False
                        run = False

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    loss = False
                    run = False

                drawWindow()
                    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y > 10:
        y -= speed
    if keys[pygame.K_DOWN] and y < 300 - haight - 10:
        y += speed

    drawWindow()

pygame.quit()