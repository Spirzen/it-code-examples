#!/usr/bin/env python3

import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Geom, GeomNode, GeomTriangles, GeomVertexData, GeomVertexFormat, GeomVertexWriter, Vec3

def make_filled_polygon(n, radius, rgba=(0.9, 0.4, 0.2, 1)):
    if n < 3:
        raise ValueError("n >= 3")
    fmt = GeomVertexFormat.getV3c4()
    vdata = GeomVertexData("poly", fmt, Geom.UHStatic)
    vertex = GeomVertexWriter(vdata, "vertex")
    color = GeomVertexWriter(vdata, "color")

    vertex.addData3(0, 0, 0)
    color.addData4(*rgba)
    for i in range(n):
        angle = 2 * math.pi * i / n
        vertex.addData3(radius * math.cos(angle), radius * math.sin(angle), 0)
        color.addData4(*rgba)

    tris = GeomTriangles(Geom.UHStatic)
    for i in range(n):
        tris.addVertices(0, i + 1, (i % n) + 2 if i < n - 1 else 1)
    tris.closePrimitive()

    geom = Geom(vdata)
    geom.addPrimitive(tris)
    node = GeomNode("filled_poly")
    node.addGeom(geom)
    return node

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -10, 0)
        self.camera.lookAt(0, 0, 0)

        for i, sides in enumerate((5, 7, 9)):
            poly = self.render.attachNewNode(make_filled_polygon(sides, 2.0 - i * 0.3))
            poly.setPos(0, i * 3 - 3, 0)
            poly.setLightOff()
            poly.setColor(0.3 + i * 0.2, 0.5, 0.9 - i * 0.15, 1)

if __name__ == "__main__":
    App().run()
