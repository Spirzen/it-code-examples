
import turtle

def draw_tree(branch_len, t, angle, depth):
    if depth > 0:
        # Рисуем ветку
        t.begin_fill()
        t.fillcolor(f"#{min(100 + depth*15, 255):02x}6432")  # Градиент коричневого
        t.forward(branch_len)
        t.left(angle)
        t.end_fill()
        
        # Рекурсивно рисуем левую и правую ветки
        draw_tree(branch_len * 0.7, t, angle, depth - 1)
        t.right(angle * 2)
        draw_tree(branch_len * 0.7, t, angle, depth - 1)
        t.left(angle)
        t.backward(branch_len)

# Настройка
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("lightblue")

t.left(90)
t.up()
t.backward(200)
t.down()
t.color("brown")

# Рисуем дерево
draw_tree(100, t, 30, 6)

t.hideturtle()
turtle.done()
