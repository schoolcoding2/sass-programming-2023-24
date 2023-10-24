# Star wars dark side decider bot
# Author : Emily Song 
# Date October 16th, 2023 -....


# Bot greets user
print("Hi there, I am the almightly fortune teller that you have been looking for")

# Bot announces that it can determine is a person can join the dark side
print(" I will decide if you can join the dark side.")
import time

# The decision will be based off of user response, if they answer yes to any of the questions they can join the dark side:
# Ask the first question asking if the user likes the colour red
like_red = input(f'do you like the colour red?')



#Asks the second question asking if the user likes capes
like_cape = input(f'do you like capes?')

if like_red.lower().strip("!.,?") == "yes" or like_cape.lower().strip("!.,?") == "yes":
    print("Dark side it is!")
elif like_red.lower().strip("!.,?") == "no" and like_cape.lower().strip("!.,?") == "no":
    print("Light side, I see")
else:
    print("Light side it is")    



