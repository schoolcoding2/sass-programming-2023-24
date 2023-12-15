# Images and Python
# Author: Emily Song
# 11 December 2023

# pip3 install = python image library of modules to use  
#  -- user = we are using the library for personal use 
# pillow = helps us open up the images 

from PIL import Image


def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    if red < 140 and blue < 140 and green > 145:
        return "green"
    
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
    image_height = im.height
    image_width = im.width

    # open background image
    bg_im = Image.open("./Images/beach.jpg")

    # starting at the top and working our way down
    # visit the pixels from left to right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))

            if pixel_to_name(pixel) == "green":
                # replace it with bg_im pixel in same location 
                bg_pixel = bg_im.getpixel((x, y))

                im.putpixel((x, y), bg_pixel)

 # REMEMBER TO CLOSE THE IMAGE WHEN DONE
    bg_im.close()

    # Save image
    im.save("./Images/output.jpg")