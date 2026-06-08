#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        self.model = self.loader.loadModel("models/misc/sphere")
        self.model.reparentTo(self.render)
        self.model.setScale(2)
        self.model.setColor(0.35, 0.6, 0.95, 1)

        self.orbit_radius = 10.0
        self.orbit_height = 3.0
        self.orbit_speed = 25.0
        self.taskMgr.add(self.orbit_camera, "orbit_camera")

    def orbit_camera(self, task):
        angle = math.radians(self.orbit_speed * globalClock.getFrameTime())
        self.camera.setPos(
            self.orbit_radius * math.sin(angle),
            -self.orbit_radius * math.cos(angle),
            self.orbit_height,
        )
        self.camera.lookAt(0, 0, 0)
        return task.cont

if __name__ == "__main__":
    App().run()
