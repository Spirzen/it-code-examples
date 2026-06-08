import sys
import pygame
import settings as S

pygame.init()
screen = pygame.display.set_mode((S.SCREEN_W, S.SCREEN_H))
pygame.display.set_caption("Ping Pong — этап 1")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill(S.COLOR_BG)
    pygame.display.flip()
    dt = clock.tick(S.FPS) / 1000.0

pygame.quit()
sys.exit()
