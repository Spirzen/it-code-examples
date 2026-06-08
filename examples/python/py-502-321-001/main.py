
import turtle

from math import sin, cos, pi

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

for i in range(360):
    r = int(127.5 * (1 + sin(i * pi / 180)))
    g = int(127.5 * (1 + cos(i * pi / 180)))
    b = 255 - r
    t.pencolor(r, g, b)
    t.forward(i * 0.3)
    t.left(59)
