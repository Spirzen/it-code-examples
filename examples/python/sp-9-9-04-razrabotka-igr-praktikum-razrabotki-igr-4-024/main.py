import sys

import pygame

import config as C
from game.states import Game

pygame.init()
screen = pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))
pygame.display.set_caption("Racing")
clock = pygame.time.Clock()
game = Game()

running = True
while running:
    dt = clock.tick(C.FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        else:
            game.handle_event(event)

    game.update(dt)
    screen.fill(C.COLOR_GRASS)
    game.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
