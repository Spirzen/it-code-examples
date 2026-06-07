"""Модуль 5: конфигурация."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    debug: bool = False
    lang: str = "ru"
