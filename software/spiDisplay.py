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
	glcd.clear_back_buffer()

#define neato font
neato = font.XglcdFont('/home/pi/Pi-ST7565/fonts/FixedFont5x8.c', 5, 8)

#create lcd object
glcd = st7565.Glcd(rgb=[21, 20, 16])

spiDisplayInit()
    
def write(x, y, ctx):

	"""
	Write text to coordinate (x,y)
	"""
	glcd.clear_back_buffer()
	glcd.draw_string(ctx, neato, x*6,y*8)
	glcd.flip()
	
	
def write_buffer(x, y, ctx):

	"""
	Write text to buffer at coordinate (x,y)
	"""
	glcd.draw_string(ctx, neato, x*6,y*8)
	
def send_buffer():
	"""
	Sends the buffer to the display and after that, the buffer will be cleared
	"""
	glcd.flip()
	glcd.clear_back_buffer()
