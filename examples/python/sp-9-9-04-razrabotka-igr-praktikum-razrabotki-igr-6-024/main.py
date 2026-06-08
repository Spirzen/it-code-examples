import pygame
from core.config import SCREEN_WIDTH, UI_HP_BG, UI_HP_FILL, UI_MP_FILL, UI_TEXT


class HUD:
    def __init__(self, renderer) -> None:
        self.r = renderer

    def draw(self, player, floor: int) -> None:
        bar_w = 280
        x, y = 24, 24
        self._bar(x, y, bar_w, 18, player.stats.hp, player.stats.max_hp, UI_HP_FILL, UI_HP_BG)
        self._bar(x, y + 26, bar_w, 14, player.stats.mana, player.stats.max_mana, UI_MP_FILL, (22, 28, 52))
        font = pygame.font.SysFont("Segoe UI", 17, bold=True)
        txt = font.render(f"Ур. {player.experience.level}  ·  Этаж {floor}", True, UI_TEXT)
        self.r.screen.blit(txt, (x, y + 48))

    def _bar(self, x, y, w, h, cur, mx, fill, bg) -> None:
        import pygame
        pygame.draw.rect(self.r.screen, bg, (x, y, w, h), border_radius=4)
        if mx > 0:
            pygame.draw.rect(self.r.screen, fill, (x, y, int(w * cur / mx), h), border_radius=4)
