def house(size=100):
    # Стены
    t.begin_fill()
    t.fillcolor("lightgray")
    for _ in range(4):
        t.fd(size)
        t.rt(90)
    t.end_fill()
    
    # Крыша
    t.fillcolor("brown")
    t.begin_fill()
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.end_fill()
    t.lt(180)  # возврат направления
    
    # Дверь
    t.penup()
    t.goto(size * 0.35, 0)
    t.pendown()
    t.fillcolor("saddlebrown")
    t.begin_fill()
    for _ in range(2):
        t.fd(size * 0.3)
        t.lt(90)
        t.fd(size * 0.5)
        t.lt(90)
    t.end_fill()
    
    # Окно
    t.penup()
    t.goto(size * 0.6, size * 0.6)
    t.pendown()
    t.fillcolor("cyan")
    t.begin_fill()
    for _ in range(4):
        t.fd(size * 0.2)
        t.rt(90)
    t.end_fill()
