"""Оркестратор матча Space Invaders."""

from __future__ import annotations

import sys

import pygame

import settings as S
from game.alien_wave import AlienWave
from game.bullets import BulletManager
from game.player import Player
from game.ufo import Ufo


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((S.WIDTH, S.HEIGHT))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 24)
        self.reset()

    def reset(self) -> None:
        self.player = Player()
        self.bullets = BulletManager()
        self.wave = AlienWave()
        self.ufo = Ufo()
        self.last_ufo = pygame.time.get_ticks()
        self.score = 0
        self.lives = S.PLAYER_LIVES
        self.game_over = False
        self.won = False

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_r and (self.game_over or self.won):
                    self.reset()
                if event.key == pygame.K_SPACE and not self.game_over and not self.won:
                    self.bullets.fire(self.player.rect)
        return True

    def update(self) -> None:
        if self.game_over or self.won:
            return
        self.player.update()
        self.bullets.update()
        self.wave.update()
        self.bullets.hit_aliens(self.wave, self.add_score)
        self.bombs_hit = self.wave.drop_bombs()
        for bomb in self.bombs_hit:
            if bomb.colliderect(self.player.rect):
                self.lives -= 1
                self.wave.remove_bomb(bomb)
                if self.lives <= 0:
                    self.game_over = True
        now = pygame.time.get_ticks()
        if not self.ufo.active and now - self.last_ufo >= S.UFO_INTERVAL_MS:
            self.ufo.spawn(S.WIDTH - 40)
            self.last_ufo = now
        self.ufo.update()
        self.bullets.hit_ufo(self.ufo, self.add_score)
        if self.wave.cleared():
            self.won = True
        elif self.wave.reached_player(self.player.rect):
            self.game_over = True

    def add_score(self, points: int) -> None:
        self.score += points

    def draw(self) -> None:
        self.screen.fill(S.BG)
        self.wave.draw(self.screen)
        self.player.draw(self.screen)
        self.bullets.draw(self.screen)
        self.ufo.draw(self.screen)
        self.screen.blit(self.font.render(f"Счёт: {self.score}", True, S.TEXT), (12, 12))
        self.screen.blit(self.font.render(f"Жизни: {self.lives}", True, S.TEXT), (12, 40))
        if self.won:
            msg = self.font.render("Победа! R — заново", True, (120, 255, 160))
            self.screen.blit(msg, msg.get_rect(center=(S.WIDTH // 2, S.HEIGHT // 2)))
        elif self.game_over:
            msg = self.font.render("Поражение — R", True, (255, 120, 120))
            self.screen.blit(msg, msg.get_rect(center=(S.WIDTH // 2, S.HEIGHT // 2)))

    def run(self) -> None:
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(S.FPS)
        pygame.quit()
        sys.exit()
