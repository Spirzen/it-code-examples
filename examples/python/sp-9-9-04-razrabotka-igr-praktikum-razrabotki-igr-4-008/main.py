import math
import config as C


def sector_at(x, y):
    dx = x - C.TRACK_CX
    dy = y - C.TRACK_CY
    angle = math.degrees(math.atan2(dy, dx)) % 360
    return int(angle // 90)  # 0: право, 1: низ, 2: лево, 3: верх


class RaceProgress:
    def __init__(self, start_x, start_y):
        self.sector = sector_at(start_x, start_y)
        self.next_sector = (self.sector + 1) % 4
        self.lap = 0
        self.total_laps = C.TOTAL_LAPS

    def update(self, x, y):
        current = sector_at(x, y)
        if current == self.next_sector:
            self.sector = current
            self.next_sector = (self.next_sector + 1) % 4
            if self.next_sector == 0:
                self.lap += 1

    @property
    def finished(self):
        return self.lap >= self.total_laps

    def progress_score(self):
        """0.0 … 1.0 — доля текущего круга для таблицы позиций (этап 15)."""
        return self.lap + self.sector / 4.0
