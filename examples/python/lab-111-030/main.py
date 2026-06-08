def gradient_arc(
    radius: float,
    extent: float = 180.0,
    steps: int = 36,
    start_color: tuple[int, int, int] = (255, 0, 0),
    end_color: tuple[int, int, int] = (0, 0, 255)
):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    # Разбиваем дугу на сегменты
    angle_step = extent / steps
    for i in range(steps):
        # Текущий угол (радианы)
        theta1 = math.radians(i * angle_step)
        theta2 = math.radians((i + 1) * angle_step)

        # Точки дуги
        x1 = radius * math.cos(theta1)
        y1 = radius * math.sin(theta1)
        x2 = radius * math.cos(theta2)
        y2 = radius * math.sin(theta2)
        
        # Цвет интерполируем линейно
        ratio = i / (steps - 1)
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        t.color((r, g, b))

        # Рисуем треугольник: центр → точка1 → точка2
        t.goto(0, 0)
        t.pendown()
        t.goto(x1, y1)
        t.goto(x2, y2)
        t.goto(0, 0)
        t.penup()
    t.hideturtle()
