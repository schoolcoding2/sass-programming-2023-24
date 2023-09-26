# Chatbot
# Author: Emily
# Date: 21 September 2023

import random
import time

# Greet the user
# pause in between lines of dialogue
print("Hello there!🤖")
time.sleep(2)
print("I am a crude chatbot, here to chat with you")
time.sleep(1.5)

# Get the user's name and store in a variable
user_name = input("so... what's your name? ")
# Respond with the user's name
print(f"It's nice to meet you, {user_name}!")

# Ask the user what their favourite food is
favourite_food = input("what is your favourite food")
time.sleep(2)

#Respond with something that is NOT TOO repetitive
# Create a list of appropriate responses 
list_of_fave_food_responses = [
    "Mmmm. That sounds Delicious.😽",

    f" yes, {favourite_food } is one of my favourites too!👍",
    "Cool.🫵",
    "Interesting, I've never tried that before.👀"]

# Choose one response randomly from the list

list_of_fave_food_responses[2]

random_response = random.choice (list_of_fave_food_responses)
print(random_response)
# Print out the chosen response

time.sleep(1.5)
        
# Respond with something appropriate
print(f"nice, I love eating {favourite_food} as well")