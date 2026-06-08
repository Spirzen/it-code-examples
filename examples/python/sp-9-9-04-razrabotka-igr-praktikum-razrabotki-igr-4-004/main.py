def draw_track(surface):
    outer = pygame.Rect(
        C.TRACK_CX - C.OUTER_RX,
        C.TRACK_CY - C.OUTER_RY,
        C.OUTER_RX * 2,
        C.OUTER_RY * 2,
    )
    inner = pygame.Rect(
        C.TRACK_CX - C.INNER_RX,
        C.TRACK_CY - C.INNER_RY,
        C.INNER_RX * 2,
        C.INNER_RY * 2,
    )
    pygame.draw.ellipse(surface, C.COLOR_ASPHALT, outer)
    pygame.draw.ellipse(surface, C.COLOR_LAWN, inner)
    pygame.draw.ellipse(surface, C.COLOR_LINE, outer, 3)
    pygame.draw.ellipse(surface, C.COLOR_LINE, inner, 2)
    draw_start_line(surface)


def draw_start_line(surface):
    """Шахматная черта на нижней дуге — старт/финиш."""
    y = C.TRACK_CY + (C.INNER_RY + C.OUTER_RY) // 2
    x0 = C.TRACK_CX - 36
    square = 8
    for i in range(9):
        color = (255, 255, 255) if i % 2 == 0 else (20, 20, 20)
        pygame.draw.rect(surface, color, (x0 + i * square, y - 6, square, 12))
    pygame.draw.line(surface, (255, 220, 0), (x0 - 4, y), (x0 + 9 * square + 4, y), 2)
