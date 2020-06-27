from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import random

#change this value to change the number of files you wish to create
runs = 1

#image number counter, will be displayed in the name of the generated files
imageid = 0

# just create an empty sample.jpg file in paint
file_name = "sample.jpg"

#function for random RGB values between 0 and 255
def randomRGBvalue():
    x = random.randint(0,255)
    return x

#loop to generate the number of pictures you need
while imageid < runs:
    
    # These three lines randomize the background color
    background_R = randomRGBvalue()
    background_G = randomRGBvalue()
    background_B = randomRGBvalue()
    
    # creates a imagefile wiht the size 550x500px 
    im = Image.new('RGB', (500, 500), (background_R, background_G, background_B))
    draw = ImageDraw.Draw(im)
    
    # random background color for the object
    rectangle_R = randomRGBvalue()
    rectangle_G = randomRGBvalue()
    rectangle_B = randomRGBvalue()
    
    # checking if background color is rectangle color
    if rectangle_R == background_R and rectangle_B == background_B and rectangle_G == background_G:
        
        # if the colors match, the object gets recolored
        rectangle_R = randomRGBvalue()
        rectangle_G = randomRGBvalue()
        rectangle_B = randomRGBvalue()
        
    # Size restrictions, can be changed at will
    leftmargin = random.randint(5,250)
    rightmargin = random.randint(255,495)
    topmarg =random.randint(5,250) 
    botmarg = random.randint(255,495)
    
     # shape being drawn onto the file
    draw.rectangle((leftmargin, topmarg, rightmargin, botmarg), fill=(rectangle_R, rectangle_G, rectangle_B), outline=(0,0,0))
    
    # here is the filename, change to what you want, includes number of image generated
    file_out = "rectangle" + str(imageid) + ".jpg"
    
    # image being saved
    im.save(file_out, quality=95)
    
    # counter for the while-loop and image number
    imageid = imageid + 1