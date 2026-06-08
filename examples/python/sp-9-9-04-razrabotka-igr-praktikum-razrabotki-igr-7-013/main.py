def _handle_combat_click(self, pos):
    combat = self.run.combat
    if combat is None:
        return
    # 1) хитбоксы врагов из ui.last_enemy_rects
    for i, rect in enumerate(self.ui.last_enemy_rects):
        if rect.collidepoint(pos):
            combat.select_enemy(i)
            return
    # 2) карты
    for i, rect in enumerate(self.ui.last_hand_rects):
        if rect.collidepoint(pos):
            combat.play_card(i, combat.selected_enemy_index)
            return
    # 3) конец хода
    if self.ui.end_turn_rect.collidepoint(pos):
        combat.end_player_turn()
