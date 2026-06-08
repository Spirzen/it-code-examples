#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, CardMaker, DirectionalLight, LineSegs

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -15, 8)
        self.camera.lookAt(0, 0, 0)

        ls = LineSegs("grid")
        ls.setColor(0.35, 0.45, 0.6, 0.8)
        ls.setThickness(1)
        step = 1.0
        extent = 8
        for i in range(-extent, extent + 1):
            x = i * step
            ls.moveTo(x, -extent * step, 0)
            ls.drawTo(x, extent * step, 0)
            ls.moveTo(-extent * step, x, 0)
            ls.drawTo(extent * step, x, 0)
        self.render.attachNewNode(ls.create())

        cm = CardMaker("floor")
        cm.setFrame(-extent, extent, -extent, extent)
        floor = self.render.attachNewNode(cm.generate())
        floor.setP(-90)
        floor.setColor(0.12, 0.14, 0.18, 1)
        floor.setLightOff()

        ambient = AmbientLight("ambient")
        ambient.setColor((0.4, 0.4, 0.45, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -60, 0)
        self.render.setLight(sun_np)

        self.cube = self.loader.loadModel("models/misc/sphere")
        self.cube.reparentTo(self.render)
        self.cube.setScale(1.2)
        self.cube.setPos(0, 0, 1.2)
        self.cube.setColor(0.4, 0.75, 0.95, 1)

if __name__ == "__main__":
    App().run()
