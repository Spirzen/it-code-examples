#!/usr/bin/env python3
"""Генерация примеров для практикума Space Invaders (статья 11).

Usage:
    python scripts/generate-invaders-practicum-examples.py
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples" / "python"
SERIES = "sp-9-9-04-razrabotka-igr-praktikum-razrabotki-igr-11"
ARTICLE_TAG = "9-04-razrabotka-igr-praktikum-razrabotki-igr-11"
URL = "https://spirzen.ru/encyclopedia/9-spinoff/9-04-razrabotka-igr/praktikum-razrabotki-igr/11"

STAGE_TITLES = {
    1: "Этап 0 — минимальный запускаемый код",
    2: "Этап 1 — корабль игрока",
    3: "Этап 2 — стрельба",
    4: "Этап 3 — сетка пришельцев",
    5: "Этап 4 — движение стаи",
    6: "Этап 5 — попадания, счёт и ускорение",
    7: "Этап 6 — бомбы и жизни",
    8: "Этап 7 — бонусная тарелка (UFO)",
    9: "Этап 8 — победа, поражение и рестарт",
}

STAGE0 = textwrap.dedent(
    '''
    import sys
    import pygame

    pygame.init()
    WIDTH, HEIGHT = 640, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders — этап 0")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((8, 10, 24))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
    '''
).strip() + "\n"

# Full game single-file used for stages 2-9 (progressive features controlled by STAGE var in generator)
FULL_GAME = r'''#!/usr/bin/env python3
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
    stage = __STAGE__
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
'''

SETTINGS = textwrap.dedent(
    '''
    """Константы Space Invaders."""

    WIDTH = 640
    HEIGHT = 720
    FPS = 60

    PLAYER_Y = HEIGHT - 56
    PLAYER_SPEED = 7
    BULLET_SPEED = 12
    BOMB_SPEED = 5
    FIRE_COOLDOWN = 18

    ALIEN_ROWS = 5
    ALIEN_COLS = 11
    ALIEN_W = 40
    ALIEN_H = 28
    ALIEN_GAP_X = 14
    ALIEN_GAP_Y = 12
    ALIEN_TOP = 72
    ALIEN_H_SPEED = 3
    ALIEN_DROP = 22

    PLAYER_LIVES = 3
    UFO_INTERVAL_MS = 20_000
    UFO_SPEED = 4

    BG = (8, 10, 24)
    PLAYER_COLOR = (120, 220, 255)
    BULLET_COLOR = (255, 240, 100)
    BOMB_COLOR = (255, 90, 90)
    TEXT = (230, 230, 240)

    ROW_POINTS = [30, 20, 20, 10, 10]
    ROW_COLORS = [
        (220, 100, 100),
        (220, 160, 80),
        (180, 120, 220),
        (120, 200, 140),
        (120, 200, 140),
    ]
    '''
).strip() + "\n"

MAIN_MODULAR = textwrap.dedent(
    '''
    """Точка входа Space Invaders."""

    from game.game import Game


    def main() -> None:
        Game().run()


    if __name__ == "__main__":
        main()
    '''
).strip() + "\n"

GAME_PY = textwrap.dedent(
    '''
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
    '''
).strip() + "\n"

# Additional modular files - I'll embed shorter versions
PLAYER_PY = textwrap.dedent(
    '''
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
    '''
).strip() + "\n"

BULLETS_PY = textwrap.dedent(
    '''
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
    '''
).strip() + "\n"

ALIEN_WAVE_PY = textwrap.dedent(
    '''
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
    '''
).strip() + "\n"

UFO_PY = textwrap.dedent(
    '''
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
    '''
).strip() + "\n"

INIT_PY = "\n"


def write_example(slug: str, order: int, title: str, files: dict[str, str]) -> None:
    folder = EXAMPLES / slug
    folder.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        path = folder / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    meta = {
        "title": f"Python — Space Invaders — {title}",
        "description": f"Фрагмент из «Python — Space Invaders»: {title}.",
        "tags": ["spinoff", "encyclopedia", ARTICLE_TAG],
        "order": order,
        "series": SERIES,
        "seriesOrder": order,
        "seriesTitle": "Python — Space Invaders",
        "encyclopediaUrl": URL,
    }
    (folder / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    write_example(f"{SERIES}-001", 1, STAGE_TITLES[1], {"main.py": STAGE0})

    for idx, stage in enumerate(range(1, 9), start=2):
        code = FULL_GAME.replace("__STAGE__", str(stage))
        write_example(f"{SERIES}-{idx:03d}", idx, STAGE_TITLES[idx], {"main.py": code})

    rev = 10
    write_example(f"{SERIES}-{rev:03d}", rev, "settings.py", {"settings.py": SETTINGS})
    rev += 1
    write_example(f"{SERIES}-{rev:03d}", rev, "main.py", {"main.py": MAIN_MODULAR})
    rev += 1
    write_example(f"{SERIES}-{rev:03d}", rev, "game/game.py", {"game/game.py": GAME_PY, "game/__init__.py": INIT_PY})
    rev += 1
    write_example(f"{SERIES}-{rev:03d}", rev, "game/player.py", {"game/player.py": PLAYER_PY})
    rev += 1
    write_example(f"{SERIES}-{rev:03d}", rev, "game/bullets.py", {"game/bullets.py": BULLETS_PY})
    rev += 1
    write_example(f"{SERIES}-{rev:03d}", rev, "game/alien_wave.py", {"game/alien_wave.py": ALIEN_WAVE_PY})
    rev += 1
    write_example(f"{SERIES}-{rev:03d}", rev, "game/ufo.py", {"game/ufo.py": UFO_PY})

    print(f"Created {rev} examples under {SERIES}")


if __name__ == "__main__":
    main()
