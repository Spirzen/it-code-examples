package tech.fastj.template

import tech.fastj.engine.Core
import tech.fastj.engine.input.Input
import tech.fastj.graphics.gameobject.GameObject
import tech.fastj.graphics.gameobject.Shape
import tech.fastj.graphics.shape.Rectangle
import tech.fastj.graphics.systems.render.RenderSettings
import tech.fastj.systems.scenes.SimpleScene

class Game {
    static void main(String[] args) {
        Core.init(new MainScene())
        Core.start()
    }
}

class MainScene extends SimpleScene {
    private float playerX = 100f
    private GameObject player

    MainScene() {
        super('main', RenderSettings.DEFAULT)
    }

    @Override
    protected void initScene() {
        player = new GameObject(
            new Shape(new Rectangle(40, 40)),
            this
        )
        player.transform.position.set(playerX, 200f)
        addGameObject(player)
    }

    @Override
    void updateScene() {
        float speed = 200f * Input.getInstance().getLastDelta()
        if (Input.getInstance().isKeyDown('A')) playerX -= speed
        if (Input.getInstance().isKeyDown('D')) playerX += speed
        player.transform.position.setX(playerX)
    }
}
