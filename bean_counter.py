# Jelly Bean Colour Counter 
# Author: Emily Song 
# January 9th, 2024

# version 0.1
# - Count red pixels/beans
# - Report on the percentage of all red beans

# version 0.2
# - Count green pixels/beans
# - Report on the percentage of all green beans

# version 0.3
# - Count yellow pixels/beans
# - Report on the percentage of all yellow beans


from PIL import Image

import colour_helper

blue= (0,0,250)

green_pixels = []

blue_pixels = []

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        # Get the pixel information
        current_pixel = jelly_bean_img.getpixel((x, y))

        # If this pixel is red
        if colour_helper.pixel_to_name(current_pixel) == "red":
            # Store its location somewhere
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_name(current_pixel) == "jelly bean green":
            green_pixels.append((x,y))
        elif colour_helper.pixel_to_name(current_pixel) == "jelly bean blue":
            blue_pixels.append((x,y))

# Create a map of all red pixels "found"
# Create a new image that stores the map
# - the new image should be the same size as the original
orig_image_width = jelly_bean_img.width
orig_image_height = jelly_bean_img.height 

blue_pixel_map = Image.new("RGB", (orig_image_width, orig_image_height))
          
# For every pixel in the red_pixels list
# Place a red pixel at that location
for pixel_loc in green_pixels:
    blue_pixel_map.putpixel(pixel_loc, BLUE PIXELS)

# Save the image
blue_pixel_map.save("./Images/green_pixel_map.jpg")
blue_pixel_map.close()

# Count all the locations of red pixels
red_pixel_count = len(red_pixels)
green_pixel_count = len(green_pixels)
blue_pixel_count = len(blue_pixels)
total_pixels = jelly_bean_img.width * jelly_bean_img.height

# Divide by the total pixels in the image
red_pixel_percentage = red_pixel_count / total_pixels * 100
green_pixel_percentage = green_pixel_count / total_pixels * 100
blue_pixel_percentage = blue_pixel_count / total_pixels * 100

# Generate the report
print(f"Red Jelly Beans: {round(red_pixel_percentage, 2)}%")
print(f"Green Jelly Beans: {round(green_pixel_percentage, 2)}%")
print(f"Blue Jelly Beans: {round(blue_pixel_percentage, 2)}%")
print(blue_pixels)
jelly_bean_img.close()

