def draw_sierpinski_chaos(
    side: float = 400,
    points: int = 20000,
    dot_size: int = 1
):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    screen = turtle.Screen()
    screen.tracer(0)

    # Вершины равностороннего треугольника
    h = side * math.sqrt(3) / 2
    A = (0, 0)
    B = (side, 0)
    C = (side / 2, h)
    vertices = [A, B, C]

    # Старт из середины AB
    x, y = side / 2, 0

    for _ in range(points):
        # Случайная вершина
        vx, vy = random.choice(vertices)
        # Середина между текущей точкой и выбранной вершиной
        x = (x + vx) / 2
        y = (y + vy) / 2
        t.goto(x - side / 2, y - h / 3)  # смещение для центрирования
        t.dot(dot_size, "black")

        if _ % 500 == 0:
            screen.update()
    screen.update()
