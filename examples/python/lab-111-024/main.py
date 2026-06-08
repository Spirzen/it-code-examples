def animated_archimedean_spiral(
    a_start: float = 0.1, 
    b_start: float = 2.0, 
    a_step: float = 0.0, 
    b_step: float = -0.02, 
    max_turns: int = 15,
    delay_ms: int = 40
):
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.tracer(0)  # Отключаем автообновление

    state = {"a": a_start, "b": b_start, "turns": 0.0, "done": False}

    def step():
        if state["done"]:
            return
        a, b = state["a"], state["b"]
        turns = state["turns"]
        deg = turns * 360.0
        rad = math.radians(deg)
        r = a + b * rad
        x = r * math.cos(rad)
        y = r * math.sin(rad)

        if turns >= max_turns or r < 0:
            state["done"] = True
            t.hideturtle()
            return

        if deg == 0:
            t.penup()
            t.goto(0, 0)
            t.pendown()
        else:
            t.goto(x, y)

        state["a"] += a_step
        state["b"] += b_step
        state["turns"] += 1.0 / 360.0

        screen.update()
        screen.ontimer(step, delay_ms)

    step()
    screen.mainloop()
