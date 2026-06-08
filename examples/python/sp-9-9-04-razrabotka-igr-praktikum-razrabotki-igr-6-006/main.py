import pygame
from core.config import ISO_TILE_H, ISO_TILE_W, SCREEN_HEIGHT, SCREEN_WIDTH


def world_to_screen(wx: float, wy: float, cam_x: float, cam_y: float) -> tuple[float, float]:
    sx = (wx - wy) * (ISO_TILE_W / 2) - cam_x + SCREEN_WIDTH / 2
    sy = (wx + wy) * (ISO_TILE_H / 2) - cam_y + SCREEN_HEIGHT / 2 - 80
    return sx, sy


def screen_to_world(sx: float, sy: float, cam_x: float, cam_y: float) -> tuple[float, float]:
    x = sx - SCREEN_WIDTH / 2 + cam_x
    y = sy - SCREEN_HEIGHT / 2 + 80 + cam_y
    wx = (x / (ISO_TILE_W / 2) + y / (ISO_TILE_H / 2)) / 2
    wy = (y / (ISO_TILE_H / 2) - x / (ISO_TILE_W / 2)) / 2
    return wx, wy


class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def draw_entity_circle(self, wx: float, wy: float, cam_x: float, cam_y: float,
                           radius_px: int, color: tuple[int, int, int]) -> None:
        sx, sy = world_to_screen(wx, wy, cam_x, cam_y)
        pygame.draw.circle(self.screen, color, (int(sx), int(sy)), radius_px)
