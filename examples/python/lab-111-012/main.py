
import turtle

def draw_equilateral_triangle(side: float, fill: bool = False, color: str = "black"):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    if fill:
        t.begin_fill()
    for _ in range(3):
        t.forward(side)
        t.left(120)  # Внешний угол = 180° – 60° = 120°
    if fill:
        t.end_fill()
    t.hideturtle()
	
draw_equilateral_triangle(100)

turtle.done()
