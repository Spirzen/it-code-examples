import sys

import pygame

from core.config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, UI_TEXT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe UI", 28)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((12, 14, 26))
    label = font.render("Этап 1 — config.py подключён", True, UI_TEXT)
    screen.blit(label, label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
