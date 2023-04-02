from turtle import Turtle, Screen, colormode
from random import randint
# Timmy modifications
tim = Turtle()
colormode(255)
# this is very important in order to rgb function work
tim.shape("turtle")
tim.color("turquoise1")
tim.pencolor("red")
tim.pensize(1)
tim.speed(0)


def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rbg = (r, g, b)
    return rbg


angles = -6
for _ in range(60):
    tim.pencolor(rand_color())
    tim.circle(100)
    angles += 6
    tim.setheading(angles)


screen = Screen()
screen.exitonclick()
