#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -8, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.4, 0.4, 0.45, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((1, 0.95, 0.9, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        self.sphere = self.loader.loadModel("models/misc/sphere")
        self.sphere.reparentTo(self.render)
        self.sphere.setScale(2)
        self.sphere.setColor(0.3, 0.75, 0.55, 1)

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.sphere.setH(self.sphere.getH() + 35 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
