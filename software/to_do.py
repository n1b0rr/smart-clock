try:
    from i2cDisplay import *
except:
    from spiDisplay import *

from buttons import Buttons
from menu import Menu



import RPi.GPIO as GPIO
from flask import Flask, render_template, request


import pickle

"""
GLOBAL VARIABLES
"""
#####PINS#####
button_up_pin = 20
button_down_pin = 21
button_left_pin = 12
button_right_pin = 16

#####OBJECTS#####
buttons = None
menu = None
app = Flask(__name__)
to_do_list = {0: "douchen", 1: "Eten", 2: "Gamen", 3: "studeren"}
x = 0

def render():
    with open('todolist.bin', 'rb') as f:
        to_do_list = pickle.load(f)

    menu = None
    menu = Menu(5)
    for i in to_do_list:
        menu.add_function(to_do_list[i], None)

    menu_function(menu)


def remove():
    global x
    if(len(to_do_list) > 0):
        to_do_list.pop(list(to_do_list)[x])
        with open('todolist.bin', 'wb') as f:
            pickle.dump(to_do_list, f)
        x=0
    render()


def init():
    """
    Initialize hardware and menu

    Returns
    -------
    None.

    """
    global x
    global button_up_pin
    global button_down_pin
    global button_left_pin
    global button_right_pin
    global buttons
    global to_do_list

    buttons = Buttons(button_up_pin, button_down_pin, button_left_pin, button_right_pin)
    buttons.init()
    

    x = 0


    with open('todolist.bin', 'rb') as f:
        to_do_list = pickle.load(f)

    render()



def menu_function(menu_object, timeout = 5):
    """
    Show the menu.
    If no buttons are pressed within the timeout, the function will return
    
    timeout variable is in seconds
    
    Returns
    -------
    None.

    """
    global x
    global buttons
    global button_state

    while True:
        menu_object.update_screen()
        button_state = buttons.poll()
        
        if(button_state["UP"]):
            menu_object.up()
            buttons.wait_released()
            if(x > 0):
                x-=1

        
        elif(button_state["DOWN"]):
            menu_object.down()
            buttons.wait_released()
            if(x < len(to_do_list)):
                x+=1

            
        elif(button_state["RIGHT"]):
            remove()
            break
            
        elif(button_state["LEFT"]):
            buttons.wait_released()
            break

init()
