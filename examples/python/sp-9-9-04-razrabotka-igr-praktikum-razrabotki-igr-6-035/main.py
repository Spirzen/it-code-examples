from core.config import ISO_TILE_H, ISO_TILE_W


class Camera:
    def __init__(self) -> None:
        self.x = 0.0
        self.y = 0.0
        self.smooth = 8.0

    def follow(self, target_x: float, target_y: float, dt: float) -> None:
        tx = (target_x - target_y) * (ISO_TILE_W / 2)
        ty = (target_x + target_y) * (ISO_TILE_H / 2)
        t = min(1.0, self.smooth * dt)
        self.x += (tx - self.x) * t
        self.y += (ty - self.y) * t
