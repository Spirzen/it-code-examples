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

def star_points(outer_r, inner_r, spikes=5):
    pts = []
    for i in range(spikes * 2):
        angle = math.pi / 2 + math.pi * i / spikes
        r = outer_r if i % 2 == 0 else inner_r
        pts.append((r * math.cos(angle), r * math.sin(angle)))
    return pts

def make_star_mesh(outer_r=2.0, inner_r=0.9, thickness=0.3, spikes=5, rgba=(0.95, 0.75, 0.15, 1)):
    outline = star_points(outer_r, inner_r, spikes)
    half = thickness * 0.5

    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("star", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    def add_tri(p1, p2, p3, n):
        for p in (p1, p2, p3):
            vertex.addData3(*p)
            normal.addData3(n)
            color.addData4(*rgba)

    tris = GeomTriangles(Geom.UHStatic)
    idx = 0

    for z, nz in ((-half, -1), (half, 1)):
        for i in range(len(outline)):
            j = (i + 1) % len(outline)
            x0, y0 = outline[i]
            x1, y1 = outline[j]
            add_tri((0, 0, z), (x0, y0, z), (x1, y1, z), (0, 0, nz))
            tris.addVertices(idx, idx + 1, idx + 2)
            idx += 3

    for i in range(len(outline)):
        j = (i + 1) % len(outline)
        x0, y0 = outline[i]
        x1, y1 = outline[j]
        p1 = (x0, y0, -half)
        p2 = (x1, y1, -half)
        p3 = (x1, y1, half)
        p4 = (x0, y0, half)
        edge = Vec3(x1 - x0, y1 - y0, 0)
        n = edge.cross(Vec3(0, 0, 1))
        n.normalize()
        for a, b, c in ((p1, p2, p3), (p1, p3, p4)):
            add_tri(a, b, c, (n.x, n.y, n.z))
            tris.addVertices(idx, idx + 1, idx + 2)
            idx += 3

    tris.closePrimitive()
    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("star")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.06, 0.08, 0.12, 1)
        self.disableMouse()
        self.camera.setPos(0, -9, 1)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))
        sun = DirectionalLight("sun")
        sun.setColor((1, 0.95, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(50, -40, 0)
        self.render.setLight(sun_np)

        self.star = self.render.attachNewNode(make_star_mesh())
        self.star.setP(-20)
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.star.setH(self.star.getH() + 45 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
