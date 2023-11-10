
# Olympic judging bot 
# Author: Emily Song
# 6 November 2023

# Greet user 
print("Hi user, I will be able to help you calculate your score from the corresponding judges. Please input the scores out of ten that you received from each of the five judges. Half points are allowed")

# Ask the user to input the number they recieved from five corresponding judges.

#set the beginning 
judge_1 = float(input("Judge 1 score:"))
judge_2 = float(input("Judge 2 score:"))
judge_3 = float(input("Judge 3 score:"))
judge_4 = float(input("Judge 4 score:"))
judge_5 = float(input("Judge 5 score:"))

average_score = (judge_1 + judge_2 + judge_3 + judge_4 + judge_5)/5

print(f"your average score would be {average_score:.2f}/10")
