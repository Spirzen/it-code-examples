
import turtle
import random

screen = turtle.Screen()
player = turtle.Turtle()
target = turtle.Turtle()

player.shape("turtle")
player.penup()
target.shape("circle")
target.color("red")
target.penup()
target.goto(random.randint(-200, 200), random.randint(-200, 200))

def move():
    player.forward(20)
    if player.distance(target) < 20:
        target.goto(random.randint(-200, 200), random.randint(-200, 200))

screen.onkey(move, "space")
screen.listen()
turtle.done()
