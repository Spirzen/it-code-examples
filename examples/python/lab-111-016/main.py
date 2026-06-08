
import turtle
import math

def draw_flower_petals(radius: float, petal_count: int, petal_radius: float, fill: bool = False):
    t = turtle.Turtle()
    t.speed(0)
    angle_step = 360.0 / petal_count
    
    for i in range(petal_count):
        t.penup()
        t.goto(radius * math.cos(math.radians(i * angle_step)),
               radius * math.sin(math.radians(i * angle_step)))
        t.setheading(i * angle_step)
        t.pendown()
        if fill:
            t.begin_fill()
        t.circle(petal_radius)
        if fill:
            t.end_fill()
    t.hideturtle()

draw_flower_petals(100, 10, 100)

turtle.done()
