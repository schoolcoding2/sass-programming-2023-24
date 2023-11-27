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


def area_of_square(sidelength: float) -> None:
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


# stars(2)  #   **
# stars(10)  #   **********

# print_area_of_a_square(12.2)
# print_area_of_a_square(13)
# # sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
# print(area_of_a_square(2))

# print(print_area_of_a_square(2))