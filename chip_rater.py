# Chip rater
# Author: Emily Song
# 2 November 2023

# Interview people about their perpection on how delicious potato chips are
# We will ask participanst a set of questions and give them an aggregate score

# Greet the user (make sure to be as friendly as possible as the subjects are research subjects)
print("Thank you for participating in our study! Please answer the following questions on the chip you just ate")

# Create a list of questions to ask
questions = [
"How crispy is the chip on the scale from 1 to 5? 5 is very crispy, 1 is mushy.",
"How would you rate the taste from 1 to 5? 5 is best chip ever. 1 is I'd rather eat dirt.",
"From 1 to 5, how would you rate the packaging? 5 is with highest regard. 1 is with low regard for the packaging."
]

total_rating = 0

# For every question in that list
for question in questions:
    print(question)

    # Get the user's rating 5

    user_rating = int(input().strip(",.?!"))

    # Add the rating to some total-rating 
    total_rating += user_rating 



# For every question in that list
    # Ask the question
    # Get the user's rating
    # Add the rating to some total-rating

# Do some math regarding the result
# Use the average score to represent the chip's rating.
average_rating = total_rating / len(questions)

# len is a function that will give you how big a list is, how big a function is


# Present the results
int(f'The average rating for this chip is: {average_rating:.2f} / 5')
# .2 = two decimal places
# f = float




