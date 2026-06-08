import math


class Car:
    def __init__(self, x, y, angle, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.0
        self.color = color
        self.width = 44
        self.height = 22

    def draw(self, surface):
        body = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(body, self.color, (0, 0, self.width, self.height), border_radius=4)
        pygame.draw.rect(body, (200, 220, 255), (self.width - 14, 4, 10, self.height - 8), border_radius=2)
        rotated = pygame.transform.rotate(body, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated, rect)
