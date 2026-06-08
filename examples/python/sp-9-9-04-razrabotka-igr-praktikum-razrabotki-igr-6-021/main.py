from dataclasses import dataclass, field


@dataclass
class Equipment:
    weapon: str | None = None
    chest: str | None = None
    _bonuses: dict[str, float] = field(default_factory=dict)

    def equip(self, item_id: str, slot: str, bonuses: dict[str, float]) -> None:
        setattr(self, slot, item_id)
        for k, v in bonuses.items():
            self._bonuses[k] = self._bonuses.get(k, 0) + v

    def bonus(self, name: str) -> float:
        return self._bonuses.get(name, 0.0)
