import math
import pygame
import config as C
from game.progress import sector_at


def draw_sectors(surface, font):
    colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255), (255, 255, 100)]
    for s in range(4):
        a0 = math.radians(s * 90)
        a1 = math.radians((s + 1) * 90)
        x0 = C.TRACK_CX + math.cos(a0) * (C.INNER_RX + 40)
        y0 = C.TRACK_CY + math.sin(a0) * (C.INNER_RY + 40)
        x1 = C.TRACK_CX + math.cos(a1) * (C.OUTER_RX - 20)
        y1 = C.TRACK_CY + math.sin(a1) * (C.OUTER_RY - 20)
        pygame.draw.line(surface, colors[s], (x0, y0), (x1, y1), 2)
        label = font.render(str(s), True, colors[s])
        surface.blit(label, (x0, y0))


def draw_waypoints(surface, waypoints):
    for i, (wx, wy) in enumerate(waypoints):
        pygame.draw.circle(surface, (255, 180, 0), (int(wx), int(wy)), 3)
        if i % 4 == 0:
            pygame.draw.circle(surface, (255, 255, 255), (int(wx), int(wy)), 6, 1)


def draw_car_debug(surface, car, font):
    s = sector_at(car.x, car.y)
    t = font.render(f"sec={s} sp={car.speed:.1f}", True, (255, 255, 255))
    surface.blit(t, (int(car.x) - 20, int(car.y) - 30))
