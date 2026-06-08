import pygame
from core.config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, GameState
from core.event_bus import EventBus
from engine.camera import Camera
from engine.input_handler import InputHandler
from engine.map_renderer import MapRenderer
from engine.renderer import Renderer, screen_to_world
from entities.player import PlayerEntity
from systems.ai_system import AISystem
from systems.combat_system import CombatSystem
from systems.loot_system import LootSystem
from systems.movement_system import MovementSystem
from systems.skill_system import SkillSystem
from ui.hud import HUD
from ui.menu import MenuUI
from world.map import GameMap


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.events = EventBus()
        self.renderer = Renderer(self.screen)
        self.map_renderer = MapRenderer(self.renderer)
        self.camera = Camera()
        self.input = InputHandler()
        self.movement = MovementSystem()
        self.combat = CombatSystem(self.events)
        self.skills = SkillSystem(self.events)
        self.ai = AISystem()
        self.loot = LootSystem(self.events)
        self.hud = HUD(self.renderer)
        self.menu_ui = MenuUI()
        self.state = GameState.MENU
        self.floor = 1
        self.player: PlayerEntity | None = None
        self.game_map: GameMap | None = None
        self.enemies = []
        self.ground_items = []
        self._wire_events()

    def _wire_events(self) -> None:
        self.events.subscribe("item_dropped", lambda item, **_: self.ground_items.append(item))

    def _start_new_game(self) -> None:
        self.floor = 1
        self.game_map = GameMap(floor=self.floor, seed=42)
        self.player = PlayerEntity(
            self.game_map.start_tile[0] + 0.5,
            self.game_map.start_tile[1] + 0.5,
        )
        self.enemies = self.ai.spawn_enemies(self.game_map, self.floor)
        self.ground_items.clear()

    def run(self) -> None:
        while self.running:
            dt = min(self.clock.tick(FPS) / 1000.0, 0.05)
            self._handle_events()
            self._update(dt)
            self._draw()
            pygame.display.flip()
        pygame.quit()

    def _handle_events(self) -> None:
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.input.on_key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.input.on_key_up(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.input.on_mouse_down(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.input.on_mouse_up(event.button)
            elif event.type == pygame.MOTION:
                self.input.on_mouse_motion(event.pos)
        self.input.end_frame()

    def _update(self, dt: float) -> None:
        if self.state == GameState.PLAYING and self.player and self.game_map:
            self._update_playing(dt)

    def _update_playing(self, dt: float) -> None:
        inp = self.input.state
        self.movement.update(self.player, self.game_map, inp, dt)
        self.camera.follow(self.player.x, self.player.y, dt)
        mouse_world = screen_to_world(*inp.mouse_pos, self.camera.x, self.camera.y)
        if inp.attack:
            self.combat.try_attack(self.player, self.enemies, mouse_world)
        if inp.skill_pressed == "fireball":
            self.skills.cast_fireball(self.player, self.enemies, mouse_world)
        self.player.attack_timer = max(0, self.player.attack_timer - dt)
        self.combat.update(dt)
        self.skills.update(dt, self.player, self.enemies)
        self.ai.update(self.enemies, self.player, self.game_map, dt)
        if self.player.stats.hp <= 0:
            self.state = GameState.GAME_OVER

    def _draw(self) -> None:
        self.screen.fill((12, 14, 26))
        if self.state == GameState.MENU:
            self.menu_ui.draw(self.screen)
            return
        if self.game_map and self.player:
            self.map_renderer.draw(self.game_map, self.camera.x, self.camera.y)
            for e in self.enemies:
                if e.alive:
                    self.renderer.draw_entity_circle(e.x, e.y, self.camera.x, self.camera.y, 12, (220, 70, 70))
            self.renderer.draw_entity_circle(
                self.player.x, self.player.y, self.camera.x, self.camera.y, 14, (80, 200, 120))
            self.hud.draw(self.player, self.floor)
