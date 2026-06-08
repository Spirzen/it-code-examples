
import time

def draw_clock():
    # Циферблат
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.circle(150)
    
    # Чёрточки часов
    for _ in range(12):
        t.penup()
        t.fd(130)
        t.pendown()
        t.fd(20)
        t.penup()
        t.goto(0, 0)
        t.rt(30)

def clock_hands():
    # Получаем время
    lt = time.localtime()
    h, m, s = lt.tm_hour % 12, lt.tm_min, lt.tm_sec
    
    # Часовая стрелка
    t.penup(); t.goto(0, 0); t.setheading(90)
    t.rt(30 * h + 0.5 * m); t.pendown()
    t.pensize(5); t.fd(60)
    
    # Минутная
    t.penup(); t.goto(0, 0); t.setheading(90)
    t.rt(6 * m); t.pendown()
    t.pensize(3); t.fd(90)
    
    # Секундная
    t.penup(); t.goto(0, 0); t.setheading(90)
    t.rt(6 * s); t.pendown()
    t.pencolor("red"); t.pensize(1); t.fd(100)

draw_clock()
while True:
    t.clear()
    draw_clock()
    clock_hands()
    screen.update()
    time.sleep(1)
