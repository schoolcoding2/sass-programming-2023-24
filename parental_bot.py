# Parental bot 
# Author: Emily Song
# Date: 16 November 2023

import time

# greet the user and ask the user four questions
print("Hi there, I am a parental bot to ensure that you, my child, are on the right track")
time.sleep(1.5)

parental_questions = [ "Did you eat?", "Did you study?", "Did you do your laundry?", "Did you call grandma?"]

# initialize the parental score:
parental_score = 0

# ask each question from list from user
for question in parental_questions:
    # print out each question from list 
    print(question)
    
    #ask user for their response for each question
    user_response = input()

    #if user responds with "yes"
    if user_response == "yes":
        parental_score += 1
    # increase parental score by 1 


# if parental score is 0 then respond with "i'm coming over", if score is between 1 and 2 then respond with "ok", if score is between 2 and 3 then respond with "Good!"
if parental_score == 0: 
    print("I'm coming over")
elif 1 <= parental_score <= 2:
        print("Ok")
elif  3 <= parental_score <= 4:
        print("Good!")
else:
        print("sorry the number you inputted is outside of my scope of knowledge")

# "" quotation = string
# () = function being employed