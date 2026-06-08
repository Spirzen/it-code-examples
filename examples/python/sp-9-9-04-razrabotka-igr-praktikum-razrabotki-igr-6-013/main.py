import math
from entities.player import PlayerEntity
from engine.input_handler import InputState
from world.collision import move_slide
from world.map import GameMap


class MovementSystem:
    def update(self, player: PlayerEntity, game_map: GameMap, inp: InputState, dt: float) -> None:
        dx = dy = 0.0
        if inp.up:
            dy -= 1
        if inp.down:
            dy += 1
        if inp.left:
            dx -= 1
        if inp.right:
            dx += 1
        if dx or dy:
            length = math.hypot(dx, dy)
            speed = player.move_speed * dt * 0.012
            mx = (dx / length) * speed
            my = (dy / length) * speed
            player.x, player.y = move_slide(game_map, player.x, player.y, mx, my)
            player.facing_angle = math.atan2(dy, dx)
