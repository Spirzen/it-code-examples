EFFECT_VULNERABLE = "vulnerable"
EFFECT_WEAK = "weak"
EFFECT_STRENGTH = "strength"
EFFECT_DRAW = "draw"
EFFECT_POISON = "poison"

TARGET_ENEMY = "enemy"
TARGET_SELF = "self"
TARGET_ALL_ENEMIES = "all_enemies"


def collect_card_bonuses(card) -> list[dict]:
    """Собрать effect/effect2 и bonuses[] в единый список."""
    out = []
    if card.effect:
        out.append({"id": card.effect, "value": card.effect_value, "target": TARGET_ENEMY})
    if getattr(card, "effect2", None):
        out.append({"id": card.effect2, "value": card.effect2_value, "target": TARGET_ENEMY})
    for b in getattr(card, "bonuses", []) or []:
        out.append(b)
    return out


def apply_on_play_bonuses(combat, card, target_index, messages: list[str]):
    for bonus in collect_card_bonuses(card):
        _apply_one(combat, bonus, target_index, messages)


def _apply_one(combat, bonus: dict, target_index, messages: list[str]):
    eid = bonus.get("id") or bonus.get("effect")
    value = int(bonus.get("value", 0))
    target = bonus.get("target", TARGET_ENEMY)
    player = combat.player
    living = combat.encounter.get_living_enemies()

    if eid == EFFECT_VULNERABLE and living:
        idx = target_index if target_index is not None else 0
        living[min(idx, len(living) - 1)].vulnerable = max(
            getattr(living[min(idx, len(living) - 1)], "vulnerable", 0), value
        )
        messages.append(f"Уязвимость {value}!")
    elif eid == EFFECT_WEAK and living:
        idx = target_index if target_index is not None else 0
        living[min(idx, len(living) - 1)].weak = value
        messages.append("Слабость!")
    elif eid == EFFECT_STRENGTH:
        player.strength += value
        messages.append(f"+{value} силы")
    elif eid == EFFECT_DRAW:
        for c in player.deck.draw(value):
            player.hand.add(c)
        messages.append(f"Добор {value}")
    elif eid == EFFECT_POISON and living:
        idx = target_index if target_index is not None else 0
        enemy = living[min(idx, len(living) - 1)]
        enemy.poison = getattr(enemy, "poison", 0) + value
        messages.append(f"Яд {value}")
