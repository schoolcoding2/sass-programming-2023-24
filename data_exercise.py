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

 
 # Exercise 3: Convert that line of data into a list.

    people_likes = ("Favourite Food", "Favourite Movie" ,"Credit Card Num" ,"City")

    for line in f: 
        # For every line of data in our csv file 
        # convert the string to a list
        people_likes = [item.lower() for item in line.split(",")]


