"""Стая пришельцев, бомбы и движение."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Optional

import pygame

import settings as S


@dataclass
class Alien:
    row: int
    rect: pygame.Rect
    points: int
    color: tuple[int, int, int]
    alive: bool = True


class AlienWave:
    def __init__(self) -> None:
        self.aliens: List[Alien] = []
        self.direction = 1
        self.bombs: List[pygame.Rect] = []
        self.bomb_cd = 120
        self._spawn_grid()

    def _spawn_grid(self) -> None:
        self.aliens.clear()
        for row in range(S.ALIEN_ROWS):
            y = S.ALIEN_TOP + row * (S.ALIEN_H + S.ALIEN_GAP_Y)
            row_width = S.ALIEN_COLS * S.ALIEN_W + (S.ALIEN_COLS - 1) * S.ALIEN_GAP_X
            start_x = (S.WIDTH - row_width) // 2
            for col in range(S.ALIEN_COLS):
                x = start_x + col * (S.ALIEN_W + S.ALIEN_GAP_X)
                self.aliens.append(
                    Alien(
                        row=row,
                        rect=pygame.Rect(x, y, S.ALIEN_W, S.ALIEN_H),
                        points=S.ROW_POINTS[row],
                        color=S.ROW_COLORS[row],
                    )
                )

    def living(self) -> List[Alien]:
        return [a for a in self.aliens if a.alive]

    def speed(self) -> int:
        left = len(self.living())
        return S.ALIEN_H_SPEED + max(0, (S.ALIEN_ROWS * S.ALIEN_COLS - left) // 8)

    def update(self) -> None:
        alive = self.living()
        if not alive:
            return
        edge = any(a.rect.left <= 8 or a.rect.right >= S.WIDTH - 8 for a in alive)
        drop = False
        if edge:
            self.direction *= -1
            drop = True
        spd = self.speed()
        for a in alive:
            a.rect.x += spd * self.direction
            if drop:
                a.rect.y += S.ALIEN_DROP
        self.bomb_cd -= 1
        if self.bomb_cd <= 0:
            bottom_row = max(a.row for a in alive)
            shooters = [a for a in alive if a.row == bottom_row]
            shooter = random.choice(shooters)
            self.bombs.append(pygame.Rect(shooter.rect.centerx - 3, shooter.rect.bottom, 6, 14))
            self.bomb_cd = random.randint(90, 180)
        for bomb in self.bombs[:]:
            bomb.y += S.BOMB_SPEED
            if bomb.top > S.HEIGHT:
                self.bombs.remove(bomb)

    def drop_bombs(self) -> List[pygame.Rect]:
        return list(self.bombs)

    def remove_bomb(self, bomb: pygame.Rect) -> None:
        if bomb in self.bombs:
            self.bombs.remove(bomb)

    def hit_test(self, rect: pygame.Rect) -> Optional[Alien]:
        for alien in self.living():
            if rect.colliderect(alien.rect):
                return alien
        return None

    def cleared(self) -> bool:
        return len(self.living()) == 0

    def reached_player(self, player: pygame.Rect) -> bool:
        alive = self.living()
        if not alive:
            return False
        return max(a.rect.bottom for a in alive) >= player.top - 8

    def draw(self, surface: pygame.Surface) -> None:
        for alien in self.living():
            pygame.draw.rect(surface, alien.color, alien.rect, border_radius=4)
        for bomb in self.bombs:
            pygame.draw.rect(surface, S.BOMB_COLOR, bomb, border_radius=2)
