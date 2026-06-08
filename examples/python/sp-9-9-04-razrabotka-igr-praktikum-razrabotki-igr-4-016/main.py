import math
import time
import pygame
from enum import Enum, auto

import config as C
from game.car import Car
from game.track import Track
from game.progress import RaceProgress
from game.ai import build_oval_waypoints, WaypointFollower
from game.hud import HUD


class State(Enum):
    MENU = auto()
    COUNTDOWN = auto()
    RACING = auto()
    PAUSED = auto()
    FINISHED = auto()


def format_time(seconds):
    if seconds <= 0:
        return "00:00.000"
    ms = int((seconds % 1) * 1000)
    s = int(seconds) % 60
    m = int(seconds) // 60
    return f"{m:02d}:{s:02d}.{ms:03d}"


class Game:
    def __init__(self):
        self.state = State.MENU
        self.countdown = 3.0
        self.track = Track()
        self.hud = HUD()
        self.font_big = pygame.font.SysFont("consolas", 36)
        self.font = pygame.font.SysFont("consolas", 22)
        self._build_race()

    def _start_position(self):
        y = C.TRACK_CY + (C.INNER_RY + C.OUTER_RY) // 2
        return C.TRACK_CX, y

    def _build_race(self):
        sx, sy = self._start_position()
        self.player = Car(sx, sy, -90, (220, 50, 50))
        self.progress = RaceProgress(sx, sy)
        wps = build_oval_waypoints()
        self.rivals = [
            WaypointFollower(Car(sx + 80, sy, -90, (50, 120, 220)), wps, speed=4.0),
            WaypointFollower(Car(sx - 60, sy, -90, (220, 180, 50)), wps, speed=4.5),
        ]
        for i, rival in enumerate(self.rivals):
            rival.index = (i * 8) % len(wps)

    def reset_race(self):
        self._build_race()
        self.state = State.COUNTDOWN
        self.countdown = 3.0

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_RETURN and self.state == State.MENU:
            self.reset_race()
        elif event.key == pygame.K_r and self.state in (State.RACING, State.FINISHED, State.PAUSED):
            self.reset_race()
        elif event.key == pygame.K_p and self.state == State.RACING:
            self.state = State.PAUSED
        elif event.key == pygame.K_p and self.state == State.PAUSED:
            self.state = State.RACING

    def update(self, dt):
        if self.state == State.COUNTDOWN:
            self.countdown -= dt
            if self.countdown <= 0:
                self.state = State.RACING
            return
        if self.state != State.RACING:
            return

        keys = pygame.key.get_pressed()
        self.player.apply_input(keys)
        self.player.steer(keys)
        self.player.move()
        self.track.clamp_car(self.player)
        self.progress.update(self.player.x, self.player.y)

        for rival in self.rivals:
            rival.update()
            self.track.clamp_car(rival.car)
            self.player.collide_with(rival.car)

        if self.progress.finished:
            self.state = State.FINISHED

    def draw(self, surface):
        surface.fill(C.COLOR_GRASS)
        self.track.draw(surface)
        for rival in self.rivals:
            rival.car.draw(surface)
        self.player.draw(surface)
        self.hud.draw(surface, self.player, self.progress, format_time)

        if self.state == State.MENU:
            t = self.font_big.render("Racing", True, (255, 255, 255))
            hint = self.font.render("Enter — старт, Esc — выход", True, (200, 200, 210))
            surface.blit(t, t.get_rect(center=(C.SCREEN_W // 2, C.SCREEN_H // 2 - 30)))
            surface.blit(hint, hint.get_rect(center=(C.SCREEN_W // 2, C.SCREEN_H // 2 + 20)))
        elif self.state == State.COUNTDOWN:
            n = max(1, int(self.countdown + 0.99))
            text = self.font_big.render(str(n), True, (255, 220, 0))
            surface.blit(text, text.get_rect(center=(C.SCREEN_W // 2, C.SCREEN_H // 2)))
        elif self.state == State.PAUSED:
            text = self.font_big.render("PAUSE", True, (255, 255, 255))
            surface.blit(text, text.get_rect(center=(C.SCREEN_W // 2, C.SCREEN_H // 2)))
        elif self.state == State.FINISHED:
            msg = self.font_big.render("FINISH!", True, (100, 255, 120))
            best = ""
            if self.progress.best_lap_time:
                best = f"Best lap: {format_time(self.progress.best_lap_time)}"
            sub = self.font.render(best + "  R — заново", True, (230, 230, 240))
            surface.blit(msg, msg.get_rect(center=(C.SCREEN_W // 2, C.SCREEN_H // 2 - 20)))
            surface.blit(sub, sub.get_rect(center=(C.SCREEN_W // 2, C.SCREEN_H // 2 + 24)))
