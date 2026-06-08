from dataclasses import dataclass
from entities.entity import Entity


@dataclass
class EnemyEntity(Entity):
    hp: float = 40.0
    max_hp: float = 40.0
    damage: float = 8.0

    def take_damage(self, amount: float) -> None:
        self.hp -= amount
        if self.hp <= 0:
            self.alive = False
