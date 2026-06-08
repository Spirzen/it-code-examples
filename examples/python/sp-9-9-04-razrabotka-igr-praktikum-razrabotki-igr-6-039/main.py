from dataclasses import dataclass, field

from core.config import ATTACK_COOLDOWN, PLAYER_SPEED
from entities.entity import Entity
from player.equipment import Equipment
from player.experience import Experience
from player.inventory import Inventory
from player.stats import Stats


@dataclass
class PlayerEntity(Entity):
    stats: Stats = field(default_factory=Stats)
    experience: Experience = field(default_factory=Experience)
    inventory: Inventory = field(default_factory=Inventory)
    equipment: Equipment = field(default_factory=Equipment)
    move_speed: float = PLAYER_SPEED
    attack_cooldown: float = ATTACK_COOLDOWN
    attack_timer: float = 0.0
    facing_angle: float = 0.0
    is_dashing: bool = False
    dash_timer: float = 0.0
    dash_cooldown_timer: float = 0.0

    @property
    def hp(self) -> float:
        return self.stats.hp

    @property
    def damage(self) -> float:
        return self.stats.damage + self.equipment.bonus("damage")
