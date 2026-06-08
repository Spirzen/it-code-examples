
import turtle
import math

def draw_regular_polygon(n: int, side: float = None, radius: float = None,
                         mode: str = "side", fill: bool = False, color: str = "black"):
    """
    :param n: количество сторон (n ≥ 3)
    :param side: длина стороны (при mode='side')
    :param radius: радиус описанной окружности (при mode='radius')
    :param mode: 'side' или 'radius' — что задано
    """
    if n < 3:
        raise ValueError("n должно быть ≥ 3")
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    if fill:
        t.begin_fill()
    
    # Вычисление угла поворота и стороны/радиуса
    angle = 360.0 / n
    if mode == "radius":
        if radius is None:
            raise ValueError("Для mode='radius' требуется параметр radius")
        side = 2 * radius * math.sin(math.radians(angle / 2))
        # Центрирование: переместиться в начальную точку
        t.penup()
        t.goto(radius, 0)
        t.setheading(90 + angle / 2)
        t.pendown()
    elif mode == "side":
        if side is None:
            raise ValueError("Для mode='side' требуется параметр side")
        radius = side / (2 * math.sin(math.radians(angle / 2)))
        t.penup()
        t.goto(0, -radius)
        t.setheading(0)
        t.pendown()
    else:
        raise ValueError("mode должен быть 'side' или 'radius'")
    
    for _ in range(n):
        t.forward(side)
        t.left(angle)
    
    if fill:
        t.end_fill()
    t.hideturtle()

draw_regular_polygon(5, 100, 100)

turtle.done()
