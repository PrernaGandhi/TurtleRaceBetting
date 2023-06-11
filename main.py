from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your Bet", prompt="Enter the color of turtle you wish to bet on: ")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []


def create_turtle(colour, y):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colour)
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)


y = -100
for color in colors:
    create_turtle(color, y)
    y += 30


if user_bet in colors:
    is_race_on = True
while is_race_on :
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You win !! {turtle.pencolor()} turtle won!!!!")
            else:
                print(f"You lose :( . {turtle.pencolor()} turtle won")
        random_distance = random.randint(0, 10)
        turtle.speed("fastest")
        turtle.forward(random_distance)




screen.exitonclick()
