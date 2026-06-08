#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.07, 0.09, 0.13, 1)
        self.disableMouse()
        self.camera.setPos(0, -12, 5)
        self.camera.lookAt(0, 0, 2)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(50, -45, 0)
        self.render.setLight(sun_np)

        template = self.loader.loadModel("models/box")
        levels = 8
        for i in range(levels):
            block = template.copyTo(self.render)
            s = 1.4 - i * 0.08
            block.setScale(s, s, 0.6)
            block.setPos(0, 0, i * 0.65 + 0.3)
            t = i / max(levels - 1, 1)
            block.setColor(0.3 + t * 0.5, 0.5 - t * 0.2, 0.9 - t * 0.4, 1)

        self.taskMgr.add(self.sway, "sway")

    def sway(self, task):
        self.render.setH(5 * math.sin(globalClock.getFrameTime() * 0.5))
        return task.cont

if __name__ == "__main__":
    App().run()
