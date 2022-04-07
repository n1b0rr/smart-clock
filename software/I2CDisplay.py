import os

# libraries for oled display
from board import SCL, SDA
import busio
import adafruit_ssd1306

# library for making images, to display
from PIL import Image, ImageDraw, ImageFont, GifImagePlugin

# neccesary for global variables
disp = 0
font = 0
width = 0
height = 0
image = 0


def initDisplay():  
# neccesary for global variables
    global disp
    global width
    global height
    global image
    global font

    i2c = busio.I2C(SCL,SDA)

    disp = adafruit_ssd1306.SSD1306_I2C(128,64,i2c)
    font = ImageFont.load_default()

    disp.fill(0)
    disp.show()

    width = disp.width
    height = disp.height

    # make an empty image on which you can write things on,
    #this image will be displayed at a continious rate per second
    image = Image.new("1", (width, height), color=0)

def write(x, y, ctx):
    draw = ImageDraw.Draw(image)
    draw.text((x, y), "Hello world", font=font, fill=255)
    disp.image(image)
    disp.show()

