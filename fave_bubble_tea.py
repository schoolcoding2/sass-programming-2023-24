# Bubble Tea Popularity Algorithm
# Author: Emily Song
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is
# Print out a summmary of the data
# initialize the variable by setting the starting tally for coco to 0
coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bubble_queen_likes = 0


# Ask the user what their favourite bubble tea is

print("What's your favourite bubble tea place?")
fave_bbt = input().strip(",.?!").lower()


# Tallying counting algorithm 
# Options: CoCo, Chattime, SunTea, Xing Fu Tang, Bubble Queen
# If the user mentions CoCo, increase the counter for CoCo by one, for a total of 5 users inputting their favourite bubble tea place 

if fave_bbt == "coco":
    coco_likes = coco_likes +1 
elif fave_bbt == "chatime":
        chatime_likes += 1
elif suntea_likes == "suntea":
      suntea_likes += 1
elif xingfutang_likes == "xingfutang":
      xingfutang_likes += 1
elif bubble_queen_likes == "bubble queen" or bubble_queen_likes == "bubblequeen":
      bubble_queen_likes += 1


# Print a summary of the results 
print(f'CoCo likes:{coco_likes}')