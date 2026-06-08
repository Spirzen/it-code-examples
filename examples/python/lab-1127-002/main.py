import turtle

t = turtle.Turtle()
screen = turtle.Screen()
step = 8

def left():
    t.setx(t.xcor() - step)

def right():
    t.setx(t.xcor() + step)

screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

turtle.done()
