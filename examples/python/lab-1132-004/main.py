#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
W, H = 720, 520
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Click targets")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)  # системный шрифт, размер 32

def new_target():
    r = random.randint(18, 32)
    x = random.randint(r, W - r)
    y = random.randint(r, H - r)
    return pygame.Rect(x - r, y - r, r * 2, r * 2)  # круг как bounding box

target = new_target()
score = 0
misses = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if target.collidepoint(event.pos):  # клик внутри Rect?
                score += 1
                target = new_target()
            else:
                misses += 1

    screen.fill((24, 28, 36))
    pygame.draw.ellipse(screen, (240, 90, 90), target)
    label = font.render(f"Счёт: {score}  Мимо: {misses}", True, (230, 230, 240))
    screen.blit(label, (16, 16))  # текст в левый верхний угол
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
