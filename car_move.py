import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 400  # Chiều dài cửa sổ
WINDOWHEIGHT = 300  # Chiều cao cửa sổ


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (24, 106, 166)
YELLOW = (239, 164, 49)

pygame.init()

### Xác định FPS ###
FPS = 200
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Animation')

class Car1():
    def __init__(self):
        ## Tạo surface và vẽ hình chiếc xe lên đó ##
        self.surface = pygame.Surface((100, 50), SRCALPHA)
        pygame.draw.polygon(self.surface, YELLOW, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
        pygame.draw.circle(self.surface, BLUE, (15, 40), 10)
        pygame.draw.circle(self.surface, BLUE, (85, 40), 10)

    def draw(self):
        DISPLAYSURF.blit(self.surface, (150, 100))

class Car():
    def __init__(self):
        self.x = -98  # Vị trí của xe
        self.xx = -100

        ## Tạo surface và vẽ hình chiếc xe lên đó ##
        self.surface = pygame.Surface((100, 50), SRCALPHA)
        pygame.draw.polygon(self.surface, RED, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
        pygame.draw.circle(self.surface, GREEN, (15, 40), 10)
        pygame.draw.circle(self.surface, GREEN, (85, 40), 10)

    def draw(self):  # Hàm dùng để vẽ xe
        DISPLAYSURF.blit(self.surface, (self.x, 100))
        DISPLAYSURF.blit(self.surface, (self.xx, 100))

    def update(self, STOP):  # Hàm dùng để thay đổi vị trí xe
        if STOP == False:
            self.x += 2
            if self.x + 100 >= WINDOWWIDTH:
                self.xx += 2
            if self.x > WINDOWWIDTH:
                self.x = 0
                self.xx = -100
car1 = Car1()
car = Car()
STOP = False
move_LEFT = False
move_RIGHT = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)
    if event.type == pygame.KEYDOWN:
        STOP = True

    if event.type == pygame.KEYUP:
        STOP = False
    car1.draw()
    car.draw()
    car.update(STOP)

    pygame.display.update()
    fpsClock.tick(FPS)