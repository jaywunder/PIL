from PIL import Image
from PIL import ImageFilter
from math import cos, sin, tan, atan, sqrt

WIDTH = 256
HEIGHT = 256

def xy_to_r(x, y):
    return sqrt(x**2 + y**2)
    
def xy_to_theta(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 0
    else:
        return atan(y / x)

img = Image.new("RGB", (WIDTH, HEIGHT), color=(120, 120, 120))
rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0 )
copy_to = Image.new("RGB", (WIDTH, HEIGHT))
for x in range(WIDTH):
    for y in range(HEIGHT):
        img.putpixel(
            (x, y),
            (int(cos(x) * WIDTH),
             int(sin(y) * HEIGHT),
             128#int(tan((y + 1) / (x + 1) ))
             )
        )
loaded = Image.open("/Users/JacobWunder/Desktop/alex.png")
loaded.load()

out = loaded.convert(matrix=rgb2xyz)
out.show(title="Image")
