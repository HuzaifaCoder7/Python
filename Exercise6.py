
#! Program that converts all the files to specific name in Python

import os

folder = "C:/Users/amjad/Pictures/Screenshots"

count = 0
for file in os.listdir(folder):
    dst = f"{count}.png"
    src = f"{folder}/{file}"
    # print(src) #! It lists all the picture in the folder
    dst = f"{folder}/{dst}"
    os.rename(src,dst)
    count = count + 1