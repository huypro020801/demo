import pygame, sys
from pygame.locals import *
import random

WINDOWWIDTH = 800  # Chiều rộng cửa sổ
WINDOWHEIGHT = 600  # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

# Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

# Xác định màn hình play
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Snake')
icon = pygame.image.load('snake1.jpg')
pygame.display.set_icon(icon)





while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    pygame.display.update()
    fpsClock.tick(FPS)