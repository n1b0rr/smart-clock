import time
from buttons import *
from alarm import *

try:
    from i2cDisplay import *
    from hardware_init import *
except:
    from spiDisplay import *

buttons = Buttons(12,16,20,21)
buttons.init()
alarm = Alarm(26)
alarm.init()
timer = 0
timer_active = False
alarm_enabled = False

while True:
    status = buttons.poll()
    if(status["UP"]):
        if(status["DOWN"]):
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

        #if(status["UP"]):
           # if(timer_active):
           #     print("timer stopped")
           #     timer_active = False
           # else:
           #     print("timer started")
           #     timer_active = True
           #     start_time = time.time()

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
    write(20, 20, "{:0>2}".format(hours) + ":" + "{:0>2}".format(minutes) + ":" + "{:0>2}".format(seconds))



