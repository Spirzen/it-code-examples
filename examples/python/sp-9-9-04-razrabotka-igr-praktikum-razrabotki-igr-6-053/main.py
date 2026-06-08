import pygame

from core.config import SCREEN_HEIGHT, SCREEN_WIDTH, UI_HP_BG, UI_HP_FILL, UI_MP_FILL, UI_TEXT


class HUD:
    def __init__(self, renderer) -> None:
        self.r = renderer

    def draw(self, player, floor: int, portal_hint: str | None = None) -> None:
        bar_w = 280
        x, y = 24, 24
        self._bar(x, y, bar_w, 18, player.stats.hp, player.stats.max_hp, UI_HP_FILL, UI_HP_BG)
        self._bar(
            x,
            y + 26,
            bar_w,
            14,
            player.stats.mana,
            player.stats.max_mana,
            UI_MP_FILL,
            (22, 28, 52),
        )
        font = pygame.font.SysFont("Segoe UI", 17, bold=True)
        txt = font.render(f"Ур. {player.experience.level}  ·  Этаж {floor}", True, UI_TEXT)
        self.r.screen.blit(txt, (x, y + 48))
        self.draw_skill_bar(player, portal_hint)

    def _bar(self, x, y, w, h, cur, mx, fill, bg) -> None:
        pygame.draw.rect(self.r.screen, bg, (x, y, w, h), border_radius=4)
        if mx > 0:
            pygame.draw.rect(self.r.screen, fill, (x, y, int(w * cur / mx), h), border_radius=4)

    def draw_skill_bar(self, player, portal_hint: str | None) -> None:
        font = pygame.font.SysFont("Segoe UI", 14)
        pygame.draw.circle(self.r.screen, (255, 120, 40), (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40), 18)
        label = font.render("F", True, UI_TEXT)
        self.r.screen.blit(label, (SCREEN_WIDTH - 86, SCREEN_HEIGHT - 48))
        if portal_hint:
            hint = font.render(portal_hint, True, (255, 204, 96))
            self.r.screen.blit(hint, (24, SCREEN_HEIGHT - 32))
