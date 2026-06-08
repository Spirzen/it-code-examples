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

def make_tetrahedron(size=2.5, rgba=(0.9, 0.75, 0.2, 1)):
    s = size
    verts = [
        (s, s, s), (s, -s, -s), (-s, s, -s), (-s, -s, s),
    ]
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("tetra", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    tris = GeomTriangles(Geom.UHStatic)
    idx = 0
    for face in faces:
        p1, p2, p3 = (verts[i] for i in face)
        e1 = Vec3(p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
        e2 = Vec3(p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
        n = e1.cross(e2)
        n.normalize()
        for p in (p1, p2, p3):
            vertex.addData3(*p)
            normal.addData3(n)
            color.addData4(*rgba)
        tris.addVertices(idx, idx + 1, idx + 2)
        idx += 3

    tris.closePrimitive()
    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("tetrahedron")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -10, 3)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.95, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(40, -50, 0)
        self.render.setLight(sun_np)

        self.tetra = self.render.attachNewNode(make_tetrahedron())
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        t = globalClock.getFrameTime()
        self.tetra.setH(40 * t)
        self.tetra.setP(25 * t)
        return task.cont

if __name__ == "__main__":
    App().run()
