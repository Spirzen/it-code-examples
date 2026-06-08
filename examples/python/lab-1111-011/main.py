#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, CardMaker, DirectionalLight

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.05, 0.07, 0.12, 1)
        self.disableMouse()
        self.camera.setPos(0, -12, 3)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.45, 0.45, 0.5, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        count = 12
        radius = 4.0
        self.cards = []

        for i in range(count):
            angle = 360.0 * i / count
            rad = math.radians(angle)
            cm = CardMaker(f"petal_{i}")
            cm.setFrame(-0.6, 0.6, -1.2, 1.2)
            card = self.render.attachNewNode(cm.generate())
            card.setPos(radius * math.sin(rad), radius * math.cos(rad), 0)
            card.setH(angle + 180)
            card.setColor(0.2 + i / count, 0.5, 0.9 - i / count, 1)
            self.cards.append(card)

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        for i, card in enumerate(self.cards):
            card.setR(10 * math.sin(globalClock.getFrameTime() + i))
        return task.cont

if __name__ == "__main__":
    App().run()
