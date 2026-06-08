"""Game constants."""

from enum import Enum, auto
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "Pythonablo — этап 1"

ISO_TILE_W = 64
ISO_TILE_H = 32
MAP_WIDTH = 61
MAP_HEIGHT = 46

PLAYER_SPEED = 310.0
ATTACK_COOLDOWN = 0.42
ATTACK_RANGE = 72.0
ATTACK_ARC = 3.14159
ATTACK_DAMAGE_BASE = 18.0

ENEMY_BASE_HP = 40.0
ENEMY_BASE_DAMAGE = 8.0
ENEMIES_PER_FLOOR = 12  # меньше для учебного этапа

XP_BASE = 18
XP_LEVEL_MULT = 1.19
XP_LEVEL_ADD = 5

DASH_DURATION = 0.15
DASH_COOLDOWN = 1.5
DASH_SPEED_MULTIPLIER = 4.5

UI_TEXT = (245, 247, 252)
UI_HP_FILL = (88, 228, 112)
UI_HP_BG = (48, 22, 28)
UI_MP_FILL = (72, 140, 255)


class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()


class TileType(Enum):
    VOID = auto()
    FLOOR = auto()
    WALL = auto()
    START = auto()
    EXIT = auto()
