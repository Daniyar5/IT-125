import pygame
from win import win

pygame.init()

class Button:
    def __init__(self):
        self.hihiha_imag = pygame.transform.scale(pygame.image.load('memImag/kingHihiha.jpeg'), (100, 100))
        self.hogRida_imag = pygame.transform.scale(pygame.image.load('memImag/hogRider.jpeg'), (100, 100))
        self.cry_imag = pygame.transform.scale(pygame.image.load('memImag/cry.jpeg'), (100, 100))
        self.bu_imag = pygame.transform.scale(pygame.image.load('memImag/bu.jpeg'), (100, 100))
        self.grr_imag = pygame.transform.scale(pygame.image.load('memImag/grr.jpeg'), (100, 100))
        self.mimi_imag = pygame.transform.scale(pygame.image.load('memImag/mimi.jpeg'), (100, 100))
        self.amogus_imag = pygame.transform.scale(pygame.image.load('memImag/amogus.jpeg'), (100, 100))
        self.yipee_imag = pygame.transform.scale(pygame.image.load('memImag/yipee.jpeg'), (100, 100))
        self.goida_imag = pygame.transform.scale(pygame.image.load('memImag/goida.jpeg'), (100, 100))

        self.hihiha_sound = pygame.mixer.Sound("memSounds/Heheha.mp3")
        self.hogRida_sound = pygame.mixer.Sound('memSounds/hogRida.mp3')
        self.cry_sound = pygame.mixer.Sound('memSounds/cry.mp3')
        self.bu_sound = pygame.mixer.Sound('memSounds/bu.mp3')
        self.grr_sound = pygame.mixer.Sound('memSounds/grr.mp3')
        self.mimi_sound = pygame.mixer.Sound('memSounds/mimi.mp3')
        self.amogus_sound = pygame.mixer.Sound('memSounds/amogus.mp3')
        self.yipee_sound = pygame.mixer.Sound('memSounds/yipee.mp3')
        self.goida_sound = pygame.mixer.Sound('memSounds/goida.mp3')

        self.bu_sound.set_volume(3)

        self.imagMems = [self.hihiha_imag, self.hogRida_imag, self.cry_imag, self.bu_imag, 
                         self.grr_imag, self.mimi_imag, self.amogus_imag, self.yipee_imag,
                         self.goida_imag]
        self.soundMems = [self.hihiha_sound, self.hogRida_sound, self.cry_sound, self.bu_sound, 
                          self.grr_sound, self.mimi_sound, self.amogus_sound, self.yipee_sound,
                          self.goida_sound]
        
        self.rects = []
        x, y = 0, 0
        for imag in self.imagMems:
            rect = imag.get_rect(topleft=(x, y))
            self.rects.append(rect)
            x += 100
            if x >= 300:
                x = 0
                y += 100
    
    def drawButton(self):
        self.x, self.y = 0, 0
        for imagMem in self.imagMems:
            win.blit(imagMem, (self.x, self.y))
            self.x += 100
            if self.x >= 300:
                self.x = 0
                self.y += 100

    def check_click(self, mouse_pos):
        for i, rect in enumerate(self.rects):
            if rect.collidepoint(mouse_pos):
                self.playSound(i)
                return True
        return False
    
    def playSound(self, index):
        if 0 <= index < len(self.soundMems):
            self.soundMems[index].play()

button = Button()