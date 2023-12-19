# Image Helper 
# Author: Emily Song 
# 19 December 2023

from PIL import Image
def is_light(pixel: tuple) -> bool:
    """Returns true if the pixel is a "light" pixel
    Params:
        pixel - 3-tuple of values r, g, b
    red, green, blue = pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    average = (red + green + blue) / 3
    if average >= 128:
        return True
    else:
        return False
    return
# Test?
light_pixel = (200, 200, 200)
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)
print(is_light(light_pixel))
print(is_light(light_gray))
print(is_light(dark_pixel))
print(is_light(dark_gray))
# Open up the image
# For every pixel in the image
    # if the pixel is light
        # replace it with a light pixel
    # else
        # replace it with a dark pixel
# after visiting every pixel, save the image
with Image.open("./Images/catto (1).png") as im:
 for y in range(im.height):
        for x in range(im.width):
             pixel = im.getpixel((x, y))
             if is_light(pixel):
                 im.putpixel((x, y), light_pixel)
             else:
                im.putpixel((x, y), dark_pixel)
im.save("./Images/binarized.jpg")










