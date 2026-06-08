def start_game(self):
    mid_y = self.rows // 2
    self.snake = [(4, mid_y), (3, mid_y), (2, mid_y)]
    self.direction = "right"
    self.next_direction = "right"
    self.running = True
    self._schedule_tick()

def _tick(self, _dt):
    self.direction = self.next_direction
    dx, dy = DIRECTIONS[self.direction]
    head_x, head_y = self.snake[0]
    new_head = (head_x + dx, head_y + dy)
    self.snake.insert(0, new_head)
    self.snake.pop()  # без еды — хвост укорачивается
    self._redraw()

def _schedule_tick(self):
    if self.tick_event:
        self.tick_event.cancel()
    self.tick_event = Clock.schedule_interval(self._tick, 0.15)
