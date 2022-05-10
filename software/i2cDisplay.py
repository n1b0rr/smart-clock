
import os

# libraries for oled display
from board import SCL, SDA
import busio
import adafruit_ssd1306

# library for making images
from PIL import Image, ImageDraw, ImageFont, GifImagePlugin


i2c = busio.I2C(SCL,SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128,64,i2c)
font = ImageFont.truetype("fonts/liberation.ttf", size=12)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height

# make an empty image on which you can write things on,
#this image will be displayed at a continious rate per second
image = Image.new("1", (width, height), color=0)
clear = Image.new("1", (width, height), color=0)

def write(x, y, ctx):
    """ 
    Write to the display directly.

    Returns
    -------
    None.
    """
    
    draw = ImageDraw.Draw(image, "1")
    draw.rectangle((width, height,0,0), fill=(0))
    draw.text((x, y), ctx, font=font, fill=255)
    disp.image(image)
    disp.show()

def write_buffer(x, y, ctx):
    """
    Write things to a buffer to send it to the display after. 

    Returns
    -------
    None.
    """
    try:
        draw.text((x*6,y*12), ctx, font=font, fill=255)
    except:
        draw = ImageDraw.Draw(image, "1")
        draw.text((x*6,y*12), ctx, font=font, fill=255)

def send_buffer():
    """ 
    Send buffer to display.

    Returns
    -------
    None.
    """
    disp.image(image)
    disp.show()
    draw = ImageDraw.Draw(image, "1")
    draw.rectangle((width, height,0,0), fill=(0))


