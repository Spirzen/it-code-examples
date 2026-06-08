def setup_experiment_window(
    title: str = "Turtle Experiment",
    width: int = 800,
    height: int = 600,
    bg_color: str = "white",
    fast_draw: bool = True
) -> tuple[turtle.Turtle, turtle.Screen]:
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(bg_color)
    if fast_draw:
        screen.tracer(0)
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    return t, screen
