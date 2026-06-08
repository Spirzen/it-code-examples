import random
import pygame
import settings as S
from game.board import (
    new_board, can_place, lock_piece, clear_lines,
    draw_board, draw_locked_blocks, draw_ghost,
)
from game.piece import Piece, spawn_piece, random_kind
from game.hud import draw_sidebar, draw_hud, draw_next_preview, draw_overlay
from game.tetrominoes import gravity_interval, LINE_SCORES


class Game:
    def __init__(self):
        self.state = "MENU"
        self.board = new_board()
        self.score = 0
        self.lines_total = 0
        self.level = 0
        self.gravity_timer = 0.0
        self.next_kind = random_kind()
        self.active = spawn_piece(self.next_kind)
        self.next_kind = random_kind()

    def reset_play(self):
        self.board = new_board()
        self.score = 0
        self.lines_total = 0
        self.level = 0
        self.gravity_timer = 0.0
        self.next_kind = random_kind()
        self.active = spawn_piece(self.next_kind)
        self.next_kind = random_kind()
        self.state = "PLAYING"

    def _spawn_after_lock(self):
        self.active = spawn_piece(self.next_kind)
        self.next_kind = random_kind()
        if not can_place(self.board, self.active.cells, self.active.x, self.active.y):
            self.state = "GAME_OVER"

    def _apply_line_score(self, cleared):
        if not cleared:
            return
        self.lines_total += cleared
        self.score += LINE_SCORES.get(cleared, 0) * (self.level + 1)
        self.level = self.lines_total // S.LINES_PER_LEVEL

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return True

        if event.key == pygame.K_ESCAPE:
            return False

        if self.state == "MENU" and event.key == pygame.K_SPACE:
            self.reset_play()
        elif self.state == "PLAYING":
            if event.key == pygame.K_p:
                self.state = "PAUSED"
            elif event.key == pygame.K_LEFT:
                self.active.try_move(self.board, -1, 0)
            elif event.key == pygame.K_RIGHT:
                self.active.try_move(self.board, 1, 0)
            elif event.key in (pygame.K_UP, pygame.K_x):
                self.active.try_rotate(self.board, 1)
            elif event.key == pygame.K_z:
                self.active.try_rotate(self.board, -1)
            elif event.key == pygame.K_SPACE:
                steps = self.active.hard_drop(self.board)
                self.score += steps * S.HARD_DROP_BONUS
                lock_piece(self.board, self.active)
                self._apply_line_score(clear_lines(self.board))
                self._spawn_after_lock()
        elif self.state == "PAUSED" and event.key == pygame.K_p:
            self.state = "PLAYING"
        elif self.state == "GAME_OVER" and event.key == pygame.K_r:
            self.state = "MENU"

        return True

    def update(self, dt):
        if self.state != "PLAYING":
            return

        keys = pygame.key.get_pressed()
        soft_drop = keys[pygame.K_DOWN]
        self.gravity_timer += dt

        if soft_drop:
            if self.gravity_timer >= 0.05:
                self.gravity_timer = 0.0
                if self.active.try_move(self.board, 0, 1):
                    self.score += S.SOFT_DROP_BONUS
                else:
                    lock_piece(self.board, self.active)
                    self._apply_line_score(clear_lines(self.board))
                    self._spawn_after_lock()
        else:
            interval = gravity_interval(self.level)
            if self.gravity_timer >= interval:
                self.gravity_timer = 0.0
                if not self.active.try_move(self.board, 0, 1):
                    lock_piece(self.board, self.active)
                    self._apply_line_score(clear_lines(self.board))
                    self._spawn_after_lock()

    def draw(self, surface):
        draw_board(surface)
        draw_sidebar(surface)
        draw_locked_blocks(surface, self.board)

        if self.state == "PLAYING":
            draw_ghost(surface, self.active, self.board)
            self.active.draw(surface)
            draw_next_preview(surface, self.next_kind)
            draw_hud(surface, self.score, self.lines_total, self.level)
        elif self.state == "MENU":
            draw_overlay(surface, "TETRIS", "Пробел — начать")
        elif self.state == "PAUSED":
            draw_ghost(surface, self.active, self.board)
            self.active.draw(surface)
            draw_next_preview(surface, self.next_kind)
            draw_hud(surface, self.score, self.lines_total, self.level)
            draw_overlay(surface, "ПАУЗА", "P — продолжить")
        elif self.state == "GAME_OVER":
            draw_hud(surface, self.score, self.lines_total, self.level)
            draw_overlay(surface, "GAME OVER", f"Score: {self.score}  ·  R — в меню")
