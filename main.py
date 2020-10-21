import pygame
import os
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
tiles = pygame.image.load('tiles.png')
font = pygame.font.Font('Nexa Light.otf', 24)

while True:
    screen.fill((0,0,0))
    screen.blit(tiles, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_SPACE:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass

    pygame.display.update()
