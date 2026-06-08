#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Reaction")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

WAIT = "wait"
READY = "ready"
GO = "go"
DONE = "done"

state = WAIT
message = "Пробел — новая попытка"
start_ms = 0
react_ms = None
best_ms = None

running = True
while running:
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and state in (WAIT, DONE):
                state = READY
                start_ms = now + random.randint(1200, 3500)
                react_ms = None
                message = "Ждите зелёный.."
            elif event.key == pygame.K_SPACE and state == GO:
                react_ms = now - start_ms
                state = DONE
                if best_ms is None or react_ms < best_ms:
                    best_ms = react_ms
                message = f"Ваша реакция: {react_ms} мс"
            elif state == READY:
                state = DONE
                message = "Рано! Пробел — снова"

    if state == READY and now >= start_ms:
        state = GO
        start_ms = now
        message = "Жми!"

    if state == WAIT:
        color = (60, 70, 90)
    elif state == READY:
        color = (200, 60, 60)
    elif state == GO:
        color = (60, 200, 100)
    else:
        color = (70, 90, 120)

    screen.fill(color)
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=(W // 2, H // 2)))
    if best_ms is not None:
        hint = font.render(f"Лучший: {best_ms} мс", True, (240, 240, 250))
        screen.blit(hint, (20, H - 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
