
import turtle

t = turtle.Turtle()
t.speed(5)

t.begin_fill()
t.fillcolor("pink")

for _ in range(6):
    t.circle(50)  # Радиус лепестка
    t.left(60)    # Поворот между лепестками

t.end_fill()

turtle.done()
