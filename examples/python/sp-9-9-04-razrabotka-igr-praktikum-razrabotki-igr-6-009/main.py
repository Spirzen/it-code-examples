from dataclasses import dataclass
from core.config import TileType


@dataclass
class Tile:
    type: TileType = TileType.VOID
    walkable: bool = False

    @classmethod
    def floor(cls) -> "Tile":
        return cls(TileType.FLOOR, True)

    @classmethod
    def wall(cls) -> "Tile":
        return cls(TileType.WALL, False)

    @classmethod
    def start(cls) -> "Tile":
        t = cls(TileType.START, True)
        return t

    @classmethod
    def exit(cls) -> "Tile":
        t = cls(TileType.EXIT, True)
        return t
