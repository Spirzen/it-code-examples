"""Бонусная летающая тарелка."""

import random

import pygame

import settings as S


class Ufo:
    def __init__(self) -> None:
        self.rect = pygame.Rect(0, 0, 52, 24)
        self.active = False
        self.points = 100
        self.dead = False
        self.death_until = 0

    def spawn(self, x: int) -> None:
        self.active = True
        self.dead = False
        self.points = random.choice([50, 100, 150, 300])
        self.rect.topleft = (x, 48)

    def update(self) -> None:
        if not self.active or self.dead:
            return
        self.rect.x -= S.UFO_SPEED
        if self.rect.right < 0:
            self.active = False
        if self.dead and pygame.time.get_ticks() > self.death_until:
            self.active = False

    def kill(self) -> None:
        self.dead = True
        self.death_until = pygame.time.get_ticks() + 900

    def draw(self, surface: pygame.Surface) -> None:
        if not self.active:
            return
        color = (200, 80, 220) if not self.dead else S.TEXT
        pygame.draw.ellipse(surface, color, self.rect)
