#!/usr/bin/env python3

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Trail")
clock = pygame.time.Clock()

trail = []       # история координат [(x, y), ..]
MAX_LEN = 40     # сколько точек хранить

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()  # текущие координаты курсора
    trail.append((mx, my))
    if len(trail) > MAX_LEN:
        trail.pop(0)  # убрать самую старую точку

    screen.fill((12, 16, 24))
    for i, (tx, ty) in enumerate(trail):
        size = 6 + i // 3           # хвост толще к «голове»
        shade = 80 + i * 4          # градиент яркости
        pygame.draw.circle(screen, (shade, 140, 220), (tx, ty), size)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
