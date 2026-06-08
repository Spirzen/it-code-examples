
import turtle

t = turtle.Turtle()
t.speed(9)

# Внешние лепестки
t.begin_fill()
t.fillcolor("lightblue")
for _ in range(12):
    t.circle(80, 60)
    t.left(120)
    t.circle(80, 60)
    t.left(120)
    t.left(30)
t.end_fill()

# Средние лепестки
t.begin_fill()
t.fillcolor("lightgreen")
for _ in range(8):
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(120)
    t.left(45)
t.end_fill()

# Центр
t.begin_fill()
t.fillcolor("yellow")
t.circle(30)
t.end_fill()

turtle.done()
