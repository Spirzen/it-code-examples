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

def make_prism(n, radius, height, rgba=(0.5, 0.35, 0.9, 1)):
    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("prism", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    bottom = []
    top = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        bottom.append((x, y, 0))
        top.append((x, y, height))

    def add_quad(p0, p1, p2, p3):
        edge1 = Vec3(p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])
        edge2 = Vec3(p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2])
        n = edge1.cross(edge2)
        n.normalize()
        for p in (p0, p1, p2, p3):
            vertex.addData3(*p)
            normal.addData3(n)
            color.addData4(*rgba)

    for i in range(n):
        j = (i + 1) % n
        add_quad(bottom[i], bottom[j], top[j], top[i])

    tris = GeomTriangles(Geom.UHStatic)
    tri_count = n * 2
    for i in range(tri_count):
        base = i * 4
        tris.addVertices(base, base + 1, base + 2)
        tris.addVertices(base, base + 2, base + 3)
    tris.closePrimitive()

    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("prism")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -10, 3)
        self.camera.lookAt(0, 0, 1)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        self.prism = self.render.attachNewNode(make_prism(6, 1.8, 2.5))
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.prism.setH(self.prism.getH() + 50 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
