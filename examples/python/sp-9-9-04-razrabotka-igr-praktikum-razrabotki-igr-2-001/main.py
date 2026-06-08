import sys
import pygame

pygame.init()

GRID_SIZE = 8
TILE_SIZE = 58
CELL_GAP = 5
BOARD_PAD = 18
FRAME = 14
HEADER_H = 88
FOOTER_H = 52

BOARD_INNER = GRID_SIZE * TILE_SIZE + (GRID_SIZE - 1) * CELL_GAP
BOARD_W = BOARD_INNER + BOARD_PAD * 2
BOARD_H = BOARD_INNER + BOARD_PAD * 2
WIDTH = BOARD_W + FRAME * 2
HEIGHT = HEADER_H + BOARD_H + FRAME * 2 + FOOTER_H
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Match-3 — этап 0")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((18, 12, 40))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
