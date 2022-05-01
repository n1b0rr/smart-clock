try:
    from i2cDisplay import *
except:
    from spiDisplay import *

from alarm import Alarm
from buttons import Buttons
from menu import Menu
from clock import clock
import time
import threading
import RPi.GPIO as GPIO
from flask import Flask, render_template


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
app = Flask(__name__)

####################

def main():
    global buttons
    global menu
    
    button_state = None
    
    init()
    
    while True:
        clock()
        button_state = buttons.poll()
        if(button_state["UP"] or button_state["DOWN"] or button_state["LEFT"] or button_state["RIGHT"]):
            buttons.wait_released()
            menu_function(menu)

    


def init():
    """
    Initialize hardware and menu

    Returns
    -------
    None.

    """
    
    global alarm_pin
    global button_up_pin
    global button_down_pin
    global button_left_pin
    global button_right_pin
    global alarm
    global buttons
    global menu
    ipaddress = "192.168.1.20"
    
    #TODO
    """
    Er moet een functie komen die de huidige ipaddress polled
    """
    
    buttons = Buttons(button_up_pin, button_down_pin, button_left_pin, button_right_pin)
    buttons.init()
    
    alarm = Alarm(alarm_pin)
    alarm.init()
    
    menu = Menu(5)
    menu.add_function("Timer", None)
    menu.add_function("Stopwatch", None)
    menu.add_function("To do", None)
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    "Setup webserver"
    #ipaddress = getIpaddress()
    threading.Thread(target=lambda: app.run(host=ipaddress, port=80, debug=True, use_reloader=False)).start()

def menu_function(menu_object, timeout = 5):
    """
    Show the menu.
    If no buttons are pressed within the timeout, the function will return
    
    timeout variable is in seconds
    
    Returns
    -------
    None.

    """
    global buttons
    start_time = time.time()
    stop_time = None
    
    while True:
        menu_object.update_screen()
        button_state = buttons.poll()
        
        if(button_state["UP"]):
            menu_object.up()
            buttons.wait_released()
            start_time = time.time()
        
        elif(button_state["DOWN"]):
            menu_object.down()
            buttons.wait_released()
            start_time = time.time()
            
        elif(button_state["RIGHT"]):
            buttons.wait_released()
            menu_object.execute_selection()
            break
            
        elif(button_state["LEFT"]):
            buttons.wait_released()
            break
        else:
            stop_time = time.time()
            if((stop_time - start_time) >= timeout):
                break
        
@app.route('/')

def index():
    return render_template("index.html")

        
        
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
    main()

        
