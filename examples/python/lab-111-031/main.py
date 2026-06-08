def radial_gradient_circle(
    radius: float,
    layers: int = 50,
    inner_color: str = "white",
    outer_color: str = "black"
):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    screen = turtle.Screen()
    screen.colormode(255)
    inner_rgb = screen.getcanvas().winfo_rgb(inner_color)
    outer_rgb = screen.getcanvas().winfo_rgb(outer_color)
    # getcanvas().winfo_rgb возвращает значения в диапазоне [0, 65535]
    inner_rgb = tuple(c // 256 for c in inner_rgb)
    outer_rgb = tuple(c // 256 for c in outer_rgb)

    for i in range(layers, 0, -1):
        r_frac = i / layers
        current_radius = radius * r_frac
        # Интерполяция цвета
        r = int(inner_rgb[0] * r_frac + outer_rgb[0] * (1 - r_frac))
        g = int(inner_rgb[1] * r_frac + outer_rgb[1] * (1 - r_frac))
        b = int(inner_rgb[2] * r_frac + outer_rgb[2] * (1 - r_frac))
        t.color((r, g, b))
        # Рисуем окружность текущего радиуса (толщиной ~radius/layers)
        t.goto(0, -current_radius)
        t.pendown()
        t.circle(current_radius)
        t.penup()
    t.hideturtle()
