from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def quadrant(p):
    match p:
        case Point(x=0, y=0):
            return "начало координат"
        case Point(x=x, y=y) if x >= 0 and y >= 0:
            return "I четверть"
        case Point(x=x, y=y):
            return f"точка ({x}, {y})"
