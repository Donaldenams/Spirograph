from turtle import Turtle, Screen
import random

dee = Turtle()

dee.shape('turtle')
dee.speed('fastest')



def random_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    dee.color(r, g, b)


def draw_spiral(gap_size):
    for _ in range(int(360 / gap_size)):
        random_colors()
        dee.circle(100)
        dee.setheading(dee.heading() + gap_size)


draw_spiral(5)

see = Screen()
see.exitonclick()
