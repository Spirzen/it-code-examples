import json
from dataclasses import dataclass, field
from pathlib import Path
from core.config import BASE_DIR

SAVE_DIR = BASE_DIR / "save_data"


@dataclass
class SaveData:
    floor: int = 1
    kills: int = 0
    player_data: dict = field(default_factory=dict)


class SaveManager:
    def __init__(self) -> None:
        SAVE_DIR.mkdir(parents=True, exist_ok=True)
        self.path = SAVE_DIR / "save.json"

    def exists(self) -> bool:
        return self.path.exists()

    def save(self, data: SaveData) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump({"floor": data.floor, "kills": data.kills, "player": data.player_data},
                      f, ensure_ascii=False, indent=2)

    def load(self) -> SaveData | None:
        if not self.path.exists():
            return None
        with open(self.path, encoding="utf-8") as f:
            raw = json.load(f)
        return SaveData(floor=raw.get("floor", 1), kills=raw.get("kills", 0),
                        player_data=raw.get("player", {}))
