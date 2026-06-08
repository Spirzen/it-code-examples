def hex_grid(
    radius: float,
    cols: int,
    rows: int,
    gap: float = 0.0,
    fill: bool = False,
    color: str = "gold"
):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.penup()
    
    # Вертикальное и горизонтальное смещение между центрами
    dx = (radius + gap) * 3 / 2
    dy = (radius + gap) * math.sqrt(3)

    for row in range(rows):
        y_offset = row * dy
        x_start = 0 if row % 2 == 0 else dx / 2
        for col in range(cols):
            cx = x_start + col * dx
            cy = y_offset

            # Рисуем шестиугольник с центром в (cx, cy)
            t.goto(cx + radius, cy)
            t.setheading(30)
            t.pendown()
            if fill:
                t.begin_fill()
            for _ in range(6):
                t.forward(radius)
                t.left(60)
            if fill:
                t.end_fill()
            t.penup()
    t.hideturtle()
