#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs

def wireframe_cube(segs, size=2.0):
    half = size * 0.5
    corners = [
        (-half, -half, -half), (half, -half, -half), (half, half, -half), (-half, half, -half),
        (-half, -half, half), (half, -half, half), (half, half, half), (-half, half, half),
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]
    segs.setColor(0.4, 0.85, 1.0, 1)
    segs.setThickness(2)
    for a, b in edges:
        segs.moveTo(*corners[a])
        segs.drawTo(*corners[b])

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.05, 0.06, 0.1, 1)
        self.disableMouse()
        self.camera.setPos(0, -10, 4)
        self.camera.lookAt(0, 0, 0)

        ls = LineSegs("wire_cube")
        wireframe_cube(ls, 2.5)
        self.wire = self.render.attachNewNode(ls.create())
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.wire.setH(self.wire.getH() + 30 * globalClock.getDt())
        self.wire.setP(self.wire.getP() + 15 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
