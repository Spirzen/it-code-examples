import settings
from classes.card import Deck, Hand, create_starting_deck


class Player:
    def __init__(self):
        self.max_hp = settings.STARTING_HP
        self.hp = settings.STARTING_HP
        self.max_energy = settings.STARTING_ENERGY
        self.energy = settings.STARTING_ENERGY
        self.block = 0
        self.strength = 0
        self.vulnerable = 0
        self.deck = Deck(create_starting_deck())
        self.hand = Hand()

    def reset_combat(self):
        self.energy = self.max_energy
        self.block = 0
        self.vulnerable = 0
        self.hand.clear()
        all_cards = self.deck.draw_pile + self.deck.discard_pile
        self.deck = Deck(all_cards)
        self.deck.shuffle()

    def start_turn(self):
        self.energy = self.max_energy
        self.block = 0
        if self.vulnerable > 0:
            self.vulnerable -= 1

    def end_turn(self):
        cards = self.hand.cards[:]
        self.hand.clear()
        self.deck.discard_all(cards)

    def spend_energy(self, cost: int) -> bool:
        if self.energy >= cost:
            self.energy -= cost
            return True
        return False

    def gain_block(self, amount: int):
        self.block += amount

    def take_damage(self, amount: int) -> int:
        if self.vulnerable > 0:
            amount = int(amount * 1.5)
        blocked = min(self.block, amount)
        self.block -= blocked
        damage = amount - blocked
        self.hp = max(0, self.hp - damage)
        return damage

    def apply_vulnerable(self, turns: int):
        self.vulnerable = max(self.vulnerable, turns)
