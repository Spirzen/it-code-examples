from kivy.clock import Clock

# в __init__ GameField:
Clock.schedule_interval(self.update, 1.0 / 60.0)

def update(self, dt):
    if not self.running:
        return
    self._move_ball(dt)

def _move_ball(self, dt):
    ball = self.ball
    ball.x += ball.velocity_x * dt
    ball.y += ball.velocity_y * dt
