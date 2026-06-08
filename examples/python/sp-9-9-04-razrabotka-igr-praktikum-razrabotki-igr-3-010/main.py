import sys
import pygame
import settings as S
from game.court import draw_court
from game.paddle import Paddle
from game.ball import Ball

pygame.init()
screen = pygame.display.set_mode((S.SCREEN_W, S.SCREEN_H))
pygame.display.set_caption("Ping Pong — этап 6")
clock = pygame.time.Clock()

paddle_left = Paddle(S.MARGIN + 8, S.COLOR_PADDLE_LEFT)
paddle_right = Paddle(
    S.MARGIN + S.FIELD_W - S.PADDLE_W - 8,
    S.COLOR_PADDLE_RIGHT,
)
ball = Ball()
ball.reset(center=False, direction=1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    dt = clock.tick(S.FPS) / 1000.0

    keys = pygame.key.get_pressed()
    direction = 0
    if keys[pygame.K_w]:
        direction -= 1
    if keys[pygame.K_s]:
        direction += 1
    paddle_left.move(direction, dt)

    ball.update(dt)

    screen.fill(S.COLOR_BG)
    draw_court(screen)
    paddle_left.draw(screen)
    paddle_right.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
