#!/usr/bin/env python3
"""Крестики-нолики 3×3 на Pygame: игрок (X) против эвристического ИИ (O)."""

from __future__ import annotations

import pygame
import sys
from typing import List, Optional, Tuple

pygame.init()

WIDTH, HEIGHT = 480, 560
BOARD_SIZE = 3
CELL = 120
OFFSET_X = (WIDTH - CELL * BOARD_SIZE) // 2
OFFSET_Y = 100
FPS = 60

BG = (18, 22, 36)
GRID = (90, 100, 140)
X_COLOR = (255, 120, 120)
O_COLOR = (120, 200, 255)
TEXT = (230, 230, 240)
WIN_LINE = (255, 220, 80)

PlayerMark = str  # "X" | "O"
Cell = Optional[PlayerMark]


class Board:
    def __init__(self, size: int = BOARD_SIZE) -> None:
        self.size = size
        self.cells: List[List[Cell]] = [[None] * size for _ in range(size)]

    def reset(self) -> None:
        self.cells = [[None] * self.size for _ in range(self.size)]

    def empty_cells(self) -> List[Tuple[int, int]]:
        return [
            (row, col)
            for row in range(self.size)
            for col in range(self.size)
            if self.cells[row][col] is None
        ]

    def place(self, row: int, col: int, mark: PlayerMark) -> bool:
        if self.cells[row][col] is not None:
            return False
        self.cells[row][col] = mark
        return True

    def winner(self) -> Optional[PlayerMark]:
        n = self.size
        lines = []
        lines.extend(self.cells)
        lines.extend([[self.cells[r][c] for r in range(n)] for c in range(n)])
        lines.append([self.cells[i][i] for i in range(n)])
        lines.append([self.cells[i][n - i - 1] for i in range(n)])
        for line in lines:
            if line[0] is not None and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_full(self) -> bool:
        return not self.empty_cells()


def would_win(board: Board, row: int, col: int, mark: PlayerMark) -> bool:
    board.place(row, col, mark)
    won = board.winner() == mark
    board.cells[row][col] = None
    return won


def choose_ai_move(board: Board, ai: PlayerMark = "O", human: PlayerMark = "X") -> Tuple[int, int]:
    empty = board.empty_cells()
    if not empty:
        raise ValueError("no empty cells")

    # 1. Выиграть, если можем
    for row, col in empty:
        if would_win(board, row, col, ai):
            return row, col

    # 2. Заблокировать победу соперника
    for row, col in empty:
        if would_win(board, row, col, human):
            return row, col

    center = board.size // 2
    if (center, center) in empty:
        return center, center

    corners = [
        (0, 0),
        (0, board.size - 1),
        (board.size - 1, 0),
        (board.size - 1, board.size - 1),
    ]
    for cell in corners:
        if cell in empty:
            return cell

    return empty[0]


def cell_from_mouse(mx: int, my: int) -> Optional[Tuple[int, int]]:
    col = (mx - OFFSET_X) // CELL
    row = (my - OFFSET_Y) // CELL
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        return row, col
    return None


def draw_mark(surface: pygame.Surface, row: int, col: int, mark: PlayerMark) -> None:
    x = OFFSET_X + col * CELL
    y = OFFSET_Y + row * CELL
    pad = 22
    if mark == "X":
        pygame.draw.line(surface, X_COLOR, (x + pad, y + pad), (x + CELL - pad, y + CELL - pad), 6)
        pygame.draw.line(surface, X_COLOR, (x + CELL - pad, y + pad), (x + pad, y + CELL - pad), 6)
    else:
        pygame.draw.circle(
            surface,
            O_COLOR,
            (x + CELL // 2, y + CELL // 2),
            CELL // 2 - pad,
            6,
        )


def draw_board(surface: pygame.Surface, board: Board, status: str) -> None:
    surface.fill(BG)
    font = pygame.font.SysFont("consolas", 28)
    surface.blit(font.render(status, True, TEXT), (24, 24))

    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            surface,
            GRID,
            (OFFSET_X, OFFSET_Y + i * CELL),
            (OFFSET_X + BOARD_SIZE * CELL, OFFSET_Y + i * CELL),
            3,
        )
        pygame.draw.line(
            surface,
            GRID,
            (OFFSET_X + i * CELL, OFFSET_Y),
            (OFFSET_X + i * CELL, OFFSET_Y + BOARD_SIZE * CELL),
            3,
        )
    pygame.draw.rect(
        surface,
        GRID,
        (OFFSET_X, OFFSET_Y, BOARD_SIZE * CELL, BOARD_SIZE * CELL),
        3,
    )

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            mark = board.cells[row][col]
            if mark:
                draw_mark(surface, row, col, mark)

    hint = pygame.font.SysFont("consolas", 20).render("ЛКМ — ход · R — заново · Esc — выход", True, TEXT)
    surface.blit(hint, (24, HEIGHT - 36))


def main() -> None:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Крестики-нолики")
    clock = pygame.time.Clock()
    board = Board()
    human_turn = True
    status = "Ваш ход (X)"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    board.reset()
                    human_turn = True
                    status = "Ваш ход (X)"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and human_turn:
                if board.winner() or board.is_full():
                    continue
                cell = cell_from_mouse(*event.pos)
                if cell is None:
                    continue
                row, col = cell
                if not board.place(row, col, "X"):
                    continue
                human_turn = False
                winner = board.winner()
                if winner:
                    status = "Победа X!"
                elif board.is_full():
                    status = "Ничья"
                else:
                    status = "Ход компьютера (O)…"

        if not human_turn and not board.winner() and not board.is_full():
            row, col = choose_ai_move(board)
            board.place(row, col, "O")
            human_turn = True
            winner = board.winner()
            if winner:
                status = "Победа O — попробуйте ещё (R)"
            elif board.is_full():
                status = "Ничья — R для реванша"
            else:
                status = "Ваш ход (X)"

        draw_board(screen, board, status)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
