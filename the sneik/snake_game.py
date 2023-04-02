from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Sneik Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment in the tail // user list slice
        # trigger game_over sequence
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
