try:
    from i2cDisplay import *
except:
    from spiDisplay import *

import time
import global_variable

def timer_function():

    timer = 0
    timer_active = False
    alarm_enabled = False

    buttons = global_variable.buttons
    alarm = global_variable.alarm

    while True:
        
        status = buttons.poll()
        buttons.wait_released()
        
        #exit function
        if(status["LEFT"]):
            return
        
        if(status["UP"] and status["DOWN"]):
            if(timer_active):
                print("timer stopped")
                timer_active = False
            else:
                backup = timer
                print("timer started")
                timer_active = True
                start_time = time.time()
            timer += 60
        if(status["DOWN"]):
            timer -= 60

        if(timer_active):
            if(timer > 0):
                timer = backup - round(time.time() - start_time)
            if(timer == 0):
                if not alarm_enabled:
                    alarm_enabled = True
                    alarm.enable()
        else:
            alarm_enabled = False
            
            alarm.disable()
    
        
    
        hours = int(timer/3600)
        minutes = int((timer - (hours*3600))/60)
        seconds = int(timer - (hours*3600) - (minutes*60))
        write(7, 2, "{:0>2}".format(hours) + ":" + "{:0>2}".format(minutes) + ":" + "{:0>2}".format(seconds))