# Functions and Turtle
# Author: Emily Song 
# 28 November 2023

import turtle

# create a turtle, give it a friendly name

mikey_turtle = turtle.Turtle()
mikey_turtle.color("lightgreen")
mikey_turtle.shape("turtle")

def squared(num: float) -> float:
    """Returns the given number squared"""
    return num**2

def draw_square(side_length: float) -> None:
    for _ in range(4):
        mikey_turtle.forward(side_length)
        mikey_turtle.left(90)

mikey_turtle.speed(0)

# Create a square that gets bigger and bigger 
for i in range(50):
    draw_square(squared(i))

turtle.done()
