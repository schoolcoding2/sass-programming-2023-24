# SFU Best - Similarity Score Expanded 
# Author: Emily Song
# 10 November 2023

# Load data from a file
#"Read it in a meaningful way"
# Link our sim score algorithm to the data

# Open the file 
with open("./data.csv") as f:

# . = in same folder ./ separates the dot from the file name
# With gives the variable a container 
# we want to open up the file, open up the stream, and then be able to close the file/data
# only want to keep the file data open for as long as we need to prevent any issues


# python has an imaginary pointer at the first line
# get the first line of data:
    print(f.readline())

# The second line of csv file
    print(f.readline())



# Create a "profile" of likes (fave places in SFU)
# For every line of data in our cvs file

# The conversion between string to list is a step we need to do prior to applying our algorithm

# For item in profile
# If item in current line's likes 
# Increase sim score by 1 

profile = [ "Bubble world", "Chef Hung", "Uncle Fatih's", "Guadalupe (MBC)", "Steve's Poke Bar"]

# Initiative top score and their name
most_similar_score = 0
most_similar_name = ""
least_similar_score = 6
least_similar_name = ""


with open ("./data.csv") as f:
    # Throw away the header
    header = f.readline()
    
    for line in f: 
        # For every line of data in our csv file 
        # convert the string to a list
        current_likes = [item.lower() for item in line.split(",")]
        
        # Store the person's name
        current_name = current_likes[1]

        # the person's name is the second piece of information RECALL THAT PYTHON STARTS COUNTING FROM 0
        current_sim_score = 0

        # sim score algorithm
        for item in profile:
            if item.lower() in current_likes:
                current_sim_score += 1

        # Print the result from this line of data
        print(f'{current_name} - score: {current_sim_score}')
        
        # Update the most similar person
        if current_sim_score > most_similar_score:
            most_similar_score = current_sim_score
            most_similar_name = current_name

        # Update the least similar person
        if current_sim_score < least_similar_score:
            least_similar_score = current_sim_score
            least_similar_name = current_name

    
print("🥇🥇🥇🥇 Most similar person! 🥇🥇🥇🥇")
print(f'{most_similar_name} - score: {most_similar_score}')


print("🎖️🎖️Least similar person🎖️🎖️ ")
print(f'{least_similar_name} - score: {least_similar_score}')