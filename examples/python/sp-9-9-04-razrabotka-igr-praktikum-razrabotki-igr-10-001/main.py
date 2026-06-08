"""Bubble Shooter — этап 0 — окно и игровой цикл."""
import math

import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60

GRID_ROWS = 12
GRID_COLS = 15
BUBBLE_RADIUS = 18
BUBBLE_DIAMETER = BUBBLE_RADIUS * 2
BUBBLE_HEIGHT = int(BUBBLE_RADIUS * math.sqrt(3))
GRID_TOP = 40
GRID_LEFT = (WIDTH - (GRID_COLS * BUBBLE_DIAMETER + BUBBLE_RADIUS)) // 2
DANGER_Y = HEIGHT - 120

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Shooter — этап 0")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((24, 26, 34))
    for x in range(GRID_LEFT, WIDTH - GRID_LEFT, 40):
        pygame.draw.line(screen, (34, 36, 46), (x, GRID_TOP), (x, int(DANGER_Y)), 1)
    pygame.draw.line(screen, (220, 70, 70), (GRID_LEFT, int(DANGER_Y)), (WIDTH - GRID_LEFT, int(DANGER_Y)), 2)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
