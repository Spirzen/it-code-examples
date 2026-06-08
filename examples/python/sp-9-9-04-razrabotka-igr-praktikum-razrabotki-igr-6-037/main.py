import pygame

from core.config import ISO_TILE_H, ISO_TILE_W, TileType
from engine.renderer import world_to_screen
from world.map import GameMap


class MapRenderer:
    FLOOR_COLOR = (42, 48, 72)
    WALL_COLOR = (22, 26, 42)
    EXIT_COLOR = (255, 180, 60)

    def __init__(self, renderer) -> None:
        self.r = renderer

    def draw(self, game_map: GameMap, cam_x: float, cam_y: float) -> None:
        from core.config import MAP_HEIGHT, MAP_WIDTH

        for ty in range(MAP_HEIGHT):
            for tx in range(MAP_WIDTH):
                tile = game_map.grid[ty][tx]
                if tile.type == TileType.VOID:
                    continue
                color = self.FLOOR_COLOR
                if tile.type == TileType.WALL:
                    color = self.WALL_COLOR
                if tile.type == TileType.EXIT:
                    color = self.EXIT_COLOR
                self._draw_diamond(tx + 0.5, ty + 0.5, cam_x, cam_y, color)

    def _draw_diamond(self, wx, wy, cam_x, cam_y, color) -> None:
        cx, cy = world_to_screen(wx, wy, cam_x, cam_y)
        hw, hh = ISO_TILE_W // 2, ISO_TILE_H // 2
        points = [(cx, cy - hh), (cx + hw, cy), (cx, cy + hh), (cx - hw, cy)]
        pygame.draw.polygon(self.r.screen, color, points)
