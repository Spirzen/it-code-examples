
import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()

# Начальная позиция
start_x = -50
start_y = 50
step = 30  # расстояние между точками

for row in range(3):
    for col in range(3):
        x = start_x + col * step
        y = start_y - row * step
        
        t.goto(x, y)
        t.pendown()
        
        # Квадрат 20x20
        for side in range(4):
            t.forward(20)
            t.left(90)
        
        t.penup()

turtle.done()
