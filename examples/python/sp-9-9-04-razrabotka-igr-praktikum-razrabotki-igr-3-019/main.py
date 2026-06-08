import pygame


class Audio:
    def __init__(self):
        self.enabled = True
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            self.hit = pygame.mixer.Sound("assets/hit.wav")
            self.goal = pygame.mixer.Sound("assets/score.wav")
            self.hit.set_volume(0.4)
            self.goal.set_volume(0.5)
        except (pygame.error, FileNotFoundError):
            self.enabled = False

    def play_hit(self):
        if self.enabled:
            self.hit.play()

    def play_goal(self):
        if self.enabled:
            self.goal.play()
