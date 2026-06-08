#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
W, H = 480, 640
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dodge")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

player = pygame.Rect(W // 2 - 18, H - 80, 36, 56)
obstacles = []
score = 0
timer = 0
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_SPACE:
            obstacles.clear()
            score = 0
            timer = 0
            game_over = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= 6
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += 6
        player.x = max(0, min(W - player.w, player.x))

        timer += 1
        if timer % 35 == 0:
            lane = random.choice([60, W // 2 - 20, W - 100])
            obstacles.append(pygame.Rect(lane, -70, 40, 70))

        for obs in obstacles[:]:
            obs.y += 7
            if obs.top > H:
                obstacles.remove(obs)
                score += 1
            elif obs.colliderect(player):
                game_over = True

    screen.fill((40, 44, 52))
    for lane_x in (W // 3, 2 * W // 3):
        pygame.draw.line(screen, (200, 200, 80), (lane_x, 0), (lane_x, H), 2)
    pygame.draw.rect(screen, (80, 180, 255), player, border_radius=6)
    for obs in obstacles:
        pygame.draw.rect(screen, (220, 70, 70), obs, border_radius=4)
    screen.blit(font.render(f"Очки: {score}", True, (240, 240, 250)), (12, 12))
    if game_over:
        screen.blit(font.render("Столкновение — пробел", True, (255, 120, 120)), (80, H // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
