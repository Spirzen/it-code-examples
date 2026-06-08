import math

import config as C


def build_oval_waypoints(n=32):
    points = []
    mid_rx = (C.OUTER_RX + C.INNER_RX) / 2
    mid_ry = (C.OUTER_RY + C.INNER_RY) / 2
    for i in range(n):
        t = (i / n) * 2 * math.pi
        x = C.TRACK_CX + math.cos(t) * mid_rx
        y = C.TRACK_CY + math.sin(t) * mid_ry
        points.append((x, y))
    return points


class WaypointFollower:
    def __init__(self, car, waypoints, speed=4.5):
        self.car = car
        self.waypoints = waypoints
        self.index = 0
        self.speed = speed

    def update(self):
        tx, ty = self.waypoints[self.index]
        dx = tx - self.car.x
        dy = ty - self.car.y
        dist = math.hypot(dx, dy)
        if dist < 16:
            self.index = (self.index + 1) % len(self.waypoints)
            tx, ty = self.waypoints[self.index]
            dx = tx - self.car.x
            dy = ty - self.car.y
            dist = math.hypot(dx, dy)
        if dist > 0:
            self.car.x += (dx / dist) * self.speed
            self.car.y += (dy / dist) * self.speed
            self.car.angle = math.degrees(math.atan2(dy, dx))
        self.car.speed = self.speed
