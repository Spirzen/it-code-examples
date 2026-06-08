from world.level_generator import LevelGenerator


class GameMap:
    def __init__(self, floor: int = 1, seed: int | None = None) -> None:
        gen = LevelGenerator(seed)
        self.grid, self.start_tile, self.exit_tile = gen.generate()
        self.floor = floor

    def is_walkable(self, x: int, y: int) -> bool:
        from core.config import MAP_HEIGHT, MAP_WIDTH
        if not (0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT):
            return False
        return self.grid[y][x].walkable
