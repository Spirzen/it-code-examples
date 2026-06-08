#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
GRID = 5
CELL = 80
MARGIN = 40
W = H = MARGIN * 2 + GRID * CELL
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Odd one out")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

base_color = (70, 130, 200)
odd_color = (200, 90, 90)
odd_cell = (random.randint(0, GRID - 1), random.randint(0, GRID - 1))
round_num = 1
message = "Кликни по другому цвету"

def next_round():
    global odd_cell, base_color, odd_color, round_num, message
    round_num += 1
    odd_cell = (random.randint(0, GRID - 1), random.randint(0, GRID - 1))
    base_color = (random.randint(40, 180), random.randint(40, 180), random.randint(80, 220))
    odd_color = tuple(max(0, min(255, c + random.randint(-70, 70))) for c in base_color)
    message = f"Раунд {round_num}"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            col = (mx - MARGIN) // CELL
            row = (my - MARGIN) // CELL
            if 0 <= col < GRID and 0 <= row < GRID:
                if (col, row) == odd_cell:
                    next_round()
                else:
                    message = "Не тот — попробуйте снова"

    screen.fill((24, 28, 36))
    for row in range(GRID):
        for col in range(GRID):
            color = odd_color if (col, row) == odd_cell else base_color
            rect = pygame.Rect(MARGIN + col * CELL + 4, MARGIN + row * CELL + 4, CELL - 8, CELL - 8)
            pygame.draw.rect(screen, color, rect, border_radius=8)
    screen.blit(font.render(message, True, (240, 240, 250)), (MARGIN, 8))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
