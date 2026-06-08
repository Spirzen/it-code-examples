import copy
import json
import os
import settings


class Card:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.name = data["name"]
        self.type = data["type"]
        self.cost = data["cost"]
        self.value = data.get("value", 0)
        self.description = data.get("description", "")
        self.rarity = data.get("rarity", "common")
        self.effect = data.get("effect")
        self.effect_value = data.get("effect_value", 0)

    def copy(self):
        return Card(self.to_dict())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "cost": self.cost,
            "value": self.value,
            "description": self.description,
            "rarity": self.rarity,
            "effect": self.effect,
            "effect_value": self.effect_value,
        }

    @property
    def color(self):
        return settings.CARD_TYPE_COLORS.get(self.type, (80, 80, 100))


def _data_path(filename: str) -> str:
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "data", filename)


def load_card_database() -> list[dict]:
    with open(_data_path("cards.json"), encoding="utf-8") as f:
        return json.load(f)


def create_card(data: dict) -> Card:
    return Card(copy.deepcopy(data))


def create_starting_deck() -> list[Card]:
    db = {c["id"]: c for c in load_card_database()}
    strike = db["strike"]
    defend = db["defend"]
    deck = []
    for _ in range(5):
        deck.append(create_card(strike))
    for _ in range(5):
        deck.append(create_card(defend))
    return deck
