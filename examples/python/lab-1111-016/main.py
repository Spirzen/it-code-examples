#!/usr/bin/env python3

import math

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

def make_uv_sphere(radius=1.5, stacks=16, slices=24, rgba=(0.85, 0.4, 0.35, 1)):
    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("uv_sphere", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    def add_point(theta, phi):
        x = radius * math.sin(phi) * math.cos(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(phi)
        n = Vec3(x, y, z)
        n.normalize()
        vertex.addData3(x, y, z)
        normal.addData3(n)
        color.addData4(*rgba)

    tris = GeomTriangles(Geom.UHStatic)
    for i in range(stacks):
        phi0 = math.pi * i / stacks
        phi1 = math.pi * (i + 1) / stacks
        for j in range(slices):
            th0 = 2 * math.pi * j / slices
            th1 = 2 * math.pi * (j + 1) / slices
            base = vertex.getWriteRow()
            for theta, phi in ((th0, phi0), (th1, phi0), (th1, phi1), (th0, phi1)):
                add_point(theta, phi)
            tris.addVertices(base, base + 1, base + 2)
            tris.addVertices(base, base + 2, base + 3)

    tris.closePrimitive()
    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("uv_sphere")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.06, 0.08, 0.12, 1)
        self.disableMouse()
        self.camera.setPos(0, -7, 1)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.3, 0.3, 0.35, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((1, 0.92, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(60, -40, 0)
        self.render.setLight(sun_np)

        self.ball = self.render.attachNewNode(make_uv_sphere())
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.ball.setH(self.ball.getH() + 25 * globalClock.getDt())
        self.ball.setP(self.ball.getP() + 10 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
