import math
from dataclasses import dataclass

from core.config import ATTACK_ARC, ATTACK_DAMAGE_BASE
from core.event_bus import EventBus
from entities.enemy import EnemyEntity
from entities.player import PlayerEntity


@dataclass
class SlashEffect:
    x: float
    y: float
    angle: float
    progress: float = 0.0
    duration: float = 0.16


class CombatSystem:
    SLASH_RANGE = 1.95

    def __init__(self, events: EventBus) -> None:
        self.events = events
        self.slashes: list[SlashEffect] = []

    def try_attack(
        self,
        player: PlayerEntity,
        enemies: list[EnemyEntity],
        mouse_world: tuple[float, float],
    ) -> bool:
        if player.attack_timer > 0:
            return False
        dx = mouse_world[0] - player.x
        dy = mouse_world[1] - player.y
        angle = player.facing_angle if abs(dx) < 0.01 and abs(dy) < 0.01 else math.atan2(dy, dx)
        player.facing_angle = angle
        player.attack_timer = player.attack_cooldown
        self.slashes.append(SlashEffect(player.x, player.y, angle))
        self._apply_slash_damage(player, enemies, angle)
        return True

    def _apply_slash_damage(self, player, enemies, angle) -> None:
        damage = player.damage + ATTACK_DAMAGE_BASE * 0.5
        half = ATTACK_ARC / 2
        for enemy in enemies:
            if not enemy.alive:
                continue
            dx, dy = enemy.x - player.x, enemy.y - player.y
            dist = math.hypot(dx, dy)
            if dist > self.SLASH_RANGE + enemy.radius:
                continue
            ea = math.atan2(dy, dx)
            diff = (ea - angle + math.pi) % (2 * math.pi) - math.pi
            if abs(diff) <= half:
                enemy.take_damage(damage)
                if enemy.hp <= 0:
                    enemy.alive = False
                    self.events.emit("enemy_killed", enemy=enemy, killer=player)

    def update(self, dt: float) -> None:
        for slash in self.slashes:
            slash.progress += dt / slash.duration
        self.slashes = [slash for slash in self.slashes if slash.progress < 1.0]
