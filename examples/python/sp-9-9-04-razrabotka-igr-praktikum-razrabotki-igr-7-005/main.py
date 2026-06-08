import random
import settings


class Deck:
    def __init__(self, cards: list[Card] | None = None):
        self.draw_pile: list[Card] = list(cards or [])
        self.discard_pile: list[Card] = []
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.draw_pile)

    def draw(self, count: int = 1) -> list[Card]:
        drawn = []
        for _ in range(count):
            if not self.draw_pile and self.discard_pile:
                self.draw_pile = self.discard_pile[:]
                self.discard_pile.clear()
                self.shuffle()
            if self.draw_pile:
                drawn.append(self.draw_pile.pop())
        return drawn

    def discard_all(self, cards: list[Card]):
        self.discard_pile.extend(cards)


class Hand:
    def __init__(self, max_size: int = settings.MAX_HAND):
        self.cards: list[Card] = []
        self.max_size = max_size

    def add(self, card: Card) -> bool:
        if len(self.cards) >= self.max_size:
            return False
        self.cards.append(card)
        return True

    def remove(self, index: int) -> Card | None:
        if 0 <= index < len(self.cards):
            return self.cards.pop(index)
        return None

    def clear(self):
        self.cards.clear()
