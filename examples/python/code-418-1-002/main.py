"""
Энциклопедия 4.18 — От чисел к картинке (Pygame)
https://spirzen.ru/encyclopedia/4-code-dev/4-18-graphic-dev/1

pip install pygame
"""

import pygame

W, H = 480, 320

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Модель → update → render")
clock = pygame.time.Clock()

# ─── 1. МОДЕЛЬ ───
ball = {
    "x": W / 2,
    "y": H / 2,
    "vx": 140.0,
    "vy": 95.0,
    "radius": 18,
    "color": (239, 68, 68),
}


def update(dt: float) -> None:
    """2. UPDATE — только числа."""
    ball["x"] += ball["vx"] * dt
    ball["y"] += ball["vy"] * dt
    r = ball["radius"]
    if ball["x"] < r or ball["x"] > W - r:
        ball["x"] = max(r, min(W - r, ball["x"]))
        ball["vx"] *= -1
    if ball["y"] < r or ball["y"] > H - r:
        ball["y"] = max(r, min(H - r, ball["y"]))
        ball["vy"] *= -1


def render() -> None:
    """3. RENDER — команды pygame.draw."""
    screen.fill((15, 23, 42))
    pygame.draw.circle(
        screen,
        ball["color"],
        (int(ball["x"]), int(ball["y"])),
        ball["radius"],
    )


running = True
while running:
    # Ввод
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0  # секунды; cap ~60 FPS

    update(dt)
    render()
    pygame.display.flip()  # swap buffers

pygame.quit()
