import settings
from classes.player import Player
from classes.combat import CombatManager
from classes.enemy import create_encounter


class RunState:
    SCREEN_MENU = "menu"
    SCREEN_COMBAT = "combat"
    SCREEN_MAP = "map"

    def __init__(self):
        self.screen = self.SCREEN_MENU
        self.player = Player()
        self.combat: CombatManager | None = None

    def start_debug_combat(self):
        self.player = Player()
        self.combat = CombatManager(self.player, create_encounter("slime"))
        self.screen = self.SCREEN_COMBAT

    def return_menu(self):
        self.screen = self.SCREEN_MENU
        self.combat = None
