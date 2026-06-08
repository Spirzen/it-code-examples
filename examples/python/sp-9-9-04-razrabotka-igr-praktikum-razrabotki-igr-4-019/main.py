import pygame
import config as C


class Minimap:
    def __init__(self):
        self.size = 120
        self.x = C.SCREEN_W - self.size - 12
        self.y = 12

    def _scale(self, px, py):
        sx = self.x + self.size // 2 + int((px - C.TRACK_CX) * 0.12)
        sy = self.y + self.size // 2 + int((py - C.TRACK_CY) * 0.12)
        return sx, sy

    def draw(self, surface, player, rivals):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, (0, 0, 0, 160), rect)
        pygame.draw.rect(surface, (200, 200, 210), rect, 2)
        pygame.draw.ellipse(
            surface, (80, 80, 85),
            rect.inflate(-20, -20), 1,
        )
        for rival in rivals:
            rx, ry = self._scale(rival.car.x, rival.car.y)
            pygame.draw.circle(surface, rival.car.color, (rx, ry), 4)
        px, py = self._scale(player.x, player.y)
        pygame.draw.circle(surface, (255, 80, 80), (px, py), 5)
