import pygame
import config as C


class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont("consolas", 22)
        self.font_small = pygame.font.SysFont("consolas", 16)
        self.panel = pygame.Surface((240, 150), pygame.SRCALPHA)
        self.panel.fill((0, 0, 0, 140))

    def draw(self, surface, player, progress, format_time, position=1, total_racers=3):
        surface.blit(self.panel, (8, 8))
        lines = [
            f"P{position}/{total_racers}",
            f"Speed: {abs(player.speed) * 10:.0f} km/h",
            f"Lap: {min(progress.lap + 1, progress.total_laps)}/{progress.total_laps}",
            f"Current: {format_time(progress.current_lap_time)}",
            f"Last: {format_time(progress.last_lap_time)}",
        ]
        if progress.best_lap_time is not None:
            lines.append(f"Best: {format_time(progress.best_lap_time)}")
        y = 14
        for text in lines:
            surf = self.font.render(text, True, (240, 240, 250))
            surface.blit(surf, (16, y))
            y += 22

        hint = "WASD — drive | P pause | R restart | Shift nitro"
        hint_surf = self.font_small.render(hint, True, (200, 200, 210))
        surface.blit(hint_surf, (C.SCREEN_W // 2 - hint_surf.get_width() // 2, C.SCREEN_H - 28))
