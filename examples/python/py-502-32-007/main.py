
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
angle = 0

def rotate():
    global angle
    pen.clear()
    pen.setheading(angle)
    pen.forward(50)
    pen.stamp()
    angle += 10
    screen.ontimer(rotate, 100)  # Запуск через 100 мс

pen.speed(0)
rotate()
turtle.done()
