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

def make_cylinder(radius=1.0, height=2.5, segments=24, rgba=(0.45, 0.7, 0.35, 1)):
    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("cylinder", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    def add_vertex(x, y, z, nx, ny, nz):
        vertex.addData3(x, y, z)
        normal.addData3(nx, ny, nz)
        color.addData4(*rgba)

    half = height * 0.5
    ring_bottom = []
    ring_top = []
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        cx = math.cos(angle)
        sy = math.sin(angle)
        ring_bottom.append((radius * cx, radius * sy, -half))
        ring_top.append((radius * cx, radius * sy, half))

    tris = GeomTriangles(Geom.UHStatic)
    idx = 0

    for i in range(segments):
        j = (i + 1) % segments
        b0, b1 = ring_bottom[i], ring_bottom[j]
        t0, t1 = ring_top[i], ring_top[j]
        for p1, p2, p3 in ((b0, b1, t1), (b0, t1, t0)):
            edge1 = Vec3(p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
            edge2 = Vec3(p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
            n = edge1.cross(edge2)
            n.normalize()
            for p in (p1, p2, p3):
                add_vertex(*p, n.x, n.y, n.z)
            tris.addVertices(idx, idx + 1, idx + 2)
            idx += 3

    for z, ring, nz in ((-half, ring_bottom, -1), (half, ring_top, 1)):
        center_idx = idx
        add_vertex(0, 0, z, 0, 0, nz)
        idx += 1
        start = idx
        for x, y, _ in ring:
            add_vertex(x, y, z, 0, 0, nz)
            idx += 1
        for i in range(segments):
            j = (i + 1) % segments
            if nz < 0:
                tris.addVertices(center_idx, start + j, start + i)
            else:
                tris.addVertices(center_idx, start + i, start + j)

    tris.closePrimitive()
    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("cylinder")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -9, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        self.cyl = self.render.attachNewNode(make_cylinder())
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.cyl.setH(self.cyl.getH() + 50 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
