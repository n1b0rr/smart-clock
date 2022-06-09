try:
    from i2cDisplay import *
except:
    from spiDisplay import *

import global_variable
import time

def stopwatch():    
    """
    Stopwatch function

    Returns
    -------
    None.

    """

    buttons = global_variable.buttons

    stopwatch_active = False
    backup = 0
    interval = 0

    while True:
        status = buttons.poll()
        buttons.wait_released()
        # exit function
        if(status["LEFT"]):
            return
    
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
        write(7, 2, "{:0>2}".format(hours) + ":" + "{:0>2}".format(minutes) + ":" + "{:0>2}".format(seconds))