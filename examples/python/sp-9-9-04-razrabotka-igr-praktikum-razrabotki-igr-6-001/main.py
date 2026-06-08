import sys
import pygame

pygame.init()

SCREEN_W, SCREEN_H = 1280, 720
FPS = 60

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Pythonablo — этап 0")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((12, 14, 26))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
