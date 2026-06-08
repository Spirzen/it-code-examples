
import turtle

import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()

size = 30
start_x = -120
start_y = 120

for row in range(8):
    for col in range(8):
        x = start_x + col * size
        y = start_y - row * size
        
        # Определяем цвет
        if (row + col) % 2 == 0:
            color = "black"
        else:
            color = "white"
        
        t.goto(x, y)
        t.dot(size, color)  # dot размером с клетку

turtle.done()
