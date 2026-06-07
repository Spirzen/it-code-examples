#!/usr/bin/env python3
"""Шаг 3 практикума: функции."""


def area(width: float, height: float) -> float:
    return width * height


if __name__ == "__main__":
    w, h = 4, 2.5
    print(f"Площадь: {area(w, h)}")
