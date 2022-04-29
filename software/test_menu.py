#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:55:40 2022

@author: nasser
"""

from buttons import Buttons
from menu import Menu
from alarm import Alarm
from hardware_init import *
import os

try:
	from i2cDisplay import *
except:
	from spiDisplay import *

def time():
    alarm.enable()
    print("time")
    
def clock():
    alarm.disable()
    print("clock")
    
def foo():
    print("foo")
    
def bar():
    print("bar")
    
def time2():
    print("time2")
    
def clock2():
    print("clock2")
    
def foo2():
    print("foo2")
    
def bar2():
    print("bar2")

def time3():
    print("time3")
    
def clock3():
    print("clock3")
    
def foo3():
    print("foo3")
    
def bar3():
    print("bar3")


menu = Menu(5)  #8 --> zal acht lijnen tekenen
menu.add_function("Display clock", clock)
menu.add_function("Display time", time)
menu.add_function("foo", foo)
menu.add_function("bar", bar)
menu.add_function("Display clock2", clock2)
menu.add_function("Display time2", time2)
menu.add_function("foo2", foo2)
menu.add_function("bar2", bar2)
menu.add_function("Display clock3", clock3)
menu.add_function("Display time3", time3)
menu.add_function("foo3", foo3)
menu.add_function("bar3", bar3)

buttons = Buttons(20, 21, 12, 16)
buttons.init()

alarm = Alarm(26)
alarm.init()

#####
while True:
    os.system('clear')
    menu.update_screen()
    status = buttons.poll()
    
    if(status["UP"]):
        menu.up()
        buttons.wait_released()
    
    elif(status["DOWN"]):
        menu.down()
        buttons.wait_released()
        
    elif(status["RIGHT"]):
        menu.execute_selection()
        buttons.wait_released()
        
