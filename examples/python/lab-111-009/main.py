
import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()

# Начальная позиция
start_x = -50
start_y = 50
step = 30  # расстояние между точками

for row in range(8):
    for col in range(8):
        x = -100 + col * 25
        y = 100 - row * 25
        t.goto(x, y)
        t.dot(20, "black")

turtle.done()
