import random
from dataclasses import dataclass
from core.config import MAP_HEIGHT, MAP_WIDTH, TileType
from world.tile import Tile


@dataclass
class Room:
    x: int
    y: int
    w: int
    h: int

    @property
    def center(self) -> tuple[int, int]:
        return self.x + self.w // 2, self.y + self.h // 2


class LevelGenerator:
    def __init__(self, seed: int | None = None) -> None:
        self.rng = random.Random(seed)

    def generate(self) -> tuple[list[list[Tile]], tuple[int, int], tuple[int, int]]:
        grid = [[Tile() for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        rooms: list[Room] = []
        for _ in range(80):
            if len(rooms) >= 6:
                break
            w, h = self.rng.randint(7, 11), self.rng.randint(6, 9)
            x = self.rng.randint(1, MAP_WIDTH - w - 2)
            y = self.rng.randint(1, MAP_HEIGHT - h - 2)
            room = Room(x, y, w, h)
            if any(not (room.x + room.w + 2 < r.x or r.x + r.w + 2 < room.x or
                        room.y + room.h + 2 < r.y or r.y + r.h + 2 < room.y) for r in rooms):
                continue
            rooms.append(room)
            for yy in range(room.y, room.y + room.h):
                for xx in range(room.x, room.x + room.w):
                    grid[yy][xx] = Tile.floor()

        for i in range(1, len(rooms)):
            self._connect(grid, rooms[i - 1].center, rooms[i].center)

        start = rooms[0].center
        exit_ = max(rooms, key=lambda r: abs(r.center[0] - start[0]) + abs(r.center[1] - start[1])).center
        grid[start[1]][start[0]] = Tile.start()
        grid[exit_[1]][exit_[0]] = Tile.exit()
        return grid, start, exit_

    def _connect(self, grid, a, b) -> None:
        x, y = a
        bx, by = b
        while x != bx:
            x += 1 if bx > x else -1
            if grid[y][x].type == TileType.VOID:
                grid[y][x] = Tile.floor()
        while y != by:
            y += 1 if by > y else -1
            if grid[y][x].type == TileType.VOID:
                grid[y][x] = Tile.floor()
