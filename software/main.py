try:
    from i2cDisplay import *
except:
    from spiDisplay import *

from alarm import Alarm
from buttons import Buttons
from menu import Menu
from clock import clock
from stopwatch import stopwatch
from timer import timer_function
import time
import threading
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import subprocess
import pickle
import global_variable

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

app = Flask(__name__)
to_do_list = {0:"Sporten", 1:"Eten", 2:"Slapen", 3:"Gamen"}
####################

def main():
    
    init()
    
    button_state = None
    buttons = global_variable.buttons
    menu = global_variable.menu
    
    while True:
        clock()
        button_state = buttons.poll()
        if(button_state["UP"] or button_state["DOWN"] or button_state["LEFT"] or button_state["RIGHT"]):
            buttons.wait_released()
            menu_function(menu, buttons)

    


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

    
    
    global_variable.buttons = Buttons(button_up_pin, button_down_pin, button_left_pin, button_right_pin)
    global_variable.buttons.init()
    
    global_variable.alarm = Alarm(alarm_pin)
    global_variable.alarm.init()
    
    global_variable.menu = Menu(5)
    global_variable.menu.add_function("Timer", timer_function)
    global_variable.menu.add_function("Stopwatch", stopwatch)
    global_variable.menu.add_function("To do", None)
    global_variable.menu.add_function("show ip", show_ip)
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    "Setup webserver"
    threading.Thread(target=lambda: app.run(host=get_ip(), port=80, debug=True, use_reloader=False)).start()

def menu_function(menu_object, buttons, timeout = 5):
    """
    Show the menu.
    If no buttons are pressed within the timeout, the function will return
    
    timeout variable is in seconds
    
    Returns
    -------
    None.

    """

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
        
def get_ip():
    """
    Get current IP address of Smart Clock

    Returns
    -------
    IP address as string variable

    """
    temp = str(subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True))
    temp = temp.strip('b')
    temp = temp.strip('\\n\'')
    return temp

def show_ip():
    """
    Shows a screen with the IP address of the RPI
    Screen will return if pressed on any button 

    Returns
    -------
    None.

    """
    
    buttons = global_variable.buttons
    status = None
    
    write(0, 0, "") #clears the display
    
    write_buffer(0, 0, "The IP address is:")
    write_buffer(0, 1, get_ip())
    send_buffer()
    
    #wait until button is pressed
    while True:
        status = buttons.poll()
        if(status["LEFT"] or status["RIGHT"] or status["UP"] or status["DOWN"]):
            buttons.wait_released()
            return
    

@app.route('/')
def index():
    """
    Render HTML webpage

    Returns
    -------
    HTML code

    """
    
    return render_template("index.html", ip=get_ip())

@app.route('/receive', methods=['GET'])
def receive():
    """
    Handle GET request for receive

    Returns
    -------
    To do list in JSON format 

    """
    global to_do_list
    return to_do_list
    
@app.route('/send', methods=['POST'])
def send():
    """
    To do list data from the website will be saved to the Smart Clock

    Returns
    -------
    Succeed page on good data, else an error page on bad data

    """
    global to_do_list
    data = request.get_json()
    
    for x in data:
        print("POST request handeling: " + x)
    
    
    try:
        assert type(data) == dict, "to_do_list variable must be a dictionary!"
        to_do_list = data
        return "GOOD"
    except:
        return "BAD"
    
        
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

        
