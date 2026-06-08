#!/usr/bin/env python3

import pygame
import random
import sys

pygame.init()
W, H = 480, 640
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flappy")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

GRAVITY = 0.45
JUMP = -8.5
GAP = 170
PIPE_W = 70
SPEED = 4

bird_y = H // 2
bird_vy = 0
pipes = []
score = 0
spawn_timer = 0
game_over = False

def spawn_pipe():
    gap_y = random.randint(120, H - GAP - 120)
    return {"x": W + 20, "gap_y": gap_y, "scored": False}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    bird_y = H // 2
                    bird_vy = 0
                    pipes.clear()
                    score = 0
                    spawn_timer = 0
                    game_over = False
                else:
                    bird_vy = JUMP

    if not game_over:
        bird_vy += GRAVITY
        bird_y += bird_vy
        spawn_timer += 1
        if spawn_timer > 55:
            spawn_timer = 0
            pipes.append(spawn_pipe())

        bird_rect = pygame.Rect(80, int(bird_y) - 14, 28, 28)
        for pipe in pipes[:]:
            pipe["x"] -= SPEED
            top = pygame.Rect(pipe["x"], 0, PIPE_W, pipe["gap_y"])
            bottom = pygame.Rect(pipe["x"], pipe["gap_y"] + GAP, PIPE_W, H)
            if pipe["x"] + PIPE_W < 0:
                pipes.remove(pipe)
                continue
            if not pipe["scored"] and pipe["x"] + PIPE_W < 80:
                pipe["scored"] = True
                score += 1
            if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
                game_over = True
        if bird_y < 0 or bird_y > H:
            game_over = True

    screen.fill((120, 200, 240))
    for pipe in pipes:
        pygame.draw.rect(screen, (40, 160, 70), (pipe["x"], 0, PIPE_W, pipe["gap_y"]))
        pygame.draw.rect(screen, (40, 160, 70), (pipe["x"], pipe["gap_y"] + GAP, PIPE_W, H - pipe["gap_y"] - GAP))
    pygame.draw.circle(screen, (255, 220, 60), (94, int(bird_y)), 16)
    screen.blit(font.render(f"{score}", True, (255, 255, 255)), (W // 2 - 10, 40))
    if game_over:
        screen.blit(font.render("Пробел — заново", True, (30, 30, 40)), (W // 2 - 110, H // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
