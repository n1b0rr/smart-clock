try:
    from i2cDisplay import *
except:
    from spiDisplay import *

from alarm import Alarm
from buttons import Buttons
from menu import Menu
from clock import clock
from threading import Thread, Event

"""
GLOBAL VARIABLES
"""
#####PINS#####
alarm_pin = 26
button_up_pin = 20
button_down_pin = 21
button_left_pin = 12
button_right_pin = 16
#####OBJECTS#####
alarm = None
buttons = None
menu = None

####################

def main():
    button_state = None
    
    init()
    
    while True:
        clock()
        button_state = buttons.poll()
        if(button_state["UP"] or button_state["DOWN"] or button_state["LEFT"] or button_state["RIGHT"]):
            #call menu
            pass

    


def init():
    """
    Initialize hardware and menu

    Returns
    -------
    None.

    """
    
    buttons = Buttons(button_up_pin, button_down_pin, button_left_pin, button_right_pin)
    buttons.init()
    
    alarm = Alarm(alarm_pin)
    alarm.init()
    
    menu = Menu(5)
    menu.add_function("Timer", None)
    menu.add_function("Stopwatch", None)
    menu.add_function("To do", None)
    menu.add_function("Return", None)

def entry():
    try:
            while True:
                main()
    except:
            print('\nCtrl-C pressed.  Cleaning up and exiting...')
    try:    
        glcd.cleanup()
        print('\nCleaned')
    except:
        print('\nNothing to clean')


if __name__ == "__main__":
    entry()

        
