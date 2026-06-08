
import turtle
import math

def draw_archimedean_spiral(a: float, b: float, turns: int = 5, step_deg: float = 1.0):
    t = turtle.Turtle()
    t.speed(0)
    total_deg = turns * 360
    t.penup()
    for deg in range(0, int(total_deg), int(step_deg)):
        rad = math.radians(deg)
        r = a + b * rad
        x = r * math.cos(rad)
        y = r * math.sin(rad)
        t.goto(x, y)
        if deg == 0:
            t.pendown()
    t.hideturtle()

draw_archimedean_spiral(10, 10)

turtle.done()
