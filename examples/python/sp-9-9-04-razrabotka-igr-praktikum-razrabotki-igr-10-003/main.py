import math
import random
from collections import deque

import pygame

# --- display ---
WIDTH, HEIGHT = 800, 600
FPS = 60

# --- grid ---
GRID_ROWS = 12
GRID_COLS = 15
BUBBLE_RADIUS = 18
BUBBLE_DIAMETER = BUBBLE_RADIUS * 2
BUBBLE_HEIGHT = int(BUBBLE_RADIUS * math.sqrt(3))
GRID_TOP = 40
GRID_LEFT = (WIDTH - (GRID_COLS * BUBBLE_DIAMETER + BUBBLE_RADIUS)) // 2

# --- gameplay ---
COLORS = [
    (231, 76, 60),    # red
    (46, 204, 113),   # green
    (52, 152, 219),   # blue
    (241, 196, 15),   # yellow
    (155, 89, 182),   # purple
    (230, 126, 34),   # orange
]
INITIAL_ROWS = 5
MATCH_MIN = 3
SHOT_SPEED = 14
AIM_MIN_DEG = 15
AIM_MAX_DEG = 165
DANGER_Y = HEIGHT - 120

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Shooter — этап 2")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 36)


def grid_to_pixel(row: int, col: int) -> tuple[float, float]:
    x = GRID_LEFT + BUBBLE_RADIUS + col * BUBBLE_DIAMETER
    if row % 2 == 1:
        x += BUBBLE_RADIUS
    y = GRID_TOP + BUBBLE_RADIUS + row * BUBBLE_HEIGHT
    return x, y


def pixel_to_grid(x: float, y: float) -> tuple[int, int]:
    row = round((y - GRID_TOP - BUBBLE_RADIUS) / BUBBLE_HEIGHT)
    row = max(0, min(GRID_ROWS - 1, row))
    if row % 2 == 0:
        col = round((x - GRID_LEFT - BUBBLE_RADIUS) / BUBBLE_DIAMETER)
    else:
        col = round((x - GRID_LEFT - BUBBLE_RADIUS * 2) / BUBBLE_DIAMETER)
    col = max(0, min(GRID_COLS - 1, col))
    return row, col


def neighbor_offsets(row: int) -> list[tuple[int, int]]:
    even = row % 2 == 0
    return [
        (-1, -1 if even else 0),
        (-1, 0 if even else 1),
        (0, -1),
        (0, 1),
        (1, -1 if even else 0),
        (1, 0 if even else 1),
    ]


def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x1 - x2, y1 - y2)


class Bubble:
    __slots__ = ("row", "col", "color")

    def __init__(self, row: int, col: int, color: tuple[int, int, int]):
        self.row = row
        self.col = col
        self.color = color

    @property
    def x(self) -> float:
        return grid_to_pixel(self.row, self.col)[0]

    @property
    def y(self) -> float:
        return grid_to_pixel(self.row, self.col)[1]

    def draw(self, surface: pygame.Surface) -> None:
        px, py = int(self.x), int(self.y)
        pygame.draw.circle(surface, self.color, (px, py), BUBBLE_RADIUS)
        highlight = tuple(min(255, c + 60) for c in self.color)
        pygame.draw.circle(surface, highlight, (px - 5, py - 5), 5)
        pygame.draw.circle(surface, (40, 40, 50), (px, py), BUBBLE_RADIUS, 2)



    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.angle = math.pi / 2
        self.current_color = random.choice(COLORS)
        self.next_color = random.choice(COLORS)

    def aim_at(self, mouse_x: int, mouse_y: int) -> None:
        dx = mouse_x - self.x
        dy = self.y - mouse_y
        angle = math.atan2(dy, dx)
        lo = math.radians(AIM_MIN_DEG)
        hi = math.radians(AIM_MAX_DEG)
        self.angle = max(lo, min(hi, angle))

    def shoot(self) -> MovingBubble:
        dx = math.cos(self.angle) * SHOT_SPEED
        dy = -math.sin(self.angle) * SHOT_SPEED
        return MovingBubble(self.x, self.y, dx, dy, self.current_color)

    def advance(self) -> None:
        self.current_color = self.next_color
        self.next_color = random.choice(COLORS)

    def swap(self) -> None:
        self.current_color, self.next_color = self.next_color, self.current_color

    def draw(self, surface: pygame.Surface, show_aim: bool) -> None:
        if show_aim:
            self._draw_aim_guide(surface)
        px, py = int(self.x), int(self.y)
        pygame.draw.circle(surface, self.current_color, (px, py), BUBBLE_RADIUS)
        pygame.draw.circle(surface, (40, 40, 50), (px, py), BUBBLE_RADIUS, 2)
        nx = self.x + 70
        pygame.draw.circle(surface, self.next_color, (int(nx), py), BUBBLE_RADIUS - 4)
        pygame.draw.circle(surface, (40, 40, 50), (int(nx), py), BUBBLE_RADIUS - 4, 2)
        label = font.render("Next", True, (180, 180, 190))
        surface.blit(label, (int(nx) - 22, py + 22))

    def _draw_aim_guide(self, surface: pygame.Surface) -> None:
        x, y = float(self.x), float(self.y)
        dx = math.cos(self.angle)
        dy = -math.sin(self.angle)
        for step in range(1, 28):
            x += dx * 18
            y += dy * 18
            if y < GRID_TOP:
                break
            if x <= BUBBLE_RADIUS or x >= WIDTH - BUBBLE_RADIUS:
                dx = -dx
                x += dx * 18
            alpha = max(40, 180 - step * 6)
            dot = pygame.Surface((8, 8), pygame.SRCALPHA)
            pygame.draw.circle(dot, (255, 255, 255, alpha), (4, 4), 3)
            surface.blit(dot, (int(x) - 4, int(y) - 4))


class Game:
    def __init__(self):
        self.grid: list[list[Bubble | None]] = [
            [None] * GRID_COLS for _ in range(GRID_ROWS)
        ]
        self._fill_initial_grid()

    def _fill_initial_grid(self) -> None:
        for row in range(INITIAL_ROWS):
            for col in range(GRID_COLS):
                self.grid[row][col] = Bubble(row, col, random.choice(COLORS))

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((24, 26, 34))
        for x in range(GRID_LEFT, WIDTH - GRID_LEFT, 40):
            pygame.draw.line(surface, (34, 36, 46), (x, GRID_TOP), (x, int(DANGER_Y)), 1)
        pygame.draw.line(surface, (220, 70, 70), (GRID_LEFT, int(DANGER_Y)), (WIDTH - GRID_LEFT, int(DANGER_Y)), 2)
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                cell = self.grid[row][col]
                if cell is not None:
                    cell.draw(surface)
        pygame.display.flip()


def main() -> None:
    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        game.draw(screen)
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
