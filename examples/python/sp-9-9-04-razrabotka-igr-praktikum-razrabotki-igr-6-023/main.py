import math
from dataclasses import dataclass
from core.event_bus import EventBus
from entities.enemy import EnemyEntity
from entities.player import PlayerEntity


@dataclass
class Projectile:
    x: float
    y: float
    vx: float
    vy: float
    damage: float
    life: float = 2.0
    radius: float = 0.25


class SkillSystem:
    MANA_COST = 15.0

    def __init__(self, events: EventBus) -> None:
        self.events = events
        self.projectiles: list[Projectile] = []

    def cast_fireball(self, player: PlayerEntity, enemies: list[EnemyEntity],
                      target: tuple[float, float]) -> bool:
        if player.stats.mana < self.MANA_COST:
            return False
        player.stats.mana -= self.MANA_COST
        dx, dy = target[0] - player.x, target[1] - player.y
        dist = math.hypot(dx, dy) or 1.0
        speed = 14.0
        self.projectiles.append(Projectile(
            player.x, player.y, dx / dist * speed, dy / dist * speed,
            damage=player.damage * 1.4,
        ))
        self.events.emit("skill_cast", skill="fireball")
        return True

    def update(self, dt: float, player: PlayerEntity, enemies: list[EnemyEntity]) -> None:
        for p in self.projectiles:
            p.x += p.vx * dt
            p.y += p.vy * dt
            p.life -= dt
            for enemy in enemies:
                if not enemy.alive:
                    continue
                dist = math.hypot(enemy.x - p.x, enemy.y - p.y)
                if dist < p.radius + enemy.radius:
                    enemy.take_damage(p.damage)
                    p.life = 0
                    if enemy.hp <= 0:
                        enemy.alive = False
                        self.events.emit("enemy_killed", enemy=enemy, killer=player)
        self.projectiles = [p for p in self.projectiles if p.life > 0]
