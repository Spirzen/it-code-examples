#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight

class ExperimentApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -10, 3)
        self.camera.lookAt(0, 0, 0)
        self._setup_lights()

    def _setup_lights(self):
        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

    def add_spinner(self, nodepath, speed=45.0):
        def spin(task, np=nodepath, rate=speed):
            np.setH(np.getH() + rate * globalClock.getDt())
            return task.cont
        self.taskMgr.add(spin, f"spin_{nodepath.getName()}")

# class MyScene(ExperimentApp):
#     def __init__(self):
#         super().__init__()
#         ..
#
# if __name__ == "__main__":
#     MyScene().run()
