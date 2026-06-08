def koch_curve_string(iterations: int) -> str:
    s = "F"
    for _ in range(iterations):
        s = s.replace("F", "F+F--F+F")
    return s

def draw_koch_snowflake(side: float, iterations: int = 3):
    t = turtle.Turtle()
    t.speed(0)
    instr = koch_curve_string(iterations)
    scale = side / (3 ** iterations)
    
    t.penup()
    t.goto(-side / 2, -side / (2 * math.sqrt(3)))
    t.pendown()
    t.setheading(0)
    
    for c in instr:
        if c == "F":
            t.forward(scale)
        elif c == "+":
            t.left(60)
        elif c == "-":
            t.right(60)
    
    # Замыкание в снежинку
    for _ in range(2):
        for c in instr:
            if c == "F":
                t.forward(scale)
            elif c == "+":
                t.left(60)
            elif c == "-":
                t.right(60)
        t.right(120)
    t.hideturtle()
