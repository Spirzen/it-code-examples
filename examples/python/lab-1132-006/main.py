#!/usr/bin/env python3

import pygame
import sys

pygame.init()
W, H = 800, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

PADDLE_W, PADDLE_H = 14, 90
BALL = 14
SPEED = 6

left = pygame.Rect(24, H // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
right = pygame.Rect(W - 24 - PADDLE_W, H // 2 - PADDLE_H // 2, PADDLE_W, PADDLE_H)
ball = pygame.Rect(W // 2 - BALL, H // 2 - BALL, BALL * 2, BALL * 2)
vx, vy = SPEED, SPEED * 0.7
score_l, score_r = 0, 0

def reset_ball(to_left: bool):
    global vx, vy
    ball.center = (W // 2, H // 2)
    vx = SPEED if to_left else -SPEED
    vy = SPEED * 0.5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left.top > 0:
        left.y -= 7
    if keys[pygame.K_s] and left.bottom < H:
        left.y += 7
    if keys[pygame.K_UP] and right.top > 0:
        right.y -= 7
    if keys[pygame.K_DOWN] and right.bottom < H:
        right.y += 7

    ball.x += int(vx)
    ball.y += int(vy)
    if ball.top <= 0 or ball.bottom >= H:
        vy = -vy
    if ball.colliderect(left) and vx < 0:
        vx = -vx
    if ball.colliderect(right) and vx > 0:
        vx = -vx
    if ball.left <= 0:
        score_r += 1
        reset_ball(True)
    if ball.right >= W:
        score_l += 1
        reset_ball(False)

    screen.fill((14, 18, 26))
    pygame.draw.aaline(screen, (50, 60, 80), (W // 2, 0), (W // 2, H))
    pygame.draw.rect(screen, (200, 220, 255), left)
    pygame.draw.rect(screen, (255, 200, 120), right)
    pygame.draw.ellipse(screen, (240, 240, 250), ball)
    hud = font.render(f"{score_l} : {score_r}", True, (220, 220, 230))
    screen.blit(hud, hud.get_rect(center=(W // 2, 36)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
