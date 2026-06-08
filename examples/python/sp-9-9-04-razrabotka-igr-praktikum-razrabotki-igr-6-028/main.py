import json
from core.config import DATA_DIR

def _load_templates(self) -> list[dict]:
    path = DATA_DIR / "enemies.json"
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("enemies", [])

def _pick_template(self, templates: list[dict]) -> dict | None:
    if not templates:
        return None
    weights = [t.get("weight", 1) for t in templates]
    return self.rng.choices(templates, weights=weights, k=1)[0]

def _make_enemy(self, wx, wy, floor, tmpl) -> EnemyEntity:
    scale = 1.0 + floor * 0.08
    hp = (tmpl["base_hp"] if tmpl else ENEMY_BASE_HP) * scale
    return EnemyEntity(wx, wy, hp=hp, max_hp=hp,
                       damage=tmpl["base_damage"] if tmpl else 8.0)
