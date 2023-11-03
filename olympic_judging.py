# Semester Evaluator bot 
# Author: Emily Song
# 3 November 2023

# Greet user 
print("Hi sharks! I am a semester evaluator bot wanting to gauge your experience with your current semester courses. ")

# Ask user how many courses they are taking this semester

course_number = input("How many courses are you taking this semester. The course number can include online courses that you are taking this semester! ")
print("okay, got it!")

course_number = 0

for i in course_number:
print(f'How do you rate the {course_number + 1} out of 5. 5 is the best with 1 being the worst.")


total_rating = (input().strip(",.?!"))

# Do some math regarding the result
# Use the average score to represent the average rating of a single course
average_rating_per_course= (total_rating / course_number)
average_rating_final = int("{average_rating:.2f} / 5")


# Present the results
if average_rating_final == int(0-1):
    print("Ouch")
elif average_rating_final == int(1.0000001-3):
    print("Not a bad semester")
elif average_rating_final == int(3.00000001- 5):
    print("Glad to hear that!")

# The end
 print("Thank you for your feedback")