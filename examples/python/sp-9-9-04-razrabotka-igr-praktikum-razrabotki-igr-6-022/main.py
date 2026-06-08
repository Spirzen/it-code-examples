def draw_inventory_overlay(screen, player) -> None:
    import pygame
    overlay = pygame.Surface((520, 420), pygame.SRCALPHA)
    overlay.fill((12, 14, 26, 220))
    ox = (SCREEN_WIDTH - 520) // 2
    oy = (SCREEN_HEIGHT - 420) // 2
    screen.blit(overlay, (ox, oy))
    font = pygame.font.SysFont("Segoe UI", 16)
    for i, slot in enumerate(player.inventory.slots[:12]):
        col, row = i % 4, i // 4
        x, y = ox + 24 + col * 118, oy + 48 + row * 72
        pygame.draw.rect(screen, (40, 48, 72), (x, y, 100, 60), border_radius=6)
        if slot:
            label = font.render(slot, True, UI_TEXT)
            screen.blit(label, (x + 8, y + 20))
