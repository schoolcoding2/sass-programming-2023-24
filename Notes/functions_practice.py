# Functions Practice
# Author: Emily
# 24 November 2023


def area_of_square(sidelength: float) -> float:
    """Returns the area of a square with a given sidelength.
    
    Params:
    
    sidelength - length of one side of the square
    """

    area = sidelength * sidelength

    return area


def print_area_of_square(sidelength: float) -> None:
    """Prints out the area of a square with given sidelength.
    
    Params:
    
    sidelength - length of one side of the square
    """

    area = sidelength * sidelength

    print(f"The area of the square is {area} square units.")

# We have two squares (sidelength 14.4 and 120)
# Add both of their areas together
sum_of_areas = area_of_square(14.4) + area_of_square(120)

print(sum_of_areas)

# scope matters: scope = python only sees the code on the outside and not part of the tab
# if two variables are defined the same, python replaces the top variable witht the bottom one
# python reads from left to right and up and down 


# stars(2)  #   **
# stars(10)  #   **********

# print_area_of_a_square(12.2)
# print_area_of_a_square(13)
# sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
# print(area_of_a_square(2))

# print(print_area_of_a_square(2))


# Exercise #1
def stars(num_stars: int) -> str: # this serves as the signature of the code 
    """Return out a string of stars of given length 
    
    Params:
    
    num_stars - the number of stars to return"""

    return "*" * num_stars

print(stars(5))

# Exercise #2
def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """Returns the biggest of three given numbers.

    Params:
    num_one - the first number
    num_two - the second number
    num_three - the third number

    Returns:
    the biggest of the three numbers
    """
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three


# code coverage: tests all branches of the if statement to see if the entire code works 
print(biggest_of_three(1000, 100, 10))
print(biggest_of_three(100, 1000, 10))
print(biggest_of_three(10, 100, 1000))


# Exercise #3 Create function of Pyramid or Pyramid_mirror 
def pyramid(num_layers: int) -> None:
    """Print out a pyramid of stars that is
    the given height.
    
    Params:
    
    num_layers - how many rows are in the pyramid
    """

    for current_layer in range(1, num_layers+1):
        print("*" * current_layer)
        print(stars(current_layer))

pyramid(5)
pyramid(10)


# Exercise 4 Create a Pyramid mirror

def pyramid_mirror(num_layers:int) -> None:
    """Print a pyramid mirrored of given number of layers.
    
    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers+1):
        # Spaces is equal to total num of layers
        # minus the stars in the current layer
        spaces = "" * (num_layers - current_layer)

        print(spaces + stars(current_layer))

pyramid_mirror(2)
pyramid_mirror(20)
pyramid_mirror(20)













