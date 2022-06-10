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
from to_do import show_to_do_list
import time
from threading import Lock, Thread
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
    global_variable.menu.add_function("To do", show_to_do_list)
    global_variable.menu.add_function("Show ip", show_ip)
    global_variable.menu.add_function("Set alarm", set_alarm)
    global_variable.menu.add_function("Clear alarm", clear_alarm)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #loads to do list to memory
    with open('todolist.bin', 'rb') as f:
        global_variable.to_do_list = pickle.load(f)

    global_variable.lock = Lock()   #lock variable to lock the to_do_list to prevent race condition
    global_variable.state_lock = Lock() #lock variable to lock the current_state variable

    "Setup webserver"
    Thread(target=lambda: app.run(host=get_ip(), port=80, debug=True, use_reloader=False)).start()

    test = Thread(target=lambda: alarm_main()).start()

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

def alarm_main():
    """
    Alarm thread for checking the time + activating the alarm


    STATE:
            None 1 value --> Time checking disabled
            1            --> Time checking enabled

    Returns
    -------
    None.

    """
    global_variable.state_lock.acquire()
    global_variable.current_state = 0
    global_variable.state_lock.release()

    while(True):

        global_variable.state_lock.acquire()

        if(global_variable.current_state == 1):
            global_variable.state_lock.release()
            print("time checking")
            #PSEUDO code
            """
            current_time = get_time()
            if(current_time >= alarm_time):
                global_variable.state_lock.acquire()
                enable_alarm()
                show_alarm_screen()
                while(True):
                    poll_buttons()
                    if(pressed_button == snooze_buton):
                        break
                disable_alarm()
                global_variable.current_state = 0
            """
        else:
            global_variable.state_lock.release()

def set_alarm():
    global_variable.state_lock.acquire()

    hh = 0
    mm = 0
    pointer = 0 # 0->hh / 1->mm
    global_variable.buttons.wait_released()
    write(7, 2, "{:0>2}".format(hh) + ":" + "{:0>2}".format(mm))
    while True:
        status = global_variable.buttons.poll()
        if(status["LEFT"] and (not status["RIGHT"])):
            global_variable.buttons.wait_released()
            pointer = pointer - 1
            if(pointer < 0):
                pointer = 0
        elif(status["RIGHT"] and (not status["LEFT"])):
            global_variable.buttons.wait_released()
            pointer = pointer + 1
            if(pointer == 2):
                pointer = 1
        elif(status["LEFT"] and status["RIGHT"]):
              global_variable.buttons.wait_released()
              global_variable.current_state = 1
              global_variable.hour = hh
              global_variable.minute = mm
              global_variable.state_lock.release()
              return
        elif(status["DOWN"]):
            global_variable.buttons.wait_released()
            if(pointer == 0):
                hh = hh - 1
            elif(pointer == 1):
                mm = mm - 1
            if(hh < 0):
                hh = 23
            if(mm < 0):
                mm = 59
        elif(status["UP"]):
            global_variable.buttons.wait_released()
            if(pointer == 0):
                hh = (hh + 1) % 24
            elif(pointer == 1):
                mm = (mm + 1) % 60
        write(7, 2, "{:0>2}".format(hh) + ":" + "{:0>2}".format(mm))

def clear_alarm():
    global_variable.state_lock.acquire()
    
    if(global_variable.current_state == 1):
       global_variable.current_state = 0
       write(0,2,"Alarm off")
    else:
        write(0,2,"Alarm already off")
    
    time.sleep(3)
    
    global_variable.state_lock.release()


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
    return global_variable.to_do_list

@app.route('/send', methods=['POST'])
def send():
    """
    To do list data from the website will be saved to the Smart Clock

    Returns
    -------
    200

    """

    data = request.get_json()

    for x in data:
        print("POST request handeling: " + x)

    global_variable.lock.acquire()  #locks the to_do_list for other functions
    global_variable.to_do_list.clear()

    it = 0
    for x in data:
        global_variable.to_do_list.update({it : x})
        it += 1


    print("New to_do_list is: ")
    print(global_variable.to_do_list)

    #write to do list to bin file
    with open('todolist.bin', 'wb') as f:
        pickle.dump(global_variable.to_do_list, f)

    global_variable.lock.release()  #unlocks the to_do_list

    return "200"

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


