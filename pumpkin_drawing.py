# Pumpkin Drawing
# Author: Emily Song
# Date: 31 October 2023

import turtle
import time
turtle.title("Emily Song's pumpkin carving exercise")



window = turtle.Screen()
window.bgcolor("pink")


# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 20)
carver.dot(20)
carver.forward(15)

# The left eye
carver.penup()
carver.setposition(-40,55)
carver.dot(20)
carver.forward(15)


# The right eye
carver.penup()
carver.setposition(40,55)
carver.dot(20)
carver.forward(15)

#carve out a smile
carver.penup()
carver.setposition(-60, 0)
carver.pendown()
carver.pensize(7)
carver.color('dark orange')

# To spped up the carver, 0 is the fastest speed
carver.speed(0)
carver.right(90)

#carving out a curved smile line 
for x in range(180):
    carver.forward(1)
    carver.left(1)
carver.right(20)

# Add a hat 
hat = turtle.Turtle()
hat.hideturtle()
hat.color("dark orange")
hat.penup()
hat.setposition(0,100)
hat.pendown()
hat.dot(40)


carver.penup()

turtle.done()
