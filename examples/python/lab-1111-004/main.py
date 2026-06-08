#!/usr/bin/env python3
"""Lit 3D cube from Geom API."""

from direct.showbase.ShowBase import ShowBase
from panda3d.core import (
    AmbientLight,
    DirectionalLight,
    Geom,
    GeomNode,
    GeomTriangles,
    GeomVertexData,
    GeomVertexFormat,
    GeomVertexWriter,
    Vec3,
)

def make_cube(size=2.0):
    half = size * 0.5
    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("cube", fmt, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    rgba = (0.35, 0.55, 0.95, 1)

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
        self.camera.setPos(0, -8, 3)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        self.cube = self.render.attachNewNode(make_cube())
        self.cube.setP(15)

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.cube.setH(self.cube.getH() + 45 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    app = App()
    app.run()
