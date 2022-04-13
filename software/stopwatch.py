from buttons import *

try:
	from i2cDisplay import *

except:
	from spiDisplay import *

import time

buttons = Buttons(12,16,20,21)
buttons.init()
stopwatch_active = False
backup = 0
interval = 0

while True:
    status = buttons.poll()

# reset stopwatch
    if(status["DOWN"]):
        backup = 0
        interval = 0
        start = time.time()

# start or stop the stopwatch 
    if(status["UP"]):
        if(stopwatch_active):
            stopwatch_active = False
            backup += round(time.time() - start)
        else:
            stopwatch_active = True
            start = time.time()

    if(stopwatch_active):
        interval = backup + round(time.time() - start)

    hours = int(interval/3600)
    minutes = int((interval - (hours*3600))/60)
    seconds = int(interval - (hours*3600) - (minutes*60))
    write(20, 20, "{:0>2}".format(hours) + ":" + "{:0>2}".format(minutes) + ":" + "{:0>2}".format(seconds))

