class SkidMarks:
    def __init__(self, limit=80):
        self.points = []
        self.limit = limit

    def add(self, x, y, speed, turn_delta):
        if abs(speed) > 5 and abs(turn_delta) > 0.5:
            self.points.append((int(x), int(y)))
            if len(self.points) > self.limit:
                self.points.pop(0)

    def draw(self, surface):
        for i in range(1, len(self.points)):
            pygame.draw.line(surface, (40, 40, 45), self.points[i - 1], self.points[i], 2)
