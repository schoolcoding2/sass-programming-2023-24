# File exercises 
# Emily Song
# 17 November 2023

# Exercise 1: Open the file (ensuring that encoding parameter is set to "utf-8") and print the contents of the second line in the file
with open("./data_example.csv", encoding="utf-8") as f:

    # go past the first line
    (f.readline())
    # print out the second line
    print(f.readline())

 # Exercise 2: open the file, and print out every line of data.
   # for every line in the file, print f

with open("./data_example.csv", encoding="utf-8") as f:   
    for line in f:  
        print(line)

 
    # Exercise 3: Convert that line of data into a list.
     # For every line of data in our csv file 
        # convert the string to a list

with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        line.split(",")

     
 # Exercise #4: count how many people like "Chicken Adobo" as their favourite food.
with open("./data_example.csv", encoding="utf-8") as f:
    # convert lines to list
    chicken_adobo = 0
    
    
    for line in f:
        current_list = line.split(",")
        
        # find if we encounter the word "chicken Adobo" 
        if "Chicken Adobo" in current_list:
            chicken_adobo += 1
        # add one to the chicken adobo counter
print(f"there are {chicken_adobo} people who like chicken adobo as their favourite food.")

# Exercise 5: Find out how many people have the first letter of their first name start with "A".

with open("./data_example.csv", encoding="utf-8") as f:
    count_a_names = 0 

    for line in f:
        current_list = line.lower().split(",")
        current_name = current_list[0]
        first_letter = current_name[0]

        if first_letter == "a":
            count_a_names += 1  

    print(f"There are {count_a_names} people who have a name starting with 'A'")
        

# Exercise 6: Find how many people come from Guangzhou

with open("./data_example.csv", encoding="utf-8") as f:
    guangzhou_count = 1  

    for line in f:
        current_list = line.split(",") 
        # Check if "Guangzhou" is in the current list
        if "Guangzhou" in current_list:
            guangzhou_count += 1 
    print(f"There are {guangzhou_count} people who come from Guangzhou.")
  
            
# Exercise 7: Find how many people have a credit card number that is even. Hint: there are a couple of ways to solve this. You can either do this with the string or with the int.

with open("./data_example.csv", encoding="utf-8") as f:
    even_credit_card = 0 

    for line in f:
        current_list = line.lower().split(",")
        card_number = current_list[3]
        even_digit_credit_card = current_list[-1]

    if even_digit_credit_card == "0":
            even_credit_card += 1  
    if even_digit_credit_card == "2":
            even_credit_card += 1 
    if even_digit_credit_card == "4":
            even_credit_card += 1 
    if even_digit_credit_card == "8":
            even_credit_card += 1 
print(f"There are {even_credit_card} people who have a credit card number that is even.")


# Exercise 8: Design a way to find the most popular food. 


import csv
from collections import Counter

# Path to the file
file_path = "./data_example.csv"

# List of all favorite food options
favorite_food = ["Hamburger", "Chicken Adobo", "Katsudon", "Fish and Chips", "Gyros", "Samosa", "Pad Thai", "Fish Tacos",
                 "Cobb Salad", "Kimchi", "Churros", "Pasta Carbonara", "Ramen", "Falafel", "Croissant", "Goulash",
                 "Mole Poblano", "Peking Duck", "Sauerbraten", "Rendang", "Poutine", "Pav Bhaji", "Tikka Masala",
                 "Pizza", "Butter Chicken", "Tandoori Chicken", "Jollof Rice", "Tiramisu", "Couscous", "Pho",
                 "Dim Sum", "Moussaka", "Lasagna", "Ceviche", "Croque Monsieur", "Pozole", "Sushi", "Chicken Satay",
                 "Biryani", "Pierogi", "Feijoada", "Kebab", "Tacos", "Paella", "Katsudon", "Sashimi", "Baklava"]

# Read the file and tally the occurrences of each food item
food_counter = Counter()

with open(file_path, encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        for item in row:
            if item.strip() in favorite_food:
                food_counter[item.strip()] += 1

# Find the most popular food item
most_popular_food, occurrences = food_counter.most_common(1)[0]

# Display the result
print(f"The most popular food item is: {most_popular_food} with {occurrences} occurrences.")
  



    
    


     
