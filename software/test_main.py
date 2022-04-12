from alarm import *
from buttons import *
import time

try:
	from i2cDisplay import *
	from hardware_init import *
except:
	from spiDisplay import *

alarm = Alarm(26)
alarm.init()

buttons = Buttons(12,16,20,21)
buttons.init()


alarm.enable()
time.sleep(2)
alarm.disable()
time.sleep(0.5)
alarm.enable()
time.sleep(0.5)
alarm.disable()
time.sleep(0.5)
alarm.enable()
time.sleep(0.5)
alarm.disable()

while True:
	status = buttons.poll()
	#write(0, 0, "Button up: " + str(status["UP"]))
	#write(0, 1, "Button down: " + str(status["DOWN"]))
	#write(0, 2, "Button left: " + str(status["LEFT"]))
	write(0, 3, "Button right: " + str(status["RIGHT"]))
	
	#TODO: FIX write() bug (Every write() call will clear the whole display, which makes writing to multiple lines impossible)
	
	
