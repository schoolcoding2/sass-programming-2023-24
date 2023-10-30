# Bubble Tea Popularity Algorithm
# Author: Emily Song
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is
# Print out a summmary of the data
# initialize the variable by setting the starting tally for coco to 0

NUM_RESPONDENTS = 5
coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bubble_queen_likes = 0
other_bubble_tea_place = 0



# Ask the user what their favourite bubble tea is

print("What's your favourite bubble tea place?")
for _ in range(NUM_RESPONDENTS): 
      fave_bbt = input().strip(",.?!").lower()
      # Tallying counting algorithm 
      # Options: CoCo, Chattime, SunTea, Xing Fu Tang, Bubble Queen
      # If the user mentions CoCo, increase the counter for CoCo by one, for a total of 5 users inputting their favourite bubble tea place 

      if fave_bbt == "coco":
            coco_likes = coco_likes +1 
      elif fave_bbt == "chatime":
            chatime_likes += 1
      elif fave_bbt == "suntea":
            suntea_likes += 1
      elif fave_bbt == "xingfutang":
            xingfutang_likes += 1
      elif fave_bbt == "bubble queen" or fave_bbt == "bubblequeen":
            bubble_queen_likes += 1
      else: 
             other_bubble_tea_place +=1

      # Print a summary of the results for coco
      print(f'CoCo likes:{coco_likes}')

      # Summary of results for chatime:
      print(f'chatime likes:{chatime_likes}')

      # Summary of the results for suntea
      print(f'sun tea: {suntea_likes}')

      # Summary of the results for xingfutang:
      print(f'xinfutang: {xingfutang_likes}')

      # Summary of the results for bubble queen
      print(f'bubble queen{bubble_queen_likes}')

print(f"coco likes to two decimal places {coco_likes: 2f}")
print(f"chatime likes to two decimal places {chatime_likes: 2f}")
print(f"suntea likes to two decimal places {suntea_likes: 2f}")
print(f"xinfutang likes to two decimal places  {xingfutang_likes: 2f}")
print(f"bubble queen likes to two decimal places  {bubble_queen_likes: 2f}")
print(f"other bubble tea places likes to two decimal places  {other_bubble_tea_place: 2f}")
