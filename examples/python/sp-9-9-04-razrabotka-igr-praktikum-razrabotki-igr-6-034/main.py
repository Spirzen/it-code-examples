import math

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

    def draw_entity_circle(
        self,
        wx: float,
        wy: float,
        cam_x: float,
        cam_y: float,
        radius_px: int,
        color: tuple[int, int, int],
    ) -> None:
        sx, sy = world_to_screen(wx, wy, cam_x, cam_y)
        pygame.draw.circle(self.screen, color, (int(sx), int(sy)), radius_px)

    def draw_slash(self, slash, cam_x: float, cam_y: float) -> None:
        sx, sy = world_to_screen(slash.x, slash.y, cam_x, cam_y)
        r = 48
        start = -slash.angle + math.pi / 2
        end = start + math.pi
        rect = pygame.Rect(sx - r, sy - r, r * 2, r * 2)
        pygame.draw.arc(self.screen, (255, 220, 120), rect, start, end, 3)

    def draw_enemy_hp(self, enemy, cam_x: float, cam_y: float) -> None:
        sx, sy = world_to_screen(enemy.x, enemy.y, cam_x, cam_y)
        w, h = 36, 5
        x = int(sx - w // 2)
        y = int(sy - 28)
        pygame.draw.rect(self.screen, (40, 20, 24), (x, y, w, h))
        if enemy.max_hp > 0:
            fill = int(w * max(0, enemy.hp) / enemy.max_hp)
            pygame.draw.rect(self.screen, (220, 60, 60), (x, y, fill, h))

    def draw_ground_item(self, item, cam_x: float, cam_y: float) -> None:
        sx, sy = world_to_screen(item.x, item.y, cam_x, cam_y)
        pygame.draw.circle(self.screen, item.color, (int(sx), int(sy)), 8)

    def draw_projectile(self, proj, cam_x: float, cam_y: float) -> None:
        sx, sy = world_to_screen(proj.x, proj.y, cam_x, cam_y)
        pygame.draw.circle(self.screen, (255, 120, 40), (int(sx), int(sy)), 10)
