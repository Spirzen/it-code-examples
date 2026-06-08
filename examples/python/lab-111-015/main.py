
import turtle
import math

def draw_star(n: int, radius: float, step: int = 2, fill: bool = False, color: str = "black"):
    """
    Рисует звезду {n/step} по обозначению Шлефли.
    Требуется, чтобы gcd(n, step) == 1 и 2*step < n.
    """
    if math.gcd(n, step) != 1 or 2 * step >= n:
        raise ValueError("Некорректные параметры: требуется gcd(n, step) == 1 и 2*step < n")
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    if fill:
        t.begin_fill()
    
    angle = 360.0 / n
    t.penup()
    t.goto(radius, 0)
    t.setheading(90 + angle / 2)
    t.pendown()
    
    for _ in range(n):
        t.forward(radius * 2 * math.sin(math.radians(step * angle / 2)))
        t.left(step * angle)
    
    if fill:
        t.end_fill()
    t.hideturtle()

draw_star(5, 100)

turtle.done()
