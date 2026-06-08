#!/usr/bin/env python3

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

def make_pyramid(base=2.0, height=2.5):
    half = base * 0.5
    apex = (0, 0, height)
    base_corners = [(-half, -half, 0), (half, -half, 0), (half, half, 0), (-half, half, 0)]

    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("pyramid", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    def add_tri(p1, p2, p3, rgba):
        edge1 = Vec3(p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
        edge2 = Vec3(p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
        n = edge1.cross(edge2)
        n.normalize()
        for p in (p1, p2, p3):
            vertex.addData3(*p)
            normal.addData3(n)
            color.addData4(*rgba)

    side_color = (0.9, 0.55, 0.2, 1)
    base_color = (0.25, 0.45, 0.85, 1)

    for i in range(4):
        p1 = base_corners[i]
        p2 = base_corners[(i + 1) % 4]
        add_tri(p1, p2, apex, side_color)

    add_tri(base_corners[0], base_corners[2], base_corners[1], base_color)
    add_tri(base_corners[0], base_corners[3], base_corners[2], base_color)

    tris = GeomTriangles(Geom.UHStatic)
    for i in range(6):
        base = i * 3
        tris.addVertices(base, base + 1, base + 2)
    tris.closePrimitive()

    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("pyramid")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -9, 3)
        self.camera.lookAt(0, 1, 1)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.95, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(50, -50, 0)
        self.render.setLight(sun_np)

        self.pyramid = self.render.attachNewNode(make_pyramid())
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.pyramid.setH(self.pyramid.getH() + 40 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
