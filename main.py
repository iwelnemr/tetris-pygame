import pygame
import os
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
tiles = pygame.image.load('tiles.png')
font = pygame.font.Font('Nexa Light.otf', 24)

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
