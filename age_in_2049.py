# Age in 2049
# Author: Emily Song
# 2 November 2023

import time
import random

# Introduce the objective to the user/ greet the user
print("Hi there, I am here to help you calculate your age by the year 2049! The answer will be based on the exact day at the time that you input your age. If your birthday has yet to occur then similarily the calculation will give you your age in 2049 without your birthday passing.")


# Ask the user their age
user_age = int(input("What is your current age? "))

user_age += 26

# print out a response 
print(f' Based on my calculations, you will be {user_age} on this same month and date in year 2049')



