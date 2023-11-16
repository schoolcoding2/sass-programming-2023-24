# Similar hobby calculator
# Author: Emily
# Date: 14 November 2023

import time

# Greet the user
print("Hi there, I am a similarity hobbies calculator! I can calculate the similarity between two people's hobbies. In order for me to do so, please tell me your name and list your hobbies out separated using spaces!")
time.sleep(1.5)

# ask person A and person B their names
person_a_name = input("What is your name person A ?")
person_b_name = input("What is your name person B?")

# ask person A and person B their list of hobbies, ensure that they are saparated by commas
# .split changes the answer from one entity of being a string to each indivdual entity as a list!

person_a_hobbies = input(f"{person_a_name}: what's your favourite hobby ?").split(" ")
person_b_hobbies = input(f"{person_b_name}: what's your favourite hobby ?").split(" ")

similarity_score = 0

for hobby in person_a_hobbies:
  if hobby in person_b_hobbies:
    similarity_score += 1


print (f"{person_a_name} and {person_b_name} you have a similarity score of {similarity_score}")
















