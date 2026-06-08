import pygame

import config as C


def ellipse_norm(x, y, rx, ry):
    dx = x - C.TRACK_CX
    dy = y - C.TRACK_CY
    return (dx / rx) ** 2 + (dy / ry) ** 2


class Track:
    EPS = 0.02

    def is_on_track(self, x, y):
        outer = ellipse_norm(x, y, C.OUTER_RX, C.OUTER_RY)
        inner = ellipse_norm(x, y, C.INNER_RX, C.INNER_RY)
        return inner >= 1.0 - self.EPS and outer <= 1.0 + self.EPS

    def clamp_car(self, car):
        x, y = car.x, car.y
        inner = ellipse_norm(x, y, C.INNER_RX, C.INNER_RY)
        outer = ellipse_norm(x, y, C.OUTER_RX, C.OUTER_RY)
        dx = x - C.TRACK_CX
        dy = y - C.TRACK_CY
        hit = False

        if outer > 1.0:
            scale = (1.0 - self.EPS) / (outer**0.5)
            x = C.TRACK_CX + dx * scale
            y = C.TRACK_CY + dy * scale
            hit = True
        elif inner < 1.0:
            scale = (1.0 + self.EPS) / (inner**0.5)
            x = C.TRACK_CX + dx * scale
            y = C.TRACK_CY + dy * scale
            hit = True

        if hit:
            car.speed *= 0.55
        car.x, car.y = x, y

    def draw(self, surface):
        outer = pygame.Rect(
            C.TRACK_CX - C.OUTER_RX,
            C.TRACK_CY - C.OUTER_RY,
            C.OUTER_RX * 2,
            C.OUTER_RY * 2,
        )
        inner = pygame.Rect(
            C.TRACK_CX - C.INNER_RX,
            C.TRACK_CY - C.INNER_RY,
            C.INNER_RX * 2,
            C.INNER_RY * 2,
        )
        pygame.draw.ellipse(surface, C.COLOR_ASPHALT, outer)
        pygame.draw.ellipse(surface, C.COLOR_LAWN, inner)
        pygame.draw.ellipse(surface, C.COLOR_LINE, outer, 3)
        pygame.draw.ellipse(surface, C.COLOR_LINE, inner, 2)

        finish_x = C.TRACK_CX
        finish_y = C.TRACK_CY + (C.INNER_RY + C.OUTER_RY) // 2
        pygame.draw.line(
            surface,
            (255, 255, 0),
            (finish_x - 30, finish_y),
            (finish_x + 30, finish_y),
            4,
        )
