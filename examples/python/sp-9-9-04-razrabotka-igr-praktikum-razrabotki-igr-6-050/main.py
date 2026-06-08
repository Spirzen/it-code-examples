import math
import random

from core.config import ENEMIES_PER_FLOOR, ENEMY_BASE_DAMAGE, ENEMY_BASE_HP, floor_mult
from entities.enemy import EnemyEntity
from entities.player import PlayerEntity
from world.collision import can_occupy, move_slide
from world.map import GameMap


class AISystem:
    def spawn_enemies(self, game_map: GameMap, floor: int) -> list[EnemyEntity]:
        enemies: list[EnemyEntity] = []
        rng = random.Random(floor * 999)
        scale = floor_mult(floor)
        target = int(ENEMIES_PER_FLOOR * (1 + floor * 0.05))
        attempts = 0
        while len(enemies) < target and attempts < 400:
            attempts += 1
            tx = rng.randint(2, len(game_map.grid[0]) - 3)
            ty = rng.randint(2, len(game_map.grid) - 3)
            wx, wy = tx + 0.5, ty + 0.5
            if not can_occupy(game_map, wx, wy):
                continue
            if (tx, ty) in (game_map.start_tile, game_map.exit_tile):
                continue
            hp = ENEMY_BASE_HP * scale
            dmg = ENEMY_BASE_DAMAGE * scale
            enemies.append(EnemyEntity(wx, wy, hp=hp, max_hp=hp, damage=dmg))
        return enemies

    def update(
        self,
        enemies: list[EnemyEntity],
        player: PlayerEntity,
        game_map: GameMap,
        dt: float,
    ) -> None:
        for enemy in enemies:
            if not enemy.alive:
                continue
            dx, dy = player.x - enemy.x, player.y - enemy.y
            dist = math.hypot(dx, dy)
            if dist < 0.15:
                player.stats.hp -= enemy.damage * dt * 2.5
                continue
            if dist > 0.01:
                speed = 85.0 * dt * 0.012
                mx = (dx / dist) * speed
                my = (dy / dist) * speed
                enemy.x, enemy.y = move_slide(game_map, enemy.x, enemy.y, mx, my)
