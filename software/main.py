try:
	from i2cDisplay import *
except:
	from spiDisplay import *



write(0, 0, "hello world!")


##################################################################
################infinite loop to hold the display still###########
##################################################################

try:
	while True:
		time.sleep(10)
except:
	print('\nCtrl-C pressed.  Cleaning up and exiting...')
	try:	
		glcd.cleanup()
		print('\nCleaned')
	except:
		print('\nNothing to clean')
		
