
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)

def drag(x, y):
    pen.ondrag(None)  # Блокировка рекурсии
    pen.goto(x, y)
    pen.ondrag(drag)  # Возврат обработчика

pen.ondrag(drag)
screen.listen()
turtle.done()
