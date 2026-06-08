BG_TOP = (18, 12, 40)
BG_BOT = (8, 20, 50)
FRAME_OUTER = (90, 60, 140)
FRAME_INNER = (140, 100, 200)
FRAME_HIGHLIGHT = (200, 170, 255)


def lerp_color(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def make_gradient_bg(w, h):
    surf = pygame.Surface((w, h))
    for y in range(h):
        t = y / max(1, h - 1)
        c = lerp_color(BG_TOP, BG_BOT, t)
        pygame.draw.line(surf, c, (0, y), (w, y))
    return surf


def make_board_frame(w, h):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    outer = pygame.Rect(0, 0, w, h)
    inner = outer.inflate(-FRAME * 2, -FRAME * 2)
    shadow = outer.move(0, 6)
    pygame.draw.rect(surf, (0, 0, 0, 80), shadow, border_radius=22)
    pygame.draw.rect(surf, FRAME_OUTER, outer, border_radius=20)
    pygame.draw.rect(surf, FRAME_INNER, outer.inflate(-4, -4), border_radius=18)
    hi = pygame.Rect(outer.x + 8, outer.y + 6, outer.w - 16, 8)
    pygame.draw.rect(surf, (*FRAME_HIGHLIGHT, 60), hi, border_radius=4)
    pygame.draw.rect(surf, (30, 22, 55), inner, border_radius=14)
    pygame.draw.rect(surf, (50, 35, 80), inner, width=2, border_radius=14)
    return surf


BG_SURFACE = make_gradient_bg(WIDTH, HEIGHT)
FRAME_SURFACE = make_board_frame(BOARD_W, BOARD_H)
