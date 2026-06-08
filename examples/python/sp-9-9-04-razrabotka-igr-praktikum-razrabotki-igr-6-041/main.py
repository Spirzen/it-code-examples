from dataclasses import dataclass


@dataclass
class Stats:
    max_hp: float = 150.0
    hp: float = 150.0
    max_mana: float = 80.0
    mana: float = 80.0
    damage: float = 18.0
    vitality: int = 10

    def on_level_up(self) -> None:
        self.vitality += 2
        self.max_hp += 12
        self.hp = self.max_hp
        self.max_mana += 6
        self.mana = self.max_mana
        self.damage += 2
