#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, CardMaker, DirectionalLight

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.05, 0.07, 0.11, 1)
        self.disableMouse()
        self.camera.setPos(0, -14, 4)
        self.camera.lookAt(0, 0, 2)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.45, 0.45, 0.5, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        count = 24
        self.pieces = []
        for i in range(count):
            angle = math.radians(i * 15)
            cm = CardMaker(f"helix_{i}")
            cm.setFrame(-0.5, 0.5, -0.8, 0.8)
            card = self.render.attachNewNode(cm.generate())
            r = 3.0
            card.setPos(r * math.cos(angle), r * math.sin(angle), i * 0.25)
            card.setH(math.degrees(angle) + 90)
            card.setColor(0.2 + i / count, 0.5, 1.0 - i / count, 1)
            card.setLightOff()
            self.pieces.append(card)

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        dt = globalClock.getDt()
        for card in self.pieces:
            card.setH(card.getH() + 30 * dt)
        return task.cont

if __name__ == "__main__":
    App().run()
