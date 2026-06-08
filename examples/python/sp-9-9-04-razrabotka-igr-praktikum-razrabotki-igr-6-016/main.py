import math
from dataclasses import dataclass
from core.config import ATTACK_ARC, ATTACK_DAMAGE_BASE
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

    def __init__(self) -> None:
        self.slashes: list[SlashEffect] = []

    def try_attack(self, player: PlayerEntity, enemies: list[EnemyEntity],
                   mouse_world: tuple[float, float]) -> bool:
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

    def update(self, dt: float) -> None:
        for s in self.slashes:
            s.progress += dt / s.duration
        self.slashes = [s for s in self.slashes if s.progress < 1.0]
