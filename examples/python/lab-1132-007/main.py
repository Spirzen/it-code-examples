#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
CELL = 24                    # размер одной клетки в пикселях
COLS, ROWS = 24, 18          # поле в клетках
W, H = COLS * CELL, ROWS * CELL
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

snake = [(COLS // 2, ROWS // 2)]  # голова — элемент [0]
direction = (1, 0)               # (dx, dy): вправо
food = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
score = 0
tick_ms = 120                    # интервал хода, мс
last_move = 0
game_over = False

def place_food():
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos

running = True
while running:
    now = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if game_over and event.key == pygame.K_SPACE:
                snake = [(COLS // 2, ROWS // 2)]
                direction = (1, 0)
                food = place_food()
                score = 0
                game_over = False
                last_move = now
            if not game_over:
                # запрет разворота на 180°: нельзя (1,0) → (-1,0) в один ход
                if event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    direction = (0, 1)

    if not game_over and now - last_move >= tick_ms:
        last_move = now
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)
        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            game_over = True
        elif new_head in snake:
            game_over = True
        else:
            snake.insert(0, new_head)   # новая голова
            if new_head == food:
                score += 1
                food = place_food()
                tick_ms = max(60, tick_ms - 4)  # ускорение
            else:
                snake.pop()             # убрать хвост — длина та же

    screen.fill((16, 20, 28))
    for i, (cx, cy) in enumerate(snake):
        color = (90, 220, 140) if i == 0 else (50, 160, 100)
        pygame.draw.rect(screen, color, (cx * CELL, cy * CELL, CELL - 2, CELL - 2), border_radius=4)
    fx, fy = food
    pygame.draw.rect(screen, (240, 90, 90), (fx * CELL, fy * CELL, CELL - 2, CELL - 2), border_radius=6)
    hud = font.render(f"Счёт: {score}", True, (230, 230, 240))
    screen.blit(hud, (8, 8))
    if game_over:
        msg = font.render("Game Over — пробел", True, (255, 120, 120))
        screen.blit(msg, msg.get_rect(center=(W // 2, H // 2)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
