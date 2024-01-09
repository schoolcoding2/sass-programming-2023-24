# Winter Holidays
# Author: Emily Song 
# January 8th, 2024

# Requirements:
# - create a function called winter_holidays()
# - take a parameter
#   - string
# - return a summary of an event from your holidays

import random

def winter_holidays(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
       
    Params:
    good_or_bad - indicate what kind of event to summarize 
      
    Returns:
    an event that happened during the holidays; the event is selected randomly based on the parameter"""
    
    if good_or_bad.lower() == "good":
        winter_events = [
            "very good, I went to go shopping for winter formal dresses",
            "It was well. I ate hot pot and celebrated my grandma's birthday",
            "I got a beautiful necklace for Christmas"
        ]
        return random.choice(winter_events)
    elif good_or_bad.lower() == "bad":
        winter_events = [
            "Unfortunately, I did not sleep much", 
            "I spent a lot of money on university applications"
        ]
        return random.choice(winter_events)
    else:
        return "Invalid input. Please specify 'good' or 'bad'."

# Ask user for their winter break events/summary 
user_input = input("Was your winter holiday experience good or bad? ").strip()

# Get a random event based on the user input
print(winter_holidays(user_input))

