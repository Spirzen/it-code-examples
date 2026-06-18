"""Корабль игрока."""

import pygame

import settings as S


class Player:
    def __init__(self) -> None:
        self.rect = pygame.Rect(S.WIDTH // 2 - 24, S.PLAYER_Y, 48, 20)

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= S.PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += S.PLAYER_SPEED
        self.rect.x = max(8, min(S.WIDTH - self.rect.w - 8, self.rect.x))

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, S.PLAYER_COLOR, self.rect, border_radius=4)
