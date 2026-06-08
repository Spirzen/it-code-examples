#!/usr/bin/env python3
"""Spinning image on a card — like main.py, but with a texture."""

import sys
from pathlib import Path

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, CardMaker, DirectionalLight, Filename, TransparencyAttrib


def default_image_path():
    return Path(__file__).resolve().parent / "images" / "sample.png"


def panda_texture_path(path):
    resolved = path.resolve()
    project_dir = Path(__file__).resolve().parent

    try:
        return resolved.relative_to(project_dir).as_posix()
    except ValueError:
        return Filename.fromOsSpecific(str(resolved)).asUnix()


class App(ShowBase):
    def __init__(self, image_path):
        ShowBase.__init__(self)

        self.setBackgroundColor(0.08, 0.1, 0.14, 1)
        self.disableMouse()
        self.camera.setPos(0, -8, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.35, 0.35, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        sun = DirectionalLight("sun")
        sun.setColor((0.9, 0.9, 0.85, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(45, -45, 0)
        self.render.setLight(sun_np)

        texture = self.loader.loadTexture(panda_texture_path(image_path))
        if texture is None:
            sys.exit(f"Cannot load image: {image_path}")

        width = texture.getXSize()
        height = texture.getYSize()
        aspect = width / height if height else 1.0
        half_h = 2.0
        half_w = half_h * aspect

        cm = CardMaker("card")
        cm.setFrame(-half_w, half_w, -half_h, half_h)
        self.card = self.render.attachNewNode(cm.generate())
        self.card.setTexture(texture)
        self.card.setTransparency(TransparencyAttrib.MAlpha)
        self.card.setLightOff()
        self.card.setP(-20)

        self.taskMgr.add(self.spin, "spin")

    def spin(self, task):
        self.card.setH(self.card.getH() + 60 * globalClock.getDt())
        return task.cont


if __name__ == "__main__":
    image = Path(sys.argv[1]) if len(sys.argv) > 1 else default_image_path()
    if not image.is_file():
        sys.exit(f"Image not found: {image}")

    app = App(image)
    app.run()
