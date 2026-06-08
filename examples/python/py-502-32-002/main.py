t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.penup()
t1.goto(-200, 0)
t1.pendown()
t1.color("red")

t2.penup()
t2.goto(200, 0)
t2.pendown()
t2.color("blue")
t2.setheading(180)  # смотрит влево

# Ползут навстречу
for _ in range(100):
    t1.forward(2)
    t2.forward(2)
