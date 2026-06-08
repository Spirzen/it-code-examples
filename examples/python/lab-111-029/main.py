def meander_pattern(
    segment: float = 20,
    repeats: int = 10,
    turns: int = 4,      # 4 = стандартный меандр (квадратный), 6 = гексагональный
    fill: bool = False
):
    t = turtle.Turtle()
    t.speed(0)
    if fill:
        t.begin_fill()
    angle = 360.0 / turns

    for _ in range(repeats):
        for _ in range(turns - 1):
            t.forward(segment)
            t.left(angle)
        t.forward(segment * 2)  # "перемычка"
        t.right(angle)
    if fill:
        t.end_fill()
    t.hideturtle()
