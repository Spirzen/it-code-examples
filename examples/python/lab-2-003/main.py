# game_loop.py

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 40))
    pygame.display.flip()
pygame.quit()
