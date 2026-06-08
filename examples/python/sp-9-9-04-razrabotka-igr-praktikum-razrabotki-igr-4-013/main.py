from enum import Enum, auto


class State(Enum):
    MENU = auto()
    COUNTDOWN = auto()
    RACING = auto()
    PAUSED = auto()
    FINISHED = auto()


class Game:
    def __init__(self):
        self.state = State.MENU
        self.countdown = 3.0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.state == State.MENU:
                self.state = State.COUNTDOWN
                self.countdown = 3.0
            elif event.key == pygame.K_p and self.state == State.RACING:
                self.state = State.PAUSED
            elif event.key == pygame.K_p and self.state == State.PAUSED:
                self.state = State.RACING

    def update(self, dt):
        if self.state == State.COUNTDOWN:
            self.countdown -= dt
            if self.countdown <= 0:
                self.state = State.RACING
