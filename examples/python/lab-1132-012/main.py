#!/usr/bin/env python3

import pygame
import math
import random
import sys

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Top-down shooter")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super__init__()
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (100, 200, 255), [(16, 0), (32, 28), (0, 28)])
        self.rect = self.image.get_rect(center=(W // 2, H // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        super__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill((255, 240, 80))
        self.rect = self.image.get_rect(center=(x, y))
        self.vx, self.vy = dx * 10, dy * 10

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if not screen.get_rectcolliderect(self.rect):
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super__init__()
        self.image = pygame.Surface((28, 28))
        self.image.fill((220, 80, 80))
        self.rect = self.image.get_rect(
            center=(random.randint(40, W - 40), random.randint(40, H - 40))
        )

    def update(self, target):
        tx, ty = target.rect.center
        ex, ey = self.rect.center
        dx, dy = tx - ex, ty - ey
        length = math.hypot(dx, dy) or 1
        self.rect.x += int(2 * dx / length)
        self.rect.y += int(2 * dy / length)

player = Player()
all_sprites = pygame.sprite.Group(player)
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
score = 0
spawn_cd = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            px, py = player.rect.center
            dx, dy = mx - px, my - py
            length = math.hypot(dx, dy) or 1
            bullet = Bullet(px, py, dx / length, dy / length)
            bullets.add(bullet)
            all_sprites.add(bullet)

    keys = pygame.key.get_pressed()
    player.update(keys)
    bullets.update()
    for enemy in enemies:
        enemy.update(player)

    spawn_cd += 1
    if spawn_cd > 90 and len(enemies) < 8:
        spawn_cd = 0
        e = Enemy()
        enemies.add(e)
        all_sprites.add(e)

    for bullet in bullets:
        hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if hit:
            bullet.kill()
            score += len(hit)

    if pygame.sprite.spritecollide(player, enemies, False):
        running = False

    screen.fill((16, 20, 28))
    all_sprites.draw(screen)
    screen.blit(font.render(f"Счёт: {score}", True, (230, 230, 240)), (12, 12))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
