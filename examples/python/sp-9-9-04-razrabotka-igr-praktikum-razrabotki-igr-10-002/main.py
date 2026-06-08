"""Bubble Shooter — этап 1 — гексагональная сетка и координаты."""
import math

import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60

GRID_ROWS = 12
GRID_COLS = 15
BUBBLE_RADIUS = 18
BUBBLE_DIAMETER = BUBBLE_RADIUS * 2
BUBBLE_HEIGHT = int(BUBBLE_RADIUS * math.sqrt(3))
GRID_TOP = 40
GRID_LEFT = (WIDTH - (GRID_COLS * BUBBLE_DIAMETER + BUBBLE_RADIUS)) // 2
DANGER_Y = HEIGHT - 120

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Shooter — этап 1")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)


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


def main() -> None:
    running = True
    hover: tuple[int, int] | None = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEMOTION:
                hover = pixel_to_grid(*event.pos)

        screen.fill((24, 26, 34))
        for x in range(GRID_LEFT, WIDTH - GRID_LEFT, 40):
            pygame.draw.line(screen, (34, 36, 46), (x, GRID_TOP), (x, int(DANGER_Y)), 1)
        pygame.draw.line(screen, (220, 70, 70), (GRID_LEFT, int(DANGER_Y)), (WIDTH - GRID_LEFT, int(DANGER_Y)), 2)

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                px, py = grid_to_pixel(row, col)
                color = (70, 74, 90) if hover != (row, col) else (120, 130, 160)
                pygame.draw.circle(screen, color, (int(px), int(py)), BUBBLE_RADIUS, 1)

        if hover is not None:
            label = font.render(f"row={hover[0]} col={hover[1]}", True, (210, 210, 220))
            screen.blit(label, (20, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
