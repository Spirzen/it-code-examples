import pygame
import settings


class UI:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("segoeui", 20)
        self.title_font = pygame.font.SysFont("segoeui", 24, bold=True)

    def draw_combat(self, player, combat):
        self.screen.fill(settings.BG_DARK)
        self._draw_player_panel(player)
        self._draw_enemies(combat.encounter)
        self._draw_hand(player, combat)
        self._draw_log(combat.log)
        end_rect = pygame.Rect(settings.SCREEN_WIDTH - 160, settings.SCREEN_HEIGHT - 56, 140, 40)
        pygame.draw.rect(self.screen, (60, 50, 90), end_rect, border_radius=6)
        label = self.font.render("Конец хода (E)", True, settings.TEXT_WHITE)
        self.screen.blit(label, (end_rect.x + 8, end_rect.y + 10))
        return {"end_turn": end_rect}

    def _draw_player_panel(self, player):
        pygame.draw.rect(self.screen, (28, 24, 48), (24, 24, 280, 120), border_radius=8)
        hp = self.title_font.render(f"HP {player.hp}/{player.max_hp}", True, settings.HP_COLOR)
        en = self.font.render(f"Энергия {player.energy}/{player.max_energy}", True, settings.ENERGY_COLOR)
        bl = self.font.render(f"Броня {player.block}", True, settings.BLOCK_COLOR)
        self.screen.blit(hp, (40, 40))
        self.screen.blit(en, (40, 72))
        self.screen.blit(bl, (40, 96))

    def _draw_hand(self, player, combat):
        cards = player.hand.cards
        if not cards:
            return
        card_w, card_h = 120, 160
        gap = 12
        total_w = len(cards) * card_w + (len(cards) - 1) * gap
        start_x = (settings.SCREEN_WIDTH - total_w) // 2
        y = settings.SCREEN_HEIGHT - card_h - 80
        rects = []
        for i, card in enumerate(cards):
            x = start_x + i * (card_w + gap)
            rect = pygame.Rect(x, y, card_w, card_h)
            can = combat.can_play_card(i)
            color = card.color if can else (50, 50, 60)
            pygame.draw.rect(self.screen, color, rect, border_radius=8)
            pygame.draw.rect(self.screen, (30, 30, 40), rect, 2, border_radius=8)
            name = self.font.render(card.name[:10], True, settings.TEXT_WHITE)
            cost = self.font.render(str(card.cost), True, settings.ENERGY_COLOR)
            self.screen.blit(name, (x + 8, y + 8))
            self.screen.blit(cost, (x + card_w - 24, y + 8))
            rects.append(rect)
        combat._hand_rects = rects  # учебный хак; в эталоне rect хранят в UI

    def _draw_enemies(self, encounter):
        living = encounter.get_living_enemies()
        for i, enemy in enumerate(living):
            x = 400 + i * 200
            pygame.draw.rect(self.screen, (90, 40, 50), (x, 120, 160, 100), border_radius=8)
            nm = self.font.render(enemy.name, True, settings.TEXT_WHITE)
            hp = self.font.render(f"{enemy.hp}/{enemy.max_hp}", True, settings.HP_COLOR)
            intent = self.font.render(f"{enemy.current_intent} {enemy.intent_value}", True, settings.TEXT_GOLD)
            self.screen.blit(nm, (x + 8, 130))
            self.screen.blit(hp, (x + 8, 155))
            self.screen.blit(intent, (x + 8, 180))

    def _draw_log(self, log):
        y = settings.SCREEN_HEIGHT - 200
        for line in log[-5:]:
            surf = self.font.render(line[:70], True, settings.TEXT_WHITE)
            self.screen.blit(surf, (24, y))
            y += 22
