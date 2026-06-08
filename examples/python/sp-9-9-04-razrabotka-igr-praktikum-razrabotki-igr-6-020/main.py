import random
from core.event_bus import EventBus
from entities.item import GroundItem


class LootSystem:
    DROP_CHANCE = 0.35

    def __init__(self, events: EventBus) -> None:
        self.events = events
        events.subscribe("enemy_killed", self._on_enemy_killed)

    def _on_enemy_killed(self, enemy, killer, **kw) -> None:
        if random.random() > self.DROP_CHANCE:
            return
        item = GroundItem(enemy.x, enemy.y, item_id="potion", label="Зелье HP")
        self.events.emit("item_dropped", item=item)
