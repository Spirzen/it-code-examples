
import turtle
import math

def iso_project(x: float, y: float, z: float, scale: float = 1.0) -> tuple[float, float]:
    """Изометрическая проекция (углы 30°, 30°, 120°)"""
    iso_x = (x - y) * math.cos(math.radians(30)) * scale
    iso_y = (x + y) * math.sin(math.radians(30)) - z * scale
    return iso_x, iso_y

def draw_iso_cube(edge: float, origin: tuple[float, float] = (0, 0), fill: bool = False, color: str = "gray"):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.penup()
    # Вершины куба (x, y, z)
    vertices = [
        (0, 0, 0), (edge, 0, 0), (edge, edge, 0), (0, edge, 0),
        (0, 0, edge), (edge, 0, edge), (edge, edge, edge), (0, edge, edge)
    ]
    # Проекция
    proj = [iso_project(x, y, z, 1.0) for x, y, z in vertices]
    # Смещение к origin
    proj = [(px + origin[0], py + origin[1]) for px, py in proj]
    
    # Рёбра (индексы вершин)
    edges = [
        (0,1), (1,2), (2,3), (3,0),  # нижняя грань
        (4,5), (5,6), (6,7), (7,4),  # верхняя грань
        (0,4), (1,5), (2,6), (3,7)   # боковые
    ]
    
    for i1, i2 in edges:
        t.penup()
        t.goto(*proj[i1])
        t.pendown()
        t.goto(*proj[i2])
    t.hideturtle()

draw_iso_cube(100)

turtle.done()
