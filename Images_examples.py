# Images and Python
# Author: Emily Song
# 11 December 2023

# pip3 install = python image library of modules to use  
#  -- user = we are using the library for personal use 
# pillow = helps us open up the images 

from PIL import Image

    # open up kid green
with Image.open("./Images/kid-green.jpg") as im:

    # grab the pixel in the top left corner
    pixel = im.getpixel((0,0))
    # print the pixel information
print(pixel)


