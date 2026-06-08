
import turtle

screen = turtle.Screen()
screen.listen()

t = turtle.Turtle()
t.shape("turtle")
t.color("green")

def go_up():
    t.setheading(90)
    t.forward(20)

def go_down():
    t.setheading(270)
    t.forward(20)

def go_left():
    t.setheading(180)
    t.forward(20)

def go_right():
    t.setheading(0)
    t.forward(20)

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(screen.bye, "q")

print("Управление: стрелки — движение, Q — выход")
