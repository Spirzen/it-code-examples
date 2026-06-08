import sys
import pygame
import settings as S
from game.game import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode((S.SCREEN_W, S.SCREEN_H))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    game = Game(vs_ai=True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if not game.handle_event(event):
                    running = False

        dt = clock.tick(S.FPS) / 1000.0
        game.update(dt)

        screen.fill(S.COLOR_BG)
        game.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
