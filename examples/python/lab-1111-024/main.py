#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs

def wireframe_sphere(segs, radius=2.0, meridians=12, parallels=8):
    segs.setColor(0.5, 0.85, 1.0, 1)
    segs.setThickness(1)

    for m in range(meridians):
        theta = 2 * math.pi * m / meridians
        for p in range(parallels + 1):
            phi = math.pi * p / parallels
            x = radius * math.sin(phi) * math.cos(theta)
            y = radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(phi)
            if p == 0:
                segs.moveTo(x, y, z)
            else:
                segs.drawTo(x, y, z)

    for p in range(1, parallels):
        phi = math.pi * p / parallels
        r = radius * math.sin(phi)
        z = radius * math.cos(phi)
        for m in range(meridians + 1):
            theta = 2 * math.pi * m / meridians
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            if m == 0:
                segs.moveTo(x, y, z)
            else:
                segs.drawTo(x, y, z)

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.04, 0.05, 0.09, 1)
        self.disableMouse()
        self.camera.setPos(0, -9, 2)
        self.camera.lookAt(0, 0, 0)

        ls = LineSegs("wire_sphere")
        wireframe_sphere(ls)
        self.wire = self.render.attachNewNode(ls.create())
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.wire.setH(self.wire.getH() + 20 * globalClock.getDt())
        self.wire.setP(self.wire.getP() + 8 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
