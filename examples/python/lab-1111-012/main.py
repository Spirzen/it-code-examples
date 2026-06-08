#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, CardMaker, DirectionalLight, Vec3
from panda3d.core import Geom, GeomNode, GeomTriangles, GeomVertexData, GeomVertexFormat, GeomVertexWriter

def make_cube(size=1.5, rgba=(0.35, 0.55, 0.95, 1)):
    half = size * 0.5
    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("cube", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    def quad(n, corners):
        for corner in corners:
            vertex.addData3(*corner)
            normal.addData3(n)
            color.addData4(*rgba)

    quad(Vec3(0, 0, 1), [(-half, -half, half), (half, -half, half), (half, half, half), (-half, half, half)])
    quad(Vec3(0, 0, -1), [(half, -half, -half), (-half, -half, -half), (-half, half, -half), (half, half, -half)])
    quad(Vec3(0, 1, 0), [(-half, half, half), (half, half, half), (half, half, -half), (-half, half, -half)])
    quad(Vec3(0, -1, 0), [(-half, -half, -half), (half, -half, -half), (half, -half, half), (-half, -half, half)])
    quad(Vec3(1, 0, 0), [(half, -half, half), (half, -half, -half), (half, half, -half), (half, half, half)])
    quad(Vec3(-1, 0, 0), [(-half, -half, -half), (-half, -half, half), (-half, half, half), (-half, half, -half)])

    tris = GeomTriangles(Geom.UHStatic)
    for face in range(6):
        base = face * 4
        tris.addVertices(base, base + 1, base + 2)
        tris.addVertices(base, base + 2, base + 3)
    tris.closePrimitive()
    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("cube")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -12, 4)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        self.cube = self.render.attachNewNode(make_cube(1.8))
        self.cube.setPos(-2.5, 0, 0.9)

        self.sphere = self.loader.loadModel("models/misc/sphere")
        self.sphere.reparentTo(self.render)
        self.sphere.setScale(1.6)
        self.sphere.setPos(2.5, 0, 0.9)
        self.sphere.setColor(0.3, 0.8, 0.5, 1)

        cm = CardMaker("floor")
        cm.setFrame(-5, 5, -5, 5)
        floor = self.render.attachNewNode(cm.generate())
        floor.setP(-90)
        floor.setColor(0.15, 0.17, 0.22, 1)
        floor.setLightOff()

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        dt = globalClock.getDt()
        self.cube.setH(self.cube.getH() + 40 * dt)
        self.sphere.setH(self.sphere.getH() - 30 * dt)
        return task.cont

if __name__ == "__main__":
    App().run()
