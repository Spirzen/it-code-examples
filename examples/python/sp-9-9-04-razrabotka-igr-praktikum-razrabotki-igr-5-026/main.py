import sys

import pygame

import settings as S
from game.game import Game

pygame.init()
screen = pygame.display.set_mode((S.SCREEN_W, S.SCREEN_H))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

game = Game()
running = True

while running:
    dt = clock.tick(S.FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif not game.handle_event(event):
            running = False

    game.update(dt)

    screen.fill(S.COLOR_BG)
    game.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
