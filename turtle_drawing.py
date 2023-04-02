from turtle import Turtle, Screen
from random import choice
# Timmy modifications
tim = Turtle()
tim.shape("turtle")
tim.color("turquoise1")
tim.pencolor("red")
tim.pensize(2)
colors = ["#920f5e", "#869bd0", "#a0ca24", "#08d836", "#6692d2", "#269046", "#717852", "#5f2e41", "#e6694d", "#094de0"]
count = 0


def main(num_sides):
    global count
    if count == 0:
        tim.pencolor(choice(colors))
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    main(shape_side)


screen = Screen()
screen.exitonclick()
