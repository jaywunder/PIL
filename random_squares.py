import PIL
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
from random import randint, choice
import math

# WIDTH = 256 * 5
# HEIGHT = 256 * 5
WIDTH = 3840
HEIGHT = 2160

im = Image.new("RGB", (WIDTH, HEIGHT), color=(255, 255, 255))

def makeSquares(im, minR=0, rangeR=255, minG=0, rangeG=255, minB=0, rangeB=255):
    ## Makes the random squares
    draw = ImageDraw.Draw(im)
    length = int(HEIGHT / 10)
    x = 0
    y = 0
    numList = [1, 1, 1, 1, 1, -1,]
    for i in range(10000):
        vx = int(length / choice([2, 4])) * choice(numList)
        vy = int(length / choice([2, 4])) * choice(numList)
        x += vx
        y += vy
        
        if x < 0:
            x = 0
        elif x > WIDTH:
            x = 0
        if y < 0:
            y = 0
        elif y > WIDTH:
            y = 0
    #normal
        pos = [x, y, x + length, y + length]
        color = (randint(minR, minR + rangeR), 
                 randint(minG, minG + rangeG),
                 randint(minB, minB + rangeB))
#         color = (int(y / HEIGHT * 128 + 100), 
#                  int(y / HEIGHT * 128), 
#                  int(y / HEIGHT * 0))
                 
#         if randint(0, 10) == 3:
#             color = (int(y / HEIGHT * 128 + 8), 
#                  int(y / HEIGHT * 20), 
#                  int(y / HEIGHT * 128 + 16))
#         if randint(0, 10) == 3:
#             color = (int(y / HEIGHT * 128 + 16), 
#                  int(y / HEIGHT * 20), 
#                  int(y / HEIGHT * 128 + 8))
        draw.rectangle(pos, fill=color)


##   TURQUOISE
makeSquares(im, 
              minR=256 / 16,
            rangeR=256 / 8,
              minG=256 / 4, 
            rangeG=256 / 4,
              minB=256 / 4, 
            rangeB=256 / 4)
im.save("/Users/JacobWunder/Documents/PIL/random_squares/turquoise.png", "PNG") 

##   PURPLE
# makeSquares(im, 
#               minR=int(256 / 16),
#             rangeR=int(256 / 8),
#             
#               minG=int(256 / 38), 
#             rangeG=int(256 / 20),
#             
#               minB=int(256 / 16), 
#             rangeB=int(256 / 8))
# im.save("/Users/JacobWunder/Documents/PIL/random_squares/purple.png", "PNG") 

##  MAROON
# makeSquares(im, 
#               minR=int(32),
#             rangeR=int(128),
#             
#               minG=int(0), 
#             rangeG=int(0),
#             
#               minB=int(0), 
#             rangeB=int(0))
# im.save("/Users/JacobWunder/Documents/PIL/random_squares/maroon.png", "PNG") 

##  RANDOM
# makeSquares(im, 
#               minR=int(64),
#             rangeR=int(128 + 64),
#             
#               minG=int(64), 
#             rangeG=int(128 + 64),
#             
#               minB=int(64), 
#             rangeB=int(128 + 64))
# im.save("/Users/JacobWunder/Documents/PIL/random_squares/___.png", "PNG")

        
im.show()
