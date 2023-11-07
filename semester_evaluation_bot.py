# Semester Evaluator bot 
# Author: Emily Song
# 3 November 2023

# Greet user 
print("Hi sharks! I am a semester evaluator bot wanting to gauge your experience with your current semester courses.")

# Ask user how many courses they are taking this semester

course_number = int(input("How many courses are you taking this semester. The course number can include online courses that you are taking this semester! "))

total_rating = 0
course_rating = 0

for i in range (1, course_number + 1):
    total_rating = int(input(f"How do you rate course { i } out of 5? 5 is the best with 1 being the worst."))
total_rating += course_rating 

# Use the average score to represent the average rating of a single course
average_rating_per_course =  total_rating / course_number
average_string = f"{average_rating_per_course:.2f}/ 5"

if average_rating_per_course <= 1: 
    print("Ouch")
elif 1 < average_rating_per_course < 3:
    print("Not a bad semester")
elif average_rating_per_course >= 3:
    print("Glad to hear that!")
else:
    print("sorry the number you inputted is outside of my scope of knowledge")

print("Thank you for your honest feedback!")