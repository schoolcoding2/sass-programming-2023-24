# Spotify Analyzer
# Author: Emily Song
# Date: January 16th, 2024

# Version 0.1 
# From all the data set, get all the songs performed by Drake

import csv

# Open up the file
with open("./spotify.csv") as f:
    # ---- Look for all songs performed by Drake
    #      Use linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Create a list to store all Drake's songs
    drake_songs = []

    # for every song in the .csv file
    for line in csv_reader:
        if "drake" in line["artist"].lower():
            # add it to the Drake's songs list
            drake_songs.append(
                (line["artist"], line["song_title"], line["danceability"])
            )

for song in drake_songs:
        print(song)


# --- Sorting Algorithm (lowest to highest)
# --- Selection Sort
        
        # starting at the beginning of the list moving to the end (set the current item to the smallest value)
for i in range(len(drake_songs)):
    # set the current item to the smallest value
    smallest_danceability = drake_songs[i][-1]
    smallest_index = i

    # for the rest of the list
    for j in range(i+1, len(drake_songs)):
        if drake_songs[j][-1] < smallest_danceability:
            smallest_danceability = drake_songs[j] [-1]
            smallest_index = j 


        # note: danceability lives at -1 or 2 in the file 

# Swap the current position with the smallest number we found:
    drake_songs[i], drake_songs[smallest_index] = drake_songs[smallest_index], drake_songs[i]


# Print out all songs that have
print("--- Sorted Drake Songs by Danceability")
for song in drake_songs:    
    print(f"{song[1]}:  {song[2]}")

    # t = tab the \t can be substituted by a space or any entity you may choose
    # there is going to be two loops (outer loop and inner loop)

    # outerloop keeps track of what is sorted and what is not

# note: recall that we previously worked with a .csv file with sfu best file


# The list is currently in ascending order, now sort the list according to descending order
    

    

