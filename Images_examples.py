# Images and Python
# Author: Emily Song
# 11 December 2023

# pip3 install = python image library of modules to use  
#  -- user = we are using the library for personal use 
# pillow = helps us open up the images 

from PIL import Image
import time
def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    if red < 25 and blue < 25 and green > 249:
        return "green"
    else:
        return "colour unknown"

# open up kid green
with Image.open("./Images/kid-green.jpg") as im:

    # grab the pixel in the top left corner
    pixel = im.getpixel((0,0))
    # print the pixel information
print(pixel)

# grab the middle pixel 
middle_coord = im.width //2 

# use // (floor division) so our answers are integers
# divide by 2 to get middle coordinates

pixel = im.getpixel((middle_coord, middle_coord))
print(pixel)


# print the pixel information


# December 14th, 2023 


# open up kid green 
with Image.open("./Images/kid-green.jpg") as im:
    # create variables that store the width and height 
    Image_height = im.height
    Image_width = im.width

    # open background image
    bg_im = Image.open("./Images/beach.jpg")

    # *** REMEMBER TO CLOSE THE IMAGE WHEN DONE


    # starting at the top and working our way down
    for y in range(Image_height):
        # visit the pixels from the left to right
        for x in range(Image_width):
        # print this pixel's information 
            pixel = im.getpixel((x,y))
            
            if pixel_to_name(pixel) == "green":
            # replace it with bg.pixel in same location 
                bg_pixel = bg_im.getpixel((x,y))

                im.putpixel((x,y), bg_pixel)


# *** REMEMBER TO CLOSE THE IMAGE WHEN DONE
bg_im.close()

# Save the image 
im.save("./Images/output.jpg")

