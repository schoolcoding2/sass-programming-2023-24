# Calculating similarity score
# Author: Emily Song
# 9 November 2023

# Calculate the similarity scores between two people

# Create two lists that represent the movies that they like
ubials_fave_movies = ["the matrix", "avengers: infinity wars", "inferno affairs", "rogue one", "the empires strikes back"]
bens_fave_movies = ["thomas and friends, big world big adventure", "paddington 2", "avengers: infinity war", "minions", "rogue one"]

# always seperate each entity with commas. 

similarity_score = 0
# Increase similarity score if movies are the same
for movie in ubials_fave_movies:
    if movie in bens_fave_movies: 
        similarity_score += 1

# Displays the results
print(f"The similarity score between the user is:")
print(similarity_score)

# all the data is normalized so the capitalization and lower case information does not count 

# compares two data points

