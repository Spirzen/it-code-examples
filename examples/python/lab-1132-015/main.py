#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Survive 30s")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

player = pygame.Rect(W // 2 - 16, H // 2 - 16, 32, 32)
hazards = []
start = pygame.time.get_ticks()
won = False
lost = False

running = True
while running:
    elapsed = (pygame.time.get_ticks() - start) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (won or lost) and event.key == pygame.K_SPACE:
            start = pygame.time.get_ticks()
            hazards.clear()
            won = lost = False

    if not won and not lost:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += 5
        player.clamp_ip(screen.get_rect())

        if random.random() < 0.04:
            hazards.append(pygame.Rect(random.randint(0, W - 24), 0, 24, 24))

        for h in hazards[:]:
            h.y += 6
            if h.top > H:
                hazards.remove(h)
            elif h.colliderect(player):
                lost = True
        if elapsed >= 30:
            won = True

    screen.fill((18, 22, 30))
    for h in hazards:
        pygame.draw.rect(screen, (220, 80, 80), h, border_radius=4)
    pygame.draw.rect(screen, (100, 200, 255), player, border_radius=6)
    left = max(0, 30 - elapsed)
    screen.blit(font.render(f"Осталось: {left:.1f} с", True, (230, 230, 240)), (16, 16))
    if won:
        screen.blit(font.render("Выжили! Пробел", True, (120, 255, 160)), (180, H // 2))
    if lost:
        screen.blit(font.render("Попали — пробел", True, (255, 120, 120)), (170, H // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
