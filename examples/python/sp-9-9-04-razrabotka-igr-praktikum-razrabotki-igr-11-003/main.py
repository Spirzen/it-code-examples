#!/usr/bin/env python3
"""Space Invaders — учебная версия на Pygame (примитивы, без внешних картинок)."""

from __future__ import annotations

import random
import sys
from typing import List, Optional, Tuple

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 720
FPS = 60
PLAYER_Y = HEIGHT - 56
PLAYER_SPEED = 7
BULLET_SPEED = 12
BOMB_SPEED = 5
FIRE_COOLDOWN = 18
ALIEN_ROWS = 5
ALIEN_COLS = 11
ALIEN_W, ALIEN_H = 40, 28
ALIEN_GAP_X, ALIEN_GAP_Y = 14, 12
ALIEN_TOP = 72
ALIEN_H_SPEED = 3
ALIEN_DROP = 22
PLAYER_LIVES = 3
UFO_INTERVAL_MS = 20_000
UFO_SPEED = 4
ROW_POINTS = [30, 20, 20, 10, 10]
ROW_COLORS = [
    (220, 100, 100),
    (220, 160, 80),
    (180, 120, 220),
    (120, 200, 140),
    (120, 200, 140),
]
BG = (8, 10, 24)
PLAYER_COLOR = (120, 220, 255)
BULLET_COLOR = (255, 240, 100)
BOMB_COLOR = (255, 90, 90)
TEXT = (230, 230, 240)


class Alien:
    __slots__ = ("rect", "row", "points", "color", "alive")

    def __init__(self, row: int, col: int, x: int, y: int) -> None:
        self.row = row
        self.points = ROW_POINTS[row]
        self.color = ROW_COLORS[row]
        self.rect = pygame.Rect(x, y, ALIEN_W, ALIEN_H)
        self.alive = True


class UFO:
    __slots__ = ("rect", "active", "points", "speed", "dead", "death_until")

    def __init__(self) -> None:
        self.rect = pygame.Rect(0, 0, 52, 24)
        self.active = False
        self.points = 100
        self.speed = UFO_SPEED
        self.dead = False
        self.death_until = 0

    def spawn(self, right_x: int) -> None:
        self.active = True
        self.dead = False
        self.points = random.choice([50, 100, 150, 300])
        self.rect.topleft = (right_x, 48)

    def update(self) -> None:
        if not self.active or self.dead:
            return
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.active = False


def create_aliens() -> List[Alien]:
    aliens: List[Alien] = []
    for row in range(ALIEN_ROWS):
        y = ALIEN_TOP + row * (ALIEN_H + ALIEN_GAP_Y)
        row_width = ALIEN_COLS * ALIEN_W + (ALIEN_COLS - 1) * ALIEN_GAP_X
        start_x = (WIDTH - row_width) // 2
        for col in range(ALIEN_COLS):
            x = start_x + col * (ALIEN_W + ALIEN_GAP_X)
            aliens.append(Alien(row, col, x, y))
    return aliens


def living_aliens(aliens: List[Alien]) -> List[Alien]:
    return [a for a in aliens if a.alive]


def alien_speed(remaining: int) -> int:
    if remaining <= 0:
        return ALIEN_H_SPEED
    return ALIEN_H_SPEED + max(0, (ALIEN_ROWS * ALIEN_COLS - remaining) // 8)


def move_aliens(aliens: List[Alien], direction: int) -> Tuple[int, bool]:
    alive = living_aliens(aliens)
    if not alive:
        return direction, False
    edge = any(
        a.rect.left <= 8 or a.rect.right >= WIDTH - 8 for a in alive
    )
    drop = False
    if edge:
        direction *= -1
        drop = True
    speed = alien_speed(len(alive))
    for a in alive:
        a.rect.x += speed * direction
        if drop:
            a.rect.y += ALIEN_DROP
    return direction, drop


def main() -> None:
    stage = 2
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 24)

    player = pygame.Rect(WIDTH // 2 - 24, PLAYER_Y, 48, 20)
    bullets: List[pygame.Rect] = []
    bombs: List[pygame.Rect] = []
    aliens = create_aliens() if stage >= 3 else []
    alien_dir = 1
    score = 0
    lives = PLAYER_LIVES
    fire_cd = 0
    bomb_cd = 120
    ufo = UFO()
    last_ufo = pygame.time.get_ticks()
    game_over = False
    won = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if stage >= 8 and event.key == pygame.K_r and (game_over or won):
                    aliens = create_aliens()
                    bullets.clear()
                    bombs.clear()
                    score = 0
                    lives = PLAYER_LIVES
                    alien_dir = 1
                    game_over = False
                    won = False
                    ufo = UFO()
                    last_ufo = pygame.time.get_ticks()
                if stage >= 2 and event.key == pygame.K_SPACE and fire_cd == 0 and not game_over and not won:
                    bullets.append(pygame.Rect(player.centerx - 2, player.top - 14, 4, 12))
                    fire_cd = FIRE_COOLDOWN

        if not game_over and not won:
            keys = pygame.key.get_pressed()
            if stage >= 1:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    player.x -= PLAYER_SPEED
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    player.x += PLAYER_SPEED
                player.x = max(8, min(WIDTH - player.w - 8, player.x))

            if fire_cd > 0:
                fire_cd -= 1

            if stage >= 4 and aliens:
                alien_dir, _ = move_aliens(aliens, alien_dir)

            if stage >= 2:
                for b in bullets[:]:
                    b.y -= BULLET_SPEED
                    if b.bottom < 0:
                        bullets.remove(b)

            if stage >= 5:
                for b in bullets[:]:
                    for a in aliens:
                        if a.alive and b.colliderect(a.rect):
                            if b in bullets:
                                bullets.remove(b)
                            a.alive = False
                            score += a.points
                            break

            if stage >= 6 and aliens and living_aliens(aliens):
                bomb_cd -= 1
                if bomb_cd <= 0:
                    bottom = [a for a in living_aliens(aliens) if a.row == max(x.row for x in living_aliens(aliens))]
                    shooter = random.choice(bottom)
                    bombs.append(pygame.Rect(shooter.rect.centerx - 3, shooter.rect.bottom, 6, 14))
                    bomb_cd = random.randint(90, 180)

                for bomb in bombs[:]:
                    bomb.y += BOMB_SPEED
                    if bomb.top > HEIGHT:
                        bombs.remove(bomb)
                        continue
                    if bomb.colliderect(player):
                        bombs.remove(bomb)
                        lives -= 1
                        if lives <= 0:
                            game_over = True

            if stage >= 7:
                now = pygame.time.get_ticks()
                if not ufo.active and now - last_ufo >= UFO_INTERVAL_MS:
                    ufo.spawn(WIDTH - 40)
                    last_ufo = now
                ufo.update()
                if ufo.active and not ufo.dead:
                    for b in bullets[:]:
                        if b.colliderect(ufo.rect):
                            bullets.remove(b)
                            ufo.dead = True
                            ufo.death_until = now + 900
                            score += ufo.points
                            break

            if stage >= 8:
                if living_aliens(aliens) == []:
                    won = True
                if living_aliens(aliens):
                    lowest = max(a.rect.bottom for a in living_aliens(aliens))
                    if lowest >= PLAYER_Y - 8:
                        game_over = True

        screen.fill(BG)
        if stage >= 3:
            for a in aliens:
                if a.alive:
                    pygame.draw.rect(screen, a.color, a.rect, border_radius=4)
        if stage >= 1:
            pygame.draw.rect(screen, PLAYER_COLOR, player, border_radius=4)
            for b in bullets:
                pygame.draw.rect(screen, BULLET_COLOR, b)
        if stage >= 6:
            for bomb in bombs:
                pygame.draw.rect(screen, BOMB_COLOR, bomb, border_radius=2)
        if stage >= 7 and ufo.active:
            color = (200, 80, 220) if not ufo.dead else TEXT
            pygame.draw.ellipse(screen, color, ufo.rect)
            if ufo.dead and pygame.time.get_ticks() > ufo.death_until:
                ufo.active = False

        if stage >= 5:
            screen.blit(font.render(f"Счёт: {score}", True, TEXT), (12, 12))
        if stage >= 6:
            screen.blit(font.render(f"Жизни: {lives}", True, TEXT), (12, 40))
        if stage >= 8:
            if won:
                msg = font.render("Победа! R — заново", True, (120, 255, 160))
                screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            elif game_over:
                msg = font.render("Поражение — R", True, (255, 120, 120))
                screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
