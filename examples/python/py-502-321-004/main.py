def koch_curve(length, depth):
    if depth == 0:
        t.fd(length)
    else:
        koch_curve(length / 3, depth - 1)
        t.lt(60)
        koch_curve(length / 3, depth - 1)
        t.rt(120)
        koch_curve(length / 3, depth - 1)
        t.lt(60)
        koch_curve(length / 3, depth - 1)

def koch_snowflake(size=200, depth=3):
    t.penup()
    t.goto(-size / 2, size / 3**0.5 / 2)
    t.pendown()
    for _ in range(3):
        koch_curve(size, depth)
        t.rt(120)
