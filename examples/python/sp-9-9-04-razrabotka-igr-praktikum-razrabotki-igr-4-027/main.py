import math
import time

import config as C


def sector_at(x, y):
    dx = x - C.TRACK_CX
    dy = y - C.TRACK_CY
    angle = math.degrees(math.atan2(dy, dx)) % 360
    return int(angle // 90)


class RaceProgress:
    def __init__(self, start_x, start_y):
        self.sector = sector_at(start_x, start_y)
        self.next_sector = (self.sector + 1) % 4
        self.lap = 0
        self.total_laps = C.TOTAL_LAPS
        self.lap_start = time.perf_counter()
        self.current_lap_time = 0.0
        self.last_lap_time = 0.0
        self.best_lap_time = None

    def update(self, x, y):
        current = sector_at(x, y)
        if current == self.next_sector:
            self.sector = current
            self.next_sector = (self.next_sector + 1) % 4
            if self.next_sector == 0:
                self.last_lap_time = time.perf_counter() - self.lap_start
                if self.best_lap_time is None or self.last_lap_time < self.best_lap_time:
                    self.best_lap_time = self.last_lap_time
                self.lap += 1
                self.lap_start = time.perf_counter()
        self.current_lap_time = time.perf_counter() - self.lap_start

    @property
    def finished(self):
        return self.lap >= self.total_laps

    def progress_score(self):
        return self.lap + self.sector / 4.0
