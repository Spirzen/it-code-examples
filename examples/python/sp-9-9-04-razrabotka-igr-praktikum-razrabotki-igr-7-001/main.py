import sys
import pygame

SCREEN_W, SCREEN_H = 1280, 720
FPS = 60
TITLE = "Карточный roguelike — этап 0"

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("segoeui", 28)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((12, 10, 24))
    hint = font.render("Этап 0 — Esc для выхода", True, (220, 210, 240))
    screen.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H // 2 - 14))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
