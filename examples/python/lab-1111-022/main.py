#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, TextNode

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -10, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.4, 0.4, 0.45, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        self.sphere = self.loader.loadModel("models/misc/sphere")
        self.sphere.reparentTo(self.render)
        self.sphere.setScale(1.8)
        self.sphere.setColor(0.3, 0.7, 0.5, 1)

        tn = TextNode("label")
        tn.setText("Panda3D")
        tn.setAlign(TextNode.ACenter)
        tn.setTextColor(1, 0.95, 0.8, 1)
        label = self.render.attachNewNode(tn.generate())
        label.setScale(0.8)
        label.setPos(0, 0, 2.5)
        label.setBillboardPointEye()

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.sphere.setH(self.sphere.getH() + 30 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
