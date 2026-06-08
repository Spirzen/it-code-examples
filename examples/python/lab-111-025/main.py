def rotating_rose(
    petal_count: int = 6,
    radius: float = 80,
    phase_step: float = 2.0,  # градусов за кадр
    delay_ms: int = 50
):
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.tracer(0)
    
    state = {"phase": 0.0}

    def clear_and_redraw():
        t.clear()
        phase = state["phase"]
        for i in range(petal_count):
            angle = i * (360.0 / petal_count) + phase
            t.penup()
            t.goto(0, 0)
            t.setheading(angle)
            t.pendown()
            t.circle(radius, 60)
            t.left(120)
            t.circle(radius, 60)
        screen.update()
        state["phase"] = (state["phase"] + phase_step) % 360.0
        screen.ontimer(clear_and_redraw, delay_ms)

    clear_and_redraw()
    screen.mainloop()
