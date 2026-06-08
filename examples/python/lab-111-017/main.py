
import turtle

def draw_rose(petal_count: int, radius: float, fill: bool = False, color: str = "pink"):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    angle_step = 360.0 / petal_count
    
    for i in range(petal_count):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * angle_step)
        t.pendown()
        if fill:
            t.begin_fill()
        t.circle(radius, 60)  # Первая дуга
        t.left(120)
        t.circle(radius, 60)  # Вторая дуга — замыкает лепесток
        if fill:
            t.end_fill()
    t.hideturtle()

draw_rose(5, 100)

turtle.done()
