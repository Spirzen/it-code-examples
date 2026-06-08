
import turtle

def draw_rectangle(width: float, height: float, fill: bool = False, color: str = "black"):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    if fill:
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    if fill:
        t.end_fill()
    t.hideturtle()

draw_rectangle(100,200)

turtle.done()
