# Loop Practice
# Author: Emily
# Date: 10 October 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# Print it out in a pretty way

# e.g. * hot wheels
#  ---
# * lego
#  ---

# define time
import time

# f string allows you to put variables inside the string (evaluate inside a string)
for item in groceries: 
    print(f'*{item}')
    print(" ---")

# Think of item as a variable name, it starts at the first item of the list and goes all the way to the end 
# put two spaces and three dashes after 


# Create a pyramid like this using a for loop

# *
# **
# ***
# ****
# *****

stars = ["*","**","***","****","*****"]
for row in stars:
    print(row)

# Problem:
# Create a new years eve countdown
# Requirements:
# * Starts off at 10
# * Countdown every second
# * Instead of reaching zero it says "Happy New Year"
# Example output:
#   10
#   9
#   8
#   ...
#   1
#   Happy New Year

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!🥳"]
for number in countdown:
        print(number)
        time.sleep(1)
