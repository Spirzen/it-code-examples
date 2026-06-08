import re

def matches(pattern: str, text: str, flags: int = 0) -> bool:
    """True, если ВСЯ строка text подходит под pattern."""
    return re.fullmatch(pattern, text, flags) is not None

def find_all(pattern: str, text: str, flags: int = 0) -> list[str]:
    """Список всех найденных фрагментов в text."""
    return re.findall(pattern, text, flags)

def first_groups(pattern: str, text: str):
    """Первая строка лога → кортеж групп (date, time, ..)."""
    m = re.match(pattern, text)
    return m.groups() if m else None
