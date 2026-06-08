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

def make_torus(major_r=2.0, minor_r=0.5, major_seg=32, minor_seg=16, rgba=(0.55, 0.35, 0.85, 1)):
    fmt = GeomVertexFormat.getV3n3c4()
    vdata = GeomVertexData("torus", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    normal = GeomVertexWriter(vdata, "normal")
    color = GeomVertexWriter(vdata, "color")

    def add_vertex(x, y, z, nx, ny, nz):
        vertex.addData3(x, y, z)
        normal.addData3(nx, ny, nz)
        color.addData4(*rgba)

    tris = GeomTriangles(Geom.UHStatic)
    for i in range(major_seg):
        theta0 = 2 * math.pi * i / major_seg
        theta1 = 2 * math.pi * (i + 1) / major_seg
        for j in range(minor_seg):
            phi0 = 2 * math.pi * j / minor_seg
            phi1 = 2 * math.pi * (j + 1) / minor_seg

            def sample(theta, phi):
                cx, sx = math.cos(theta), math.sin(theta)
                cy, sy = math.cos(phi), math.sin(phi)
                x = (major_r + minor_r * cy) * cx
                y = (major_r + minor_r * cy) * sx
                z = minor_r * sy
                nx = cy * cx
                ny = cy * sx
                nz = sy
                return (x, y, z), (nx, ny, nz)

            corners = [sample(theta0, phi0), sample(theta1, phi0), sample(theta1, phi1), sample(theta0, phi1)]
            base = vertex.getWriteRow()
            for (x, y, z), (nx, ny, nz) in corners:
                add_vertex(x, y, z, nx, ny, nz)
            tris.addVertices(base, base + 1, base + 2)
            tris.addVertices(base, base + 2, base + 3)

    tris.closePrimitive()
    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("torus")
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
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        self.torus = self.render.attachNewNode(make_torus())
        self.torus.setP(70)
        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.torus.setH(self.torus.getH() + 35 * globalClock.getDt())
        return task.cont

if __name__ == "__main__":
    App().run()
