#spirograph

import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
timmy_the_turtle.hideturtle()
turtle.colormode(255)

def rgb_colours():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.speed('fastest')
        timmy_the_turtle.circle(100)
        current_heading = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_heading+size_of_gap)
        timmy_the_turtle.color(rgb_colours())

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

