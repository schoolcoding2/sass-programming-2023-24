# Jelly Bean Colour Counter 
# Author: Emily Song 
# January 9th, 2024

# version 0.1
# - Count red pixels/beans
# - Report on the percentage of all red beans
from PIL import Image 

import colour_helper 

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []


for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):

        current_pixel = jelly_bean_img.getpixel((x, y))

        if colour_helper.pixel_to_name(current_pixel) == "red": 

            red_pixels.append((x, y))

red_pixel_count = len(red_pixels)

print(red_pixel_count)

total_pixels = jelly_bean_img.width * jelly_bean_img.height

print(total_pixels)

red_pixel_percentage = red_pixel_count / total_pixels * 100

print(f"Red Jelly Beans: {round(red_pixel_percentage, 2)}%")