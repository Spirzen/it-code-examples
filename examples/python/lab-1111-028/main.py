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

FACE_COLORS = [
    (0.9, 0.2, 0.2, 1),
    (0.2, 0.85, 0.3, 1),
    (0.25, 0.45, 0.95, 1),
    (0.95, 0.85, 0.2, 1),
    (0.85, 0.35, 0.9, 1),
    (0.3, 0.85, 0.85, 1),
]

def make_rubik_cube(size=2.0):
    half = size * 0.5
    faces = [
        (Vec3(0, 0, 1), [(-half, -half, half), (half, -half, half), (half, half, half), (-half, half, half)]),
        (Vec3(0, 0, -1), [(half, -half, -half), (-half, -half, -half), (-half, half, -half), (half, half, -half)]),
        (Vec3(0, 1, 0), [(-half, half, half), (half, half, half), (half, half, -half), (-half, half, -half)]),
        (Vec3(0, -1, 0), [(-half, -half, -half), (half, -half, -half), (half, -half, half), (-half, -half, half)]),
        (Vec3(1, 0, 0), [(half, -half, half), (half, -half, -half), (half, half, -half), (half, half, half)]),
        (Vec3(-1, 0, 0), [(-half, -half, -half), (-half, -half, half), (-half, half, half), (-half, half, -half)]),
    ]

    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("rubik", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    tris = GeomTriangles(Geom.UHStatic)
    for fi, (n, corners) in enumerate(faces):
        rgba = FACE_COLORS[fi]
        base = vertex.getWriteRow()
        for corner in corners:
            vertex.addData3(*corner)
            normal.addData3(n)
            color.addData4(*rgba)
        tris.addVertices(base, base + 1, base + 2)
        tris.addVertices(base, base + 2, base + 3)

    tris.closePrimitive()
    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("rubik_cube")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -8, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.45, 0.45, 0.5, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        self.cube = self.render.attachNewNode(make_rubik_cube())
        self.cube.setLightOff()
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.cube.setH(self.cube.getH() + 40 * globalClock.getDt())
        self.cube.setP(self.cube.getP() + 20 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
