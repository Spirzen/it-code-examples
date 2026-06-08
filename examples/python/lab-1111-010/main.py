#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.06, 0.07, 0.1, 1)
        self.disableMouse()
        self.camera.setPos(0, -14, 10)
        self.camera.lookAt(0, 0, 0)

        size = 1.4
        gap = 0.15
        step = size + gap
        colors = [
            (0.9, 0.3, 0.3, 1), (0.3, 0.85, 0.45, 1), (0.35, 0.55, 0.95, 1),
            (0.95, 0.75, 0.2, 1), (0.75, 0.4, 0.9, 1), (0.3, 0.85, 0.85, 1),
        ]

        idx = 0
        for row in range(3):
            for col in range(4):
                cm = CardMaker(f"tile_{row}_{col}")
                cm.setFrame(-size / 2, size / 2, -size / 2, size / 2)
                tile = self.render.attachNewNode(cm.generate())
                tile.setPos((col - 1.5) * step, (row - 1) * step, 0)
                tile.setColor(*colors[idx % len(colors)])
                tile.setLightOff()
                idx += 1

        self.render.setP(-55)

if __name__ == "__main__":
    App().run()
