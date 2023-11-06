# McDoland's program
# Author: Emily Song
# 3 November 2023

#Greet the user
print("Hi there, welcome to McDoland's!")

# Ask user if they would like a burger 
user_burger = input("Would you like our signature $5 burgers?").lower().strip(",.?!")

# Ask user if they would want fries for $3

user_fries = input("Would you like our signature $3 fries?").lower().strip(",.?!")

# calculate total cost with 14% tax 

if user_burger == "yes" and user_fries == "no":
   print(f"Your total will be ${5.00*1.14}") 
elif user_burger == "yes" and user_fries == "yes":
   print(f"Your total is ${8*1.14}")
elif user_burger == "no" and user_fries == "yes":
   print(f"Your total will be ${3.00*1.14}") 
elif user_burger == "no" and user_fries == "no":
   print("okay, let me know if you ever decide to change your mind")
else:
    print("okay then. The next server will be able to accommodate for your order. Thank you for your patience")

   