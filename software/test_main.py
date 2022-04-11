from alarm import *
from buttons import *


alarm_b = Alarm(15)
alarm_b.init()
alarm_b.enable()
alarm_b.disable()

buttons = Buttons(1,2,3,4)
buttons.init()
buttons.poll()
