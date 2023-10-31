# Pumpkin Drawing
# Author: Emily Song
# Date: 31 October 2023

import turtle
import time
turtle.title("Emily Song's pumpkin carving exercise")



window = turtle.Screen()
window.bgcolor("black")

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
carver.setposition(0, 0)
carver.dot(20)
carver.forward(15)

# The left eye
carver.penup()
carver.setposition(-40,40)
carver.dot(20)
carver.forward(15)


# The right eye
carver.penup()
carver.setposition(40,40)
carver.dot(20)
carver.forward(15)

#carve out a smile
carver.penup()
carver.setposition(0,-40)
carver.pendown()
carver.pensize(10)
carver.color('brown')

carver.backward(100)
carver.circle(100,100)

carver.right(270)
carver.forward(100)
carver.end_fill()




turtle.done()
