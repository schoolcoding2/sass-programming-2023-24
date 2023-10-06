# Food Suggestion Bot
# Author: Emily 
# Date: 6 October 2023

# A bot that asks the user what their favourite food is
# The bot identifies the type/cuisine of the food and offer a suggestion for a restaurant

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, i am here to suggest a restaurant to you.")
time.sleep(1)

fave_food = input("To help me suggest a restaurant, tell me what your favourite food is.")
time.sleep(1)

# If they answer with an Italian dish
# Suggest an Italian restaurant
# List all the Italian dishes

italian_food = ["pizza","pasta","canneloni","tiramisu" ]
if fave_food.lower().strip(",.?!") in italian_food:
    print("I think that you may like Italian food. 🍝")
    time.sleep(1)
    print("I suggest Bella Roman Italian Ristorante Richmond ")
    time.sleep(1)
    print("You can find the address below:")
    time.sleep(1)
    print("8368 Alexandra Rd, Richmond")

# Add one more cuisine/type/etc. -> Chinese food
# Test it out to see if it works
chinese_food = ["dumplings", "fried rice", "buns", "mooncake", "rice", "wonton"]
if fave_food.lower().strip(",.?!") in chinese_food:
    print("I highly recommend trying out some Chinese food")
    time.sleep(1)
    print("There's a good resturant called Mui Garden Restaurant Richmond")
    time.sleep(1)
    print("The address is 5960 Minoru Blvd, Richmond")
    time.sleep(1)
    print("I hope you enjoy!")
else:
    print("Sorry, I don't recognize your favourite food.")
    print("The algorithm is still being worked on")
    print("I can't offer a good suggestion for you")

