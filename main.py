import turtle as t
from turtle import Turtle
from turtle import Screen
import random

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g , b)
    return color

tam = Turtle()
tam.speed("fastest")

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tam.color(random_color())
        tam.circle(100)
        tam.setheading(tam.heading() + gap_size)
        tam.circle(100)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()