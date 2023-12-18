# Is light bot -Image Problem
# Author: Emily Song 
# 18 December 2023

from PIL import Image

def is_light(pixel:tuple) -> bool:
    """ Returns Turn if the pixel is a "light" pixel

    Params:
        pixel - 3-tuple of values r, g, b

    Returns:
        True if the pixel is a light pixel
        False if a dark pixel


    """

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) /3

    if average >= 128:
        return True

    else: 
        return False

# Test
light_pixel = (255,255,255)
light_gray = (128,128,128)
dark_gray = (127,127,127)
dark_pixel = (0,0,0)

# pixels go from 0 to 265 with 265 being the darkest
print(is_light(light_pixel)) # True 
print(is_light(light_gray)) # True
print(is_light(dark_gray))  # False
print(is_light(dark_pixel))  # False

    # open up the cat image 

    # for every pixel in the image:
    # if the pixel is light
    # replace it with a light pixel
    # else, replace it with a dark pixel 

    # after visiting every pixel, save the image 

    # save photo as binormizedimage.pjg)
   
    # open up cat image 
# Open the image
with Image.open("./Images/catto.jpg") as im:
    # For every pixel in the image
    for y in range(im.height):
        for x in range(im.width):
            pixel = im.getpixel((x, y))

            # if the pixel is light
            # else
            # replace it with a dark pixel
            if is_light(pixel):
                im.putpixel((x, y), light_pixel)
            else:
                im.putpixel((x, y), dark_pixel)
    

    # After visiting every pixel, save the image
    im.save("./Images/binarized.jpg")