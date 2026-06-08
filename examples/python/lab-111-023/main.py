
import turtle
import math

def draw_polar_rose(a: float, k: int, step_deg: float = 2.0):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    for deg in range(0, 360 * (1 if k % 2 else 2), int(step_deg)):
        rad = math.radians(deg)
        r = a * math.cos(k * rad)
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        t.goto(x, y)
        if deg == 0:
            t.pendown()
    t.hideturtle()

draw_polar_rose(100, 5)

turtle.done()
