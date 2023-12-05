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

# get mikey turtle to draw our tree
# to get a level 1 tree
# 1. turn so that wilson trutle faces up
# 2. go forward some number of pixels
# 3. turn to the left by 
# 4. tell wilson turtle to turn to the left and draw a level-1 tree
# 5. tell wilson turtle to turn right and draw a level-1 tree
# 6. get wilson turtle to move back to original place
# the turtle stops when the tree reaches zero 

def draw_tree(level: int, height:int) -> None: 
    """A recursive function that draws a tree with initial given length
    
    Params:
    
    level-number representing levels of branches]
    height- height of the main trunk in pixels
    """

    if level > 0: 
        # 1. draw the branch of the tree
              # assume that mikey turtle is facing upwards
        mikey_turtle.forward(height)

        # 2. turn to the left
        mikey_turtle.left(45)
        # 3. draw a smaller tree (current level -1)
        draw_tree(level-1, height/1)
        # 4. turn to the right
        mikey_turtle.right(45)
        # 5. Draw a smaller tree (current level -1)
        draw_tree(level-1,height/1)
        # 6. Move back to beginning
        mikey_turtle.left(45)
        mikey_turtle.back(height)
    else:
        #create a level 0 tree, which is a leaf:
        original_color = mikey_turtle.color()
        mikey_turtle.color("green")
        mikey_turtle.stamp()
        mikey_turtle.color(original_color[0])

# setting mikey to draw a level 0 tree
mikey_turtle.hideturtle()
mikey_turtle.setheading(90)
mikey_turtle.color("brown")
mikey_turtle.width(4)
mikey_turtle.shape("arrow")
mikey_turtle.speed(3)


# [0] = pen color
# [1] = fill color 
 

def draw_fancy_tree(level: int, height:int) -> None: 
    """A recursive function that draws a tree with initial given length
    
    Params:
    
    level-number representing levels of branches]
    height- height of the main trunk in pixels
    """

    if level > 0:
        # 1. draw the branch of the tree
              # assume that mikey turtle is facing upwards
        mikey_turtle.forward(height)
        # 2. turn to the left
        mikey_turtle.left(45)
        # 3. draw a smaller tree (current level -1)
        draw_fancy_tree(level-1, height/2)
        # 4. turn to the right
        mikey_turtle.right(90)
        # 5. Draw a smaller tree (current level -1)
        draw_fancy_tree(level-1,height/2)
        # 6. Move back to beginning
        mikey_turtle.left(45)
        draw_fancy_tree(level-1,height/2)
        mikey_turtle.back(height)
    else:
        #create a level 0 tree, which is a leaf:
        original_color = mikey_turtle.color()
        mikey_turtle.color("green")
        mikey_turtle.stamp()
        mikey_turtle.color(original_color[0])
        
# setting mikey to draw a level 0 tree
mikey_turtle.hideturtle()
mikey_turtle.setheading(90)
mikey_turtle.color("brown")
mikey_turtle.width(4)
mikey_turtle.shape("arrow")
mikey_turtle.speed(3)
draw_fancy_tree(4,150)
mikey_turtle.stamp()
turtle.done()