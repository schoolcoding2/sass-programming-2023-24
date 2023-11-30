# Advent Calendar
# Author: Emily Song
# November 30th,2023

# There is one elf carrying the most calories
# How many does that one have?

# Open the file
# create a list that holds all the calories of the elves
elves = []
# Calories of the current elf
current_cals = 0

with open("./aoc2022day1.txt") as f:

    for line in f: 
        # If there is something in the line
        if line.strip():
            current_cals += int(line.strip())
            # converts the string to integer 
        else: 
            # dump current_cals into elves list
            elves.append(current_cals)

            # reset current_cals for next 
            current_cals = 0


print(current_cals)

# Find the biggest calories in the list:
biggest_cals = 0
for elf in elves: 
    if elf > biggest_cals:
        biggest_cals = elf

print(biggest_cals)
print(max(elves))


# Exercise #2

# Find the elf with the most calories in the list
sorted_elves = sorted(elves)
print(elves)
print(max(elves))
print(sum(sorted(elves)[-3:]))
top_three = sorted_elves[-3:]
top_three_total= sum(top_three)
