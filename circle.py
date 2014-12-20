from PIL import Image
import math

WIDTH = 256
HEIGHT = 256

img = Image.new("RGB", (WIDTH, HEIGHT))

def xy_to_r(x, y):
    return sqrt(x**2 + y**2)
    
def polar_to_xy(r, theta, offsetx, offsety):
    return int(r * math.cos(theta) + offsetx), int(r * math.sin(theta) + offsety)
    
def xy_to_theta(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 0
    else:
        return atan(y / x)

def make_circle(im, r, offsetx, offsety, a):
    assert isinstance(im, Image.Image)
    for theta in range(360):
#         xy = polar_to_xy(r * math.sin(a * theta), theta, offsetx, offsety)
#         xy = polar_to_xy(theta / (a + 3), theta, offsetx, offsety)
#         xy = polar_to_xy(a * math.sin(theta), theta, offsetx, offsety)
#         xy = polar_to_xy(r * math.sin(1 * theta), a * theta, offsetx, offsety)
        xy = polar_to_xy(theta / 50, theta, offsetx, offsety)
        im.putpixel(xy, #(256, 256, 256))
                   (int(math.cos(theta) * 256),  
                    int(math.sin(theta) * 256), 
                    int(math.tan(theta) * 256)))
                    
for i in range(10):
    make_circle(img, WIDTH / 2.1, WIDTH / 2, HEIGHT / 2, i)
#     img.show()
    if i < 10:
        img.save("/Users/JacobWunder/Desktop/polar/test/image0%s" % i, format="png")
    else:
        img.save("/Users/JacobWunder/Desktop/polar/test/image%s" % i, format="png")
    del img
    img = Image.new("RGB", (WIDTH, HEIGHT))