class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.save = SaveSystem()
        self.run = RunState(self.save)
        self.ui = UI(self.screen)
        self.running = True

    def run_loop(self):
        while self.running:
            dt = self.clock.tick(settings.FPS)
            for event in pygame.event.get():
                self._handle_event(event)
            self._update(dt)
            self._draw()
            pygame.display.flip()
        pygame.quit()
