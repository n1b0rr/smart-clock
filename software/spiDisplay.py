import st7565
import time
import xglcd_font as font
import math


def spiDisplayInit():

	"""
	Initialize the Display communication and setup the font
	"""

	glcd.init()
	glcd.send_command([0x60]) #PATCH for smart-clock ST7565R display
	glcd.set_contrast(0)

#define neato font
neato = font.XglcdFont('/home/pi/Pi-ST7565/fonts/Neato5x7.c', 5, 7)

#create lcd object
glcd = st7565.Glcd(rgb=[21, 20, 16])

spiDisplayInit()
    
def write(x, y, ctx):

	"""
	Write text to coordinate (x,y)
	"""
	glcd.clear_back_buffer()
	glcd.draw_string(ctx, neato, x,y)
	glcd.flip()
	
	

