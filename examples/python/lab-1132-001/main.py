#!/usr/bin/env python3

import pygame
import sys

pygame.init()  # запуск видео, звука, ввода
screen = pygame.display.set_mode((800, 600))  # окно 800×600, surface для рисования
pygame.display.set_caption("Мини-игра")
clock = pygame.time.Clock()  # таймер кадров
FPS = 60

running = True
while running:
    # 1) Ввод пользователя
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # крестик окна
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # 2) Логика: координаты, счёт, столкновения

    # 3) Рисование
    screen.fill((20, 24, 32))  # цвет фона RGB
    # pygame.draw.. / blit спрайтов

    pygame.display.flip()  # показать нарисованный кадр
    clock.tick(FPS)  # подождать до следующего кадра

pygame.quit()
sys.exit()
