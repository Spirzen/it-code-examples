import time


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
