#!/usr/bin/env python3

import pygame
import sys

pygame.init()
W, H = 720, 520
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

paddle = pygame.Rect(W // 2 - 60, H - 36, 120, 14)
ball = pygame.Rect(W // 2, H - 60, 16, 16)
vx, vy = 5, -5

BRICK_ROWS, BRICK_COLS = 5, 10
brick_w = W // BRICK_COLS - 4
brick_h = 22
bricks = []
colors = [(220, 80, 80), (220, 160, 60), (220, 220, 80), (80, 200, 120), (80, 160, 220)]
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        rect = pygame.Rect(2 + col * (brick_w + 4), 40 + row * (brick_h + 4), brick_w, brick_h)
        bricks.append({"rect": rect, "color": colors[row], "alive": True})

lives = 3
won = False
lost = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (won or lost) and event.key == pygame.K_SPACE:
            bricks = []
            for row in range(BRICK_ROWS):
                for col in range(BRICK_COLS):
                    rect = pygame.Rect(2 + col * (brick_w + 4), 40 + row * (brick_h + 4), brick_w, brick_h)
                    bricks.append({"rect": rect, "color": colors[row], "alive": True})
            ball.center = (W // 2, H - 60)
            vx, vy = 5, -5
            lives = 3
            won = lost = False

    if not won and not lost:
        mx, _ = pygame.mouse.get_pos()
        paddle.centerx = max(paddle.w // 2, min(W - paddle.w // 2, mx))
        ball.x += vx
        ball.y += vy
        if ball.left <= 0 or ball.right >= W:
            vx = -vx
        if ball.top <= 0:
            vy = -vy
        if ball.colliderect(paddle) and vy > 0:
            vy = -abs(vy)
            offset = (ball.centerx - paddle.centerx) / (paddle.w / 2)
            vx = int(6 * offset)
        if ball.bottom >= H:
            lives -= 1
            ball.center = (W // 2, H - 60)
            vx, vy = 5, -5
            if lives <= 0:
                lost = True
        for brick in bricks:
            if brick["alive"] and ball.colliderect(brick["rect"]):
                brick["alive"] = False
                vy = -vy
                break
        if all(not b["alive"] for b in bricks):
            won = True

    screen.fill((18, 22, 32))
    for brick in bricks:
        if brick["alive"]:
            pygame.draw.rect(screen, brick["color"], brick["rect"], border_radius=4)
    pygame.draw.rect(screen, (200, 210, 240), paddle, border_radius=6)
    pygame.draw.ellipse(screen, (255, 240, 120), ball)
    screen.blit(font.render(f"Жизни: {lives}", True, (230, 230, 240)), (12, 8))
    if won:
        screen.blit(font.render("Победа! Пробел", True, (120, 255, 160)), (W // 2 - 90, H // 2))
    if lost:
        screen.blit(font.render("Поражение. Пробел", True, (255, 120, 120)), (W // 2 - 110, H // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
