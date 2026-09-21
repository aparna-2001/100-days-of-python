# day 018
# Hirst painting


import turtle
from turtle import Turtle, Screen
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

turtle.colormode(255)
tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.penup()
tim.hideturtle()

#removed two colors since they match the background
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

def move_horizontal():
    for _ in range(9):
        tim.dot( 10,random.choice(color_list) )
        tim.penup()
        tim.forward(50)
        tim.penup()
        tim.dot(10)

def right_corner():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)

def left_corner():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)

def draw():
    for _ in range(5):
        move_horizontal()
        right_corner()
        move_horizontal()
        left_corner()

draw()

screen = Screen()
screen.exitonclick()
