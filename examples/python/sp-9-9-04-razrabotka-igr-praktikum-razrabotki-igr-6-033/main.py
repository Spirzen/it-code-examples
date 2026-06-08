import pygame

from core.config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, GameState
from core.event_bus import EventBus
from engine.camera import Camera
from engine.input_handler import InputHandler
from engine.map_renderer import MapRenderer
from engine.renderer import Renderer, screen_to_world
from entities.item import GroundItem
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
        self.menu_selected = 0
        self.show_inventory = False
        self.floor = 1
        self.player: PlayerEntity | None = None
        self.game_map: GameMap | None = None
        self.enemies = []
        self.ground_items: list[GroundItem] = []
        self._wire_events()

    def _wire_events(self) -> None:
        self.events.subscribe("item_dropped", self._on_item_dropped)
        self.events.subscribe("enemy_killed", self._on_enemy_killed)

    def _on_item_dropped(self, item: GroundItem, **_) -> None:
        self.ground_items.append(item)

    def _on_enemy_killed(self, enemy, killer, **_) -> None:
        if killer is None or self.player is None or self.game_map is None:
            return
        xp = 12 + self.game_map.floor * 2
        ups = killer.experience.add_xp(xp)
        for _ in range(ups):
            killer.stats.on_level_up()
        self.events.emit("level_up", player=killer, levels=ups)

    def _start_new_game(self) -> None:
        self.floor = 1
        self.game_map = GameMap(floor=self.floor, seed=42)
        self.player = PlayerEntity(
            self.game_map.start_tile[0] + 0.5,
            self.game_map.start_tile[1] + 0.5,
        )
        self.enemies = self.ai.spawn_enemies(self.game_map, self.floor)
        self.ground_items.clear()
        self.show_inventory = False

    def _try_use_portal(self) -> None:
        if not self.game_map or not self.player:
            return
        ex, ey = self.game_map.exit_tile
        if self.player.distance_sq_to(ex + 0.5, ey + 0.5) > 1.85**2:
            return
        self.floor += 1
        self.game_map = GameMap(floor=self.floor, seed=1000 + self.floor)
        self.player.x = self.game_map.start_tile[0] + 0.5
        self.player.y = self.game_map.start_tile[1] + 0.5
        self.enemies = self.ai.spawn_enemies(self.game_map, self.floor)
        self.ground_items.clear()

    def _try_interact(self) -> None:
        if not self.player:
            return
        if self.game_map and self._near_portal():
            self._try_use_portal()
            return
        for item in list(self.ground_items):
            if self.player.distance_to(item) < 1.2:
                if item.item_id == "potion":
                    self.player.stats.hp = min(self.player.stats.max_hp, self.player.stats.hp + 40)
                elif item.item_id == "sword_1":
                    if self.player.inventory.add("sword_1"):
                        self.player.equipment.equip("sword_1", "weapon", {"damage": 8.0})
                self.ground_items.remove(item)
                break

    def _near_portal(self) -> bool:
        if not self.game_map or not self.player:
            return False
        ex, ey = self.game_map.exit_tile
        return self.player.distance_sq_to(ex + 0.5, ey + 0.5) <= 1.85**2

    def run(self) -> None:
        while self.running:
            dt = min(self.clock.tick(FPS) / 1000.0, 0.05)
            self._handle_events()
            self._update(dt)
            self._draw()
            pygame.display.flip()
        pygame.quit()

    def _handle_events(self) -> None:
        inp = self.input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                inp.on_key_down(event.key)
            elif event.type == pygame.KEYUP:
                inp.on_key_up(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                inp.on_mouse_down(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                inp.on_mouse_up(event.button)
            elif event.type == pygame.MOTION:
                inp.on_mouse_motion(event.pos)

        state = inp.state
        if self.state == GameState.MENU:
            if state.menu_up:
                self.menu_selected = (self.menu_selected - 1) % 2
            if state.menu_down:
                self.menu_selected = (self.menu_selected + 1) % 2
            if state.menu_confirm:
                if self.menu_selected == 0:
                    self._start_new_game()
                    self.state = GameState.PLAYING
                else:
                    self.running = False
        elif self.state == GameState.PLAYING:
            if state.menu_back:
                self.state = GameState.PAUSED
            if state.inventory_pressed:
                self.show_inventory = not self.show_inventory
        elif self.state == GameState.PAUSED:
            if state.menu_back:
                self.state = GameState.PLAYING
        elif self.state == GameState.GAME_OVER:
            if state.menu_back:
                self.state = GameState.MENU
                self.menu_selected = 0

        inp.end_frame()

    def _update(self, dt: float) -> None:
        if self.state == GameState.PLAYING and self.player and self.game_map:
            self._update_playing(dt)

    def _update_playing(self, dt: float) -> None:
        assert self.player and self.game_map
        inp = self.input.state

        if inp.dash_pressed:
            self.movement.try_dash(self.player, self.game_map, inp)

        self.movement.update(self.player, self.game_map, inp, dt)
        self.camera.follow(self.player.x, self.player.y, dt)
        mouse_world = screen_to_world(*inp.mouse_pos, self.camera.x, self.camera.y)

        if inp.attack:
            self.combat.try_attack(self.player, self.enemies, mouse_world)
        if inp.skill_pressed == "fireball":
            self.skills.cast_fireball(self.player, self.enemies, mouse_world)
        if inp.interact_pressed:
            self._try_interact()

        self.player.attack_timer = max(0, self.player.attack_timer - dt)
        self.player.stats.mana = min(self.player.stats.max_mana, self.player.stats.mana + 8 * dt)

        self.combat.update(dt)
        self.skills.update(dt, self.player, self.enemies)
        self.ai.update(self.enemies, self.player, self.game_map, dt)

        if self.player.stats.hp <= 0:
            self.state = GameState.GAME_OVER

    def _draw(self) -> None:
        self.screen.fill((12, 14, 26))

        if self.state == GameState.MENU:
            self.menu_ui.draw(self.screen, self.menu_selected)
            return

        if self.game_map and self.player:
            self.map_renderer.draw(self.game_map, self.camera.x, self.camera.y)
            for item in self.ground_items:
                self.renderer.draw_ground_item(item, self.camera.x, self.camera.y)
            for enemy in self.enemies:
                if enemy.alive:
                    self.renderer.draw_entity_circle(
                        enemy.x,
                        enemy.y,
                        self.camera.x,
                        self.camera.y,
                        12,
                        (220, 70, 70),
                    )
                    self.renderer.draw_enemy_hp(enemy, self.camera.x, self.camera.y)
            for slash in self.combat.slashes:
                self.renderer.draw_slash(slash, self.camera.x, self.camera.y)
            for projectile in self.skills.projectiles:
                self.renderer.draw_projectile(projectile, self.camera.x, self.camera.y)
            self.renderer.draw_entity_circle(
                self.player.x,
                self.player.y,
                self.camera.x,
                self.camera.y,
                14,
                (80, 200, 120),
            )

            portal_hint = "E — портал" if self._near_portal() else None
            self.hud.draw(self.player, self.floor, portal_hint)

            if self.show_inventory:
                self._draw_inventory_overlay()

        if self.state == GameState.PAUSED:
            self.menu_ui.draw_pause(self.screen)
        elif self.state == GameState.GAME_OVER:
            self.menu_ui.draw_game_over(self.screen)

    def _draw_inventory_overlay(self) -> None:
        from core.config import SCREEN_HEIGHT, SCREEN_WIDTH, UI_TEXT

        assert self.player
        overlay = pygame.Surface((520, 420), pygame.SRCALPHA)
        overlay.fill((12, 14, 26, 220))
        ox = (SCREEN_WIDTH - 520) // 2
        oy = (SCREEN_HEIGHT - 420) // 2
        self.screen.blit(overlay, (ox, oy))
        font = pygame.font.SysFont("Segoe UI", 16)
        title = font.render("Инвентарь (I — закрыть)", True, UI_TEXT)
        self.screen.blit(title, (ox + 24, oy + 16))
        for i, slot in enumerate(self.player.inventory.slots[:12]):
            col, row = i % 4, i // 4
            x, y = ox + 24 + col * 118, oy + 48 + row * 72
            pygame.draw.rect(self.screen, (40, 48, 72), (x, y, 100, 60), border_radius=6)
            if slot:
                label = font.render(slot, True, UI_TEXT)
                self.screen.blit(label, (x + 8, y + 20))
