# Turtle example
# Author: Emily Song 
# 21 November 2023

import turtle

# ----- CONSTANTS (for robustness)
TURTLE_MAGNITUDE = 20
# create a turtle
michaelangelo = turtle.Turtle()  
# The capital T at the end signifies that the Turtle is a class

# Get some instructions from the user
print("""To give commands, type: 
F - to go forward
L - to go left
R - to go right 
B - to go back """)


# Repeat the below code INDEFINITELY
done = False

# Repeat the action is we are not done making the end product
while not done: 

    command = input("Where should I go?").strip(".!?,").lower()
    # Based on the instructions, move the turtle from the screen
    # on the screen 
    if command in ["f", "forward"]:
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command in ["b", "backward"]:
        michaelangelo.back(TURTLE_MAGNITUDE)
    elif command in ["r", "right"]:
        michaelangelo.right(90)
    elif command in ["l", "left"]:
        michaelangelo.left(90)
    elif command == "stop":
        done = True 
    
   
turtle.done()

