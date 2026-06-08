from random import uniform
from kivy.graphics import Ellipse
from kivy.properties import NumericProperty


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self._update_ellipse, size=self._update_ellipse)

    def serve(self, direction_y=-1):
        speed = self.parent.ball_speed if self.parent else 420
        self.velocity_x = uniform(-0.35, 0.35) * speed
        self.velocity_y = direction_y * speed * 0.85

    def stop(self):
        self.velocity_x = 0
        self.velocity_y = 0
