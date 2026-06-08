import json
import os
import random

INTENT_ATTACK = "attack"
INTENT_BLOCK = "block"
INTENT_BUFF = "buff"


class Enemy:
    def __init__(self, data: dict, hp_mult: float = 1.0):
        self.name = data["name"]
        self.max_hp = int(data["hp"] * hp_mult)
        self.hp = self.max_hp
        self.block = 0
        self.strength = 0
        self.attack_damage = data.get("attack_damage", 5)
        self.block_value = data.get("block_value", 5)
        self.buff_value = data.get("buff_value", 2)
        self.intent_pattern = data.get("intent_pattern", ["attack"])
        self.intent_index = 0
        self.current_intent = INTENT_ATTACK
        self.intent_value = 0
        self.alive = True
        self._plan_intent()

    def _plan_intent(self):
        key = self.intent_pattern[self.intent_index % len(self.intent_pattern)]
        self.intent_index += 1
        self.current_intent = key
        if key == INTENT_ATTACK:
            self.intent_value = self.attack_damage + self.strength
        elif key == INTENT_BLOCK:
            self.intent_value = self.block_value
        elif key == INTENT_BUFF:
            self.intent_value = self.buff_value

    def execute_intent(self, player):
        if not self.alive:
            return
        if self.current_intent == INTENT_ATTACK:
            player.take_damage(self.intent_value)
        elif self.current_intent == INTENT_BLOCK:
            self.block += self.intent_value
        elif self.current_intent == INTENT_BUFF:
            self.strength += self.intent_value
        self.block = 0
        self._plan_intent()

    def take_damage(self, amount: int) -> int:
        blocked = min(self.block, amount)
        self.block -= blocked
        dmg = amount - blocked
        self.hp = max(0, self.hp - dmg)
        if self.hp <= 0:
            self.alive = False
        return dmg


class Encounter:
    def __init__(self, enemies: list[Enemy]):
        self.enemies = enemies

    def get_living_enemies(self) -> list[Enemy]:
        return [e for e in self.enemies if e.alive]

    def all_dead(self) -> bool:
        return len(self.get_living_enemies()) == 0


def load_enemies() -> list[dict]:
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "data", "enemies.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def create_encounter(enemy_id: str, hp_mult: float = 1.0) -> Encounter:
    db = {e["id"]: e for e in load_enemies()}
    return Encounter([Enemy(db[enemy_id], hp_mult)])
