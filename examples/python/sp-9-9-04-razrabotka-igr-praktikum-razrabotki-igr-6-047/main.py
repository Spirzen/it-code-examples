import math

from world.map import GameMap

ENTITY_RADIUS = 0.34


def can_occupy(game_map: GameMap, x: float, y: float, radius: float = ENTITY_RADIUS) -> bool:
    for dx, dy in ((0, 0), (-radius, 0), (radius, 0), (0, -radius), (0, radius)):
        if not game_map.is_walkable(int(x + dx), int(y + dy)):
            return False
    return True


def move_slide(
    game_map: GameMap,
    x: float,
    y: float,
    dx: float,
    dy: float,
    radius: float = ENTITY_RADIUS,
) -> tuple[float, float]:
    dist = math.hypot(dx, dy)
    if dist < 1e-6:
        return x, y
    steps = max(4, int(dist * 28))
    sx, sy = dx / steps, dy / steps
    for _ in range(steps):
        nx, ny = x + sx, y + sy
        if can_occupy(game_map, nx, ny, radius):
            x, y = nx, ny
        else:
            if can_occupy(game_map, x + sx, y, radius):
                x += sx
            if can_occupy(game_map, x, y + sy, radius):
                y += sy
    return x, y
