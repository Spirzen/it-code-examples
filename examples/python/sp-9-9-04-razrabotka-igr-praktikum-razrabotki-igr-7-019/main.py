def editor_data_to_card_dict(data: dict) -> dict:
    effect = data.get("effect", "damage")
    kind = data.get("kind", "spell")
    card_type = "creature" if kind == "creature" else {
        "damage": "attack", "block": "block", "buff": "buff",
        "debuff": "debuff", "draw": "draw",
    }[effect]
    return {
        "id": data.get("id") or f"custom_{uuid.uuid4().hex[:8]}",
        "name": data.get("name", "Без названия"),
        "type": card_type,
        "cost": int(data.get("cost", 1)),
        "value": int(data.get("damage", 0)),
        "health": int(data.get("health", 0)),
        "description": data.get("description", ""),
        "rarity": "custom",
        "custom": True,
        "kind": kind,
    }
