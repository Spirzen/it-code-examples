
import turtle

t = turtle.Turtle()

t.color("cyan")
t.pensize(2)

for i in range(8):
    t.forward(50)
    t.backward(50)
    t.right(45)


turtle.done()
