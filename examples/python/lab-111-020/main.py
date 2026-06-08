
import turtle

from collections import deque

def draw_pythagoras_tree_iterative(base_len: float, depth: int, angle: float = 45.0):
    t = turtle.Turtle()
    t.speed(0)
    stack = deque()
    # (x, y, heading, length, level)
    stack.append((0, 0, 90, base_len, 0))
    
    while stack:
        x, y, heading, length, level = stack.pop()
        if level > depth:
            continue
        t.penup()
        t.goto(x, y)
        t.setheading(heading)
        t.pendown()
        t.forward(length)
        new_x, new_y = t.position()
        # Левая ветвь
        stack.append((new_x, new_y, heading - angle, length * 0.7, level + 1))
        # Правая ветвь
        stack.append((new_x, new_y, heading + angle, length * 0.7, level + 1))
    t.hideturtle()

draw_pythagoras_tree_iterative(100, 5)

turtle.done()
