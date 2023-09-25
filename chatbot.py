# Chatbot
# Author: Emily
# Date: 21 September 2023

# Greet the user
print("Hello there!🤖")
print("I am a crude chatbot, here to chat with you")

# Get the user's name and store in a variable
user_name = input("so... what's your name? ")
# Respond with the user's name
print(f"It's nice to meet you, {user_name}!")

# Ask the user what their favourite food is
favourite_food = input("what is your favourite food")

#Respond with something that is NOT TOO repetitive
# Create a list of appropriate responses 
list_of_fave_food_responses = [
    "Mmmm. That sounds Delicious." 
    f" yes, {favourite_food } is one of my favourites too!"
    "Cool."
    "Interesting, I've never tried that before."
]
# Choose one response randomly from the list
import random 
random_response = random.choice (list_of_fave_food_responses)
print(random_response)
# Print out the chosen response



        
# Respond with something appropriate
print(f"nice, I love eating {favourite_food} as well")