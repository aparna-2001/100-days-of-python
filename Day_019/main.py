
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(5)
def move_backwards():
    tim.backward(5)
def move_clockwise():
    tim.right(10)
def move_counterclockwise():
    tim.left(10)
def clear_screen():
    tim.reset()

screen.listen()
screen.onkey(fun= move_forward , key= 'W')
screen.onkey(fun= move_backwards , key= 'S')
screen.onkey(fun= move_clockwise , key= 'D')
screen.onkey(fun= move_counterclockwise , key= 'A')
screen.onkey(fun= clear_screen , key= 'C')

screen.exitonclick()