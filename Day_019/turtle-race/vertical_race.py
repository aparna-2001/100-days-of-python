#Day_019
#Turtle race
# 1. Top-to-Bottom Race — turtles race vertically from top to bottom.

import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title = "turtle race", prompt="which turtle will win the race? enter the color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
is_race_on = False

change = 0

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = change, y = 300)
    new_turtle.setheading(270)
    change += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.ycor() < (-300-(40/2)):
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle won the race")
            else:
                print(f"you've lost! the {winning_color} turtle won the race")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
