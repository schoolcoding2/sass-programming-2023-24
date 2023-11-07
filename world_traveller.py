# World Travellor bot 
# Author: Emily Song
# 6 November 2023

# Greet user

travellor_name = input(" Hi fellow travellor, what is your name")
print(f'Hi {travellor_name}, it is nice to meet you')

continent_list =  ["Asia", "Africa", "North America", "South America", "Antarctica", "Europe", "Australia"
                   ]

total = 0

for continent in continent_list:
# Ask the user if they've travelled to this continent
    print(f"Have you visited {continent}?")

# Get their response
    response = input().strip().lower()

# If their response is yes
    if response == "yes":
        # Add one to the total
        total += 1
    
# print to total number of countries that user has travelled to 
print(f" Oh, so you have travelled to {total}/7 countries")


