"""Пули игрока."""

from __future__ import annotations

from typing import Callable, List

import pygame

import settings as S


class BulletManager:
    def __init__(self) -> None:
        self.shots: List[pygame.Rect] = []
        self.cooldown = 0

    def fire(self, player: pygame.Rect) -> None:
        if self.cooldown > 0:
            return
        self.shots.append(pygame.Rect(player.centerx - 2, player.top - 14, 4, 12))
        self.cooldown = S.FIRE_COOLDOWN

    def update(self) -> None:
        if self.cooldown > 0:
            self.cooldown -= 1
        for shot in self.shots[:]:
            shot.y -= S.BULLET_SPEED
            if shot.bottom < 0:
                self.shots.remove(shot)

    def draw(self, surface: pygame.Surface) -> None:
        for shot in self.shots:
            pygame.draw.rect(surface, S.BULLET_COLOR, shot)

    def hit_aliens(self, wave, on_kill: Callable[[int], None]) -> None:
        for shot in self.shots[:]:
            alien = wave.hit_test(shot)
            if alien is not None:
                self.shots.remove(shot)
                on_kill(alien.points)
                alien.alive = False

    def hit_ufo(self, ufo, on_kill: Callable[[int], None]) -> None:
        if not ufo.active or ufo.dead:
            return
        for shot in self.shots[:]:
            if shot.colliderect(ufo.rect):
                self.shots.remove(shot)
                on_kill(ufo.points)
                ufo.kill()
                break
