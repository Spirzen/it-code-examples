#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs

def regular_polygon_lines(segs, n, radius, z=0.0):
    segs.setThickness(3)
    for i in range(n + 1):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        if i == 0:
            segs.moveTo(x, y, z)
        else:
            segs.drawTo(x, y, z)

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -12, 0)
        self.camera.lookAt(0, 0, 0)

        for sides, radius, color in [(3, 2, (1, 0.3, 0.3, 1)), (6, 3, (0.3, 1, 0.5, 1)), (8, 4, (0.4, 0.6, 1, 1))]:
            ls = LineSegs(f"poly_{sides}")
            ls.setColor(*color)
            regular_polygon_lines(ls, sides, radius, z=0)
            np = self.render.attachNewNode(ls.create())
            np.setY(radius - 4)

if __name__ == "__main__":
    App().run()
