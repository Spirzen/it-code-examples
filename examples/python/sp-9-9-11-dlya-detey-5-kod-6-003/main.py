
import turtle

t = turtle.Turtle()
t.speed(5)  # от 1 (медленно) до 10 (быстро); 0 — мгновенно

t.color("blue")        # цвет лини
t.fillcolor("yellow")  # цвет заливки
t.begin_fill()         # начать заливку

for _ in range(3):     # _ — имя, когда значение не нужно
    t.forward(120)
    t.left(120)

t.end_fill()           # закончить заливку
turtle.done()
