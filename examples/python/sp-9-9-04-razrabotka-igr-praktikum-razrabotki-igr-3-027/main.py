import pygame
import settings as S
from game.court import draw_court, field_rect
from game.paddle import Paddle
from game.ball import Ball
from game.hud import draw_score, draw_menu, draw_paused, draw_win
from game.ai import ai_follow_ball


class Game:
    def __init__(self, vs_ai=True):
        self.vs_ai = vs_ai
        self.field = field_rect()
        self.state = "MENU"
        self.score_left = 0
        self.score_right = 0
        self.serve_direction = 1
        self.winner = ""

        self.paddle_left = Paddle(S.MARGIN + 8, S.COLOR_PADDLE_LEFT)
        self.paddle_right = Paddle(
            S.MARGIN + S.FIELD_W - S.PADDLE_W - 8,
            S.COLOR_PADDLE_RIGHT,
        )
        self.ball = Ball()

    def reset_match(self):
        self.score_left = 0
        self.score_right = 0
        self.serve_direction = 1
        self.winner = ""
        self.ball.reset(center=True)
        self.state = "MENU"

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return True

        if event.key == pygame.K_ESCAPE:
            return False

        if event.key == pygame.K_p and self.state in ("PLAYING", "PAUSED", "SERVE"):
            self.state = "PAUSED" if self.state == "PLAYING" else "PLAYING"
        elif event.key == pygame.K_r and self.state == "WIN":
            self.reset_match()
        elif event.key == pygame.K_SPACE:
            if self.state == "MENU":
                self.reset_match()
                self.state = "SERVE"
            elif self.state == "SERVE":
                self.ball.reset(center=False, direction=self.serve_direction)
                self.state = "PLAYING"
        return True

    def update(self, dt):
        if self.state not in ("PLAYING", "SERVE"):
            return

        keys = pygame.key.get_pressed()
        dir_left = keys[pygame.K_s] - keys[pygame.K_w]
        self.paddle_left.move(dir_left, dt)

        if self.vs_ai:
            if self.state == "PLAYING" and self.ball.vx > 0:
                ai_follow_ball(self.paddle_right, self.ball, dt, 0.82)
        else:
            dir_right = keys[pygame.K_DOWN] - keys[pygame.K_UP]
            self.paddle_right.move(dir_right, dt)

        if self.state != "PLAYING":
            return

        self.ball.update(dt, self.field)
        self.ball.collide_paddle(self.paddle_left)
        self.ball.collide_paddle(self.paddle_right)

        if self.ball.rect.right < self.field.left:
            self.score_right += 1
            self.serve_direction = -1
            self.ball.reset(center=True)
            self.state = "SERVE"
        elif self.ball.rect.left > self.field.right:
            self.score_left += 1
            self.serve_direction = 1
            self.ball.reset(center=True)
            self.state = "SERVE"

        if self.score_left >= S.WIN_SCORE:
            self.state = "WIN"
            self.winner = "Игрок 1"
        elif self.score_right >= S.WIN_SCORE:
            self.state = "WIN"
            self.winner = "Игрок 2" if not self.vs_ai else "Компьютер"

    def draw(self, surface):
        draw_court(surface)
        self.paddle_left.draw(surface)
        self.paddle_right.draw(surface)
        if self.state in ("PLAYING", "SERVE", "PAUSED", "WIN"):
            self.ball.draw(surface)
        draw_score(surface, self.score_left, self.score_right)

        if self.state == "MENU":
            draw_menu(surface)
        elif self.state == "PAUSED":
            draw_paused(surface)
        elif self.state == "WIN":
            draw_win(surface, self.winner)
        elif self.state == "SERVE":
            font = pygame.font.SysFont("consolas", 22)
            hint = font.render("Пробел — подача", True, S.COLOR_ACCENT)
            surface.blit(hint, hint.get_rect(center=(S.SCREEN_W // 2, S.SCREEN_H - 24)))
