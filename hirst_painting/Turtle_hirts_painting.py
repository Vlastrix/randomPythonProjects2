from turtle import Turtle, Screen, colormode
from random import choice
colormode(255)
# Used to steal colors (literal XD)
# import colorgram
# rgb_colors = []
# colors = colorgram.extract("something.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
tim = Turtle()
tim.hideturtle()
tim.pensize(20)
tim.speed("fast")
tim.penup()
x = -300
y = -300
tim.goto(x, y)

colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
                (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10),
                (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9),
                (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167),
                (77, 234, 202), (52, 234, 243), (3, 67, 40)]
# size of circles 20
# Distance 50
# 10 by 10 rows


def dots():
    for _ in range(10):
        tim.setheading(0)
        tim.pendown()
        tim.pencolor(choice(colors))
        tim.dot(16)
        tim.penup()
        tim.forward(50)


dots()

for _ in range(9):
    y += 50
    tim.goto(x, y)
    dots()


screen = Screen()
screen.exitonclick()
