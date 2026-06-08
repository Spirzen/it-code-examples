self.selected_enemy_index: int | None = None

def card_needs_target(self, card) -> bool:
    return card.type == settings.CARD_ATTACK

def select_enemy(self, index: int):
    living = self.encounter.get_living_enemies()
    if 0 <= index < len(living):
        self.selected_enemy_index = index

def play_card(self, index: int, target_index: int | None = None) -> bool:
    # ...
    if self.card_needs_target(card):
        ti = target_index if target_index is not None else (self.selected_enemy_index or 0)
        living = self.encounter.get_living_enemies()
        target = living[min(ti, len(living) - 1)]
    # ...
