import pygame
import settings
from classes.player import Player
from classes.combat import CombatManager
from classes.enemy import create_encounter
from classes.ui import UI


def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player()
    combat = CombatManager(player, create_encounter("slime"))
    ui = UI(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    combat.end_player_turn()
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if hasattr(combat, "_hand_rects"):
                    for i, rect in enumerate(combat._hand_rects):
                        if rect.collidepoint(event.pos):
                            combat.play_card(i, 0)
        if combat.combat_over:
            running = False
        hitboxes = ui.draw_combat(player, combat)
        pygame.display.flip()
        clock.tick(settings.FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
