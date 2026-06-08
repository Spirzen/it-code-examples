#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
W, H = 640, 480
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Catch")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

player = pygame.Rect(W // 2 - 40, H - 50, 80, 16)
items = []
score = 0
missed = 0
spawn = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 7
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 7
    player.x = max(0, min(W - player.w, player.x))

    spawn += 1
    if spawn > 25:
        spawn = 0
        items.append(pygame.Rect(random.randint(10, W - 20), -20, 16, 16))

    for item in items[:]:
        item.y += 5
        if item.colliderect(player):
            items.remove(item)
            score += 1
        elif item.top > H:
            items.remove(item)
            missed += 1

    screen.fill((20, 26, 40))
    pygame.draw.rect(screen, (100, 200, 255), player, border_radius=4)
    for item in items:
        pygame.draw.circle(screen, (255, 220, 80), item.center, 8)
    screen.blit(font.render(f"Поймано: {score}  Упущено: {missed}", True, (240, 240, 250)), (12, 12))
    if missed >= 10:
        over = font.render("10 промахов — Esc", True, (255, 100, 100))
        screen.blit(over, over.get_rect(center=(W // 2, H // 2)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
