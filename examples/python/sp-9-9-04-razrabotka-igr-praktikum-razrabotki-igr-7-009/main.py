import settings
from classes.enemy import Encounter, create_encounter


class CombatManager:
    STATE_PLAYER_TURN = "player_turn"
    STATE_ENEMY_TURN = "enemy_turn"
    STATE_VICTORY = "victory"
    STATE_DEFEAT = "defeat"

    def __init__(self, player, encounter: Encounter):
        self.player = player
        self.encounter = encounter
        self.state = self.STATE_PLAYER_TURN
        self.turn = 0
        self.log: list[str] = []
        self.combat_over = False
        self.victory = False
        self._init_combat()

    def _init_combat(self):
        self.player.reset_combat()
        for card in self.player.deck.draw(settings.STARTING_HAND):
            self.player.hand.add(card)
        self.turn = 1
        self.log.append(f"Бой начался. Ход {self.turn}")

    def can_play_card(self, index: int) -> bool:
        if self.state != self.STATE_PLAYER_TURN:
            return False
        if index < 0 or index >= len(self.player.hand.cards):
            return False
        return self.player.energy >= self.player.hand.cards[index].cost

    def play_card(self, index: int, target_index: int = 0) -> bool:
        if not self.can_play_card(index):
            return False
        card = self.player.hand.cards[index]
        if card.type == settings.CARD_ATTACK:
            living = self.encounter.get_living_enemies()
            if not living:
                return False
            target = living[min(target_index, len(living) - 1)]
        else:
            target = None

        if not self.player.spend_energy(card.cost):
            return False

        self.player.hand.remove(index)

        if card.type == settings.CARD_ATTACK and target:
            dmg = card.value + self.player.strength
            dealt = target.take_damage(dmg)
            self.log.append(f"{card.name}: {dealt} урона → {target.name}")
            if card.effect == "vulnerable" and target.alive:
                target.vulnerable = max(getattr(target, "vulnerable", 0), card.effect_value)
        elif card.type == settings.CARD_BLOCK:
            self.player.gain_block(card.value)
            self.log.append(f"{card.name}: +{card.value} брони")
        elif card.type == settings.CARD_DRAW:
            for c in self.player.deck.draw(card.value):
                self.player.hand.add(c)
            self.log.append(f"{card.name}: добор")

        self.player.deck.discard_all([card])

        if self.encounter.all_dead():
            self._set_victory()
        return True

    def end_player_turn(self):
        if self.state != self.STATE_PLAYER_TURN:
            return
        self.player.end_turn()
        self.state = self.STATE_ENEMY_TURN
        self._enemy_phase()

    def _enemy_phase(self):
        for enemy in self.encounter.get_living_enemies():
            enemy.execute_intent(self.player)
            if self.player.hp <= 0:
                self._set_defeat()
                return
        if self.player.hp <= 0:
            return
        self.turn += 1
        self.player.start_turn()
        for c in self.player.deck.draw(settings.DRAW_PER_TURN):
            self.player.hand.add(c)
        self.state = self.STATE_PLAYER_TURN
        self.log.append(f"Ход {self.turn}. Ваша очередь.")

    def _set_victory(self):
        self.state = self.STATE_VICTORY
        self.combat_over = True
        self.victory = True
        self.log.append("Победа!")

    def _set_defeat(self):
        self.state = self.STATE_DEFEAT
        self.combat_over = True
        self.victory = False
        self.log.append("Поражение…")


def demo_combat_cli():
    from classes.player import Player
    p = Player()
    cm = CombatManager(p, create_encounter("slime"))
    cm.play_card(0, 0)
    cm.end_player_turn()
    for line in cm.log:
        print(line)
    print("HP игрока", p.hp, "враг", cm.encounter.enemies[0].hp)


if __name__ == "__main__":
    demo_combat_cli()
