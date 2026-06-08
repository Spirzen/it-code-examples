#!/usr/bin/env python3

from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -8, 2)
        self.camera.lookAt(0, 0, 0)

if __name__ == "__main__":
    app = App()
    app.run()
