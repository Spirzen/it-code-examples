#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.05, 0.06, 0.1, 1)
        self.disableMouse()
        self.camera.setPos(0, -12, 2)
        self.camera.lookAt(0, 0, 2)

        turns = 4
        steps = 120
        radius = 1.5
        height = 5.0

        for phase, color in ((0, (0.4, 0.85, 1, 1)), (math.pi, (1, 0.5, 0.4, 1))):
            ls = LineSegs(f"helix_{phase}")
            ls.setColor(*color)
            ls.setThickness(3)
            for i in range(steps + 1):
                t = i / steps
                angle = turns * 2 * math.pi * t + phase
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                z = height * t
                if i == 0:
                    ls.moveTo(x, y, z)
                else:
                    ls.drawTo(x, y, z)
            self.render.attachNewNode(ls.create())

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.render.setH(self.render.getH() + 15 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
