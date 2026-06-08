
import turtle
import math

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

t.begin_fill()
t.fillcolor("red")

t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)

t.end_fill()

t.penup()

t.hideturtle()
turtle.done()
