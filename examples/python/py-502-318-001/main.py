#!/usr/bin/env python3
"""Minimal Panda3D application."""

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, CardMaker, DirectionalLight


class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -8, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        cm = CardMaker("card")
        cm.setFrame(-2, 2, -2, 2)
        self.card = self.render.attachNewNode(cm.generate())
        self.card.setColor(0.25, 0.55, 0.95, 1)
        self.card.setP(-20)

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.card.setH(self.card.getH() + 60 * globalClock.getDt())
        return task.cont


if __name__ == "__main__":
    app = App()
    app.run()
