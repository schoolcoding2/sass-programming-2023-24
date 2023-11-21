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

# Exercise 6: Find how many people come from Guangzhou

with open("./data_example.csv", encoding="utf-8") as f:
    current_list = line.split(",")  
    # convert strings into list
    guangzhou_counter = 1
    for line in f:
        #find if we encounter the word "Guangzhou" 
        if "Guangzhou" in current_list:
            guangzhou_counter += 1
        # add one to the chicken adobo counter
print(f"there are {guangzhou_counter} people who come from Guangzhou.")
            
# Exercise 7: Find how many people have a credit card number that is even. Hint: there are a couple of ways to solve this. You can either do this with the string or with the int.


# Exercise 8: Design a way to find the most popular food. 
with open("./data_example.csv", encoding="utf-8") as f:
    current_list = line.split(",")

    # list of all favourite food option submitted in the file 
    favourite_food = [ "Hamburger", "Chicken Adobo", "Katsudon", "Fish and Chips", "Gyros", "Samosa", "Pad Thai", "Fish Tacos", "Cobb Salad", 
 "Kimchi", "Churros", "Pasta Carbonara", "Ramen", "Falafel", "Croissant", "Goulash", "Mole Poblano","Peking Duck","Sauerbraten",
  "Rendan", "Poutine", "Pav Bhaji", "Tikka Masala", "Pizza", "Butter Chicken","Tandoori Chicken", "Jollof Rice", "Tiramisu",
  "Couscous", "Pho", "Dim Sum", "Moussaka", "Lasagna", "Ceviche", "Croque Monsieur", "Pozole", "Sushi", "Chicken Satay"
  "Biryani", "Pierogi", "Feijoada", "Kebab", "Tacos", "Paella", "Katsudon", "Sashimi", "Baklava"]



     
