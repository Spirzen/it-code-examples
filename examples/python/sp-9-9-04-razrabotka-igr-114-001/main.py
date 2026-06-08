import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
x, y = 320, 240

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 4
    if keys[pygame.K_RIGHT]:
        x += 4

    screen.fill((30, 30, 40))
    pygame.draw.rect(screen, (0, 200, 120), (x - 16, y - 16, 32, 32))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
