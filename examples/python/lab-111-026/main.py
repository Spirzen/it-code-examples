def draw_dragon_curve(length: float, iterations: int):
    """
    Итеративная реализация на основе последовательности поворотов:
    На шаге n повороты = повороты_{n-1} + ['R'] + инвертированные(повороты_{n-1}) в обратном порядке.
    Эффективно строим через бит: поворот на шаге i — 'L', если (i & -i) * 2 & i != 0, иначе 'R'.
    """
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length * 1.5, 0)
    t.pendown()
    t.setheading(0)

    total_steps = 2 ** iterations
    for i in range(total_steps):
        t.forward(length)
        # Определение направления поворота:
        # i начинается с 0; поворот после i-го отрезка
        turn_right = ((i & -i) << 1) & (i + 1) == 0
        if turn_right:
            t.right(90)
        else:
            t.left(90)
    t.hideturtle()
