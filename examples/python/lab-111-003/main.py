
import turtle

t = turtle.Turtle()

t.speed(8)
t.color("red")
t.pensize(3)

for i in range(6):
    t.circle(30)      # маленький круг — лепесток
    t.right(60)       # поворот на 60 градусов

t.color("yellow")
t.dot(20)             # серединка

turtle.done()
