# Cookies 
# Author: Emily Song 
# 21 November 2023

import random
import turtle

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")

 # applying the mathematical concept of functions and inputs
def make_cookie(x: int, y: int):
    """Draws a cookie on the screen at (x,y)
    Parameters:
    x- x-coordinate of the centre of the cookie
    y- y-coordinate of the centre of the cookie
    """

    # set up the outline of the cookie
    baker_turtle.color("brown")
    baker_turtle.penup()
    baker_turtle.goto(-5 + x, -30 + y)
    baker_turtle.pendown()
    baker_turtle.circle(30)
    baker_turtle.penup()


    # center 
    baker_turtle.goto(0 + x,0+ y )
    baker_turtle.stamp()

    # Top right chip, bottom-right, bottom-left, middle) 
    baker_turtle.goto(10 + x,10 +y)
    baker_turtle.stamp()
    baker_turtle.goto(10 +x,-10 +y)
    baker_turtle.stamp()
    baker_turtle.goto(-10 +x,-10 +y)
    baker_turtle.stamp()
    baker_turtle.goto(-10+ x,10+y)
    baker_turtle.stamp()
    baker_turtle.penup()
    
make_cookie(100,100)
make_cookie(0,0)
