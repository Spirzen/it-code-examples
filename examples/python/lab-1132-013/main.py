#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
W, H = 640, 560
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Invaders lite")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

player = pygame.Rect(W // 2 - 24, H - 48, 48, 20)
bullets = []
enemies = []
for row in range(4):
    for col in range(8):
        enemies.append(pygame.Rect(60 + col * 64, 50 + row * 40, 40, 28))

enemy_dir = 1
move_down = False
score = 0
cooldown = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and cooldown == 0:
            bullets.append(pygame.Rect(player.centerx - 2, player.top - 12, 4, 12))
            cooldown = 20

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 6
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 6
    player.x = max(0, min(W - player.w, player.x))

    if cooldown > 0:
        cooldown -= 1

    if enemies:
        edge_hit = any(e.left <= 4 or e.right >= W - 4 for e in enemies)
        if edge_hit:
            enemy_dir *= -1
            move_down = True
        for e in enemies:
            e.x += 3 * enemy_dir
            if move_down:
                e.y += 16
        move_down = False

    for b in bullets[:]:
        b.y -= 10
        if b.bottom < 0:
            bullets.remove(b)
            continue
        for e in enemies[:]:
            if b.colliderect(e):
                bullets.remove(b)
                enemies.remove(e)
                score += 10
                break

    if not enemies:
        for row in range(4):
            for col in range(8):
                enemies.append(pygame.Rect(60 + col * 64, 50 + row * 40, 40, 28))

    screen.fill((8, 10, 24))
    for e in enemies:
        pygame.draw.rect(screen, (180, 90, 220), e, border_radius=4)
    pygame.draw.rect(screen, (120, 220, 255), player, border_radius=4)
    for b in bullets:
        pygame.draw.rect(screen, (255, 240, 100), b)
    screen.blit(font.render(f"Счёт: {score}", True, (230, 230, 240)), (12, 12))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
