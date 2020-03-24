import glob
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
import random

# change directory
os.chdir('C:/Users/ZainbaMuhdYunus/Desktop/py_images')

# declare fontsFolder
my_image = 'ges-4.JPG'
fontsFolder = 'C:/Windows/Fonts'

# csv file to be used
a = pd.read_csv('try.csv')

# choose keys or colons
album = a.AlbumID
topics = a.Topics

fontsFolder = 'fontsfolder'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 24)

index = 0
for i,j in zip(album,topics):
    img = Image.open(my_image)
    draw = ImageDraw.Draw(img)

    draw.text((80,70), str(i), font=arialFont, fill=('white') )
    draw.text((80,150), str(j), font=arialFont, fill=('white'))

    # index = random.randrange(1,1000)
    index = index + 1
    full_name = str(index) + '.jpg'
    img.save(full_name)


   