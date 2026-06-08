#!/usr/bin/env python3

import pygame
import sys

pygame.init()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bounce")
clock = pygame.time.Clock()

x, y = W // 2, H // 2      # центр шара
vx, vy = 4, 3              # пикселей за кадр по X и Y
radius = 24
color = (80, 180, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += vx
    y += vy
    # отражение от левой/правой стены
    if x - radius <= 0 or x + radius >= W:
        vx = -vx
    # отражение от верха/низа
    if y - radius <= 0 or y + radius >= H:
        vy = -vy

    screen.fill((18, 22, 30))
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
