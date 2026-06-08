import random


class SevenBag:
    """Очередь тетромино по правилу 7-bag."""

    def __init__(self, seed=None):
        self.rng = random.Random(seed)
        self.queue = []
        self._refill()

    def _refill(self):
        bag = ALL_KINDS[:]
        self.rng.shuffle(bag)
        self.queue.extend(bag)

    def pop(self):
        if len(self.queue) < 1:
            self._refill()
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) < 1:
            self._refill()
        return self.queue[0]
