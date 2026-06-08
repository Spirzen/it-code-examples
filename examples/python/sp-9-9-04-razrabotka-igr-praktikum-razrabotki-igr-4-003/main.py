import sys
import pygame
import config as C

pygame.init()
screen = pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))
pygame.display.set_caption("Racing — этап 1")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill(C.COLOR_GRASS)
    pygame.display.flip()
    clock.tick(C.FPS)

pygame.quit()
sys.exit()
