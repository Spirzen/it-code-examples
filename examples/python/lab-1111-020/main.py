#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, PointLight
from panda3d.core import Geom, GeomNode, GeomTriangles, GeomVertexData, GeomVertexFormat, GeomVertexWriter, Vec3

def make_cube(size=2.0):
    half = size * 0.5
    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("cube", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")
    rgba = (0.6, 0.6, 0.65, 1)

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
        self.setBackgroundColor(0.02, 0.02, 0.05, 1)
        self.disableMouse()
        self.camera.setPos(0, -9, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.08, 0.08, 0.1, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        pl = PointLight("point")
        pl.setColor((1, 0.85, 0.6, 1))
        self.light_np = self.render.attachNewNode(pl)
        self.light_np.setPos(2, -1, 3)
        self.render.setLight(self.light_np)

        self.cube = self.render.attachNewNode(make_cube())
        self.taskMgr.add(self.orbit_light, "orbit_light")

    def orbit_light(self, task):
        t = globalClock.getFrameTime()
        self.light_np.setPos(3 * math.cos(t), 3 * math.sin(t), 2.5)
        return task.cont

if __name__ == "__main__":
    App().run()
