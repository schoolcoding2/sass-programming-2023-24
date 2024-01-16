# Spotify Analyzer
# Author: Emily Song
# Date: January 16th, 2024

# Version 0.1 

# open up the file
with open("./spotify.csv") as f:


# ---- look for all songs performed by Drake

# Use linear search 
# Create a  csv reader object
    csv_reader = csv.DictReader(f)

# Create a list to store all Drake's songs
drake_songs = []

# Create a counter for the current line number 
line_num = 0

# For every song in the .csv file
for line in csv_reader:
    # Check if it's the first line
    if line_num == 0:
    # print out the names of the columns 
        print(line)

        line_num += 1
# From the data set, get all the songs

# Create a list to store all Drake's songs
drake_songs = []
# for every song in the .csv file
for line in csv_reader:
    if "drake" in line["artist"].lower():

# if this song is sung by Drake add it to the Drake's songs list
        drake_songs.append(
            (line["artist"], line["song_title"], line["danceability"])
        )

for song in drake_songs:
    print(song)
# recall that we previously worked with a .csv file with sfu best file
# refer to line 26 (least and most similar score portion)


