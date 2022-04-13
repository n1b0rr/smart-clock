#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:55:40 2022

@author: nasser
"""

import os

def time():
    print("time")
    
def clock():
    print("clock")
    
def foo():
    print("foo")
    
def bar():
    print("bar")

from menu import Menu

menu = Menu(3)  #3 --> zal drie lijnen tekenen
menu.add_function("Display clock", clock)
menu.add_function("Display time", time)
menu.add_function("foo", foo)
menu.add_function("bar", bar)

menu.update_screen()
menu.execute_selection()
os.system('clear')

menu.down()
menu.update_screen()
menu.execute_selection()
os.system('clear')

menu.down()
menu.update_screen()
menu.execute_selection()
os.system('clear')

menu.down()
menu.update_screen()    ##bug
menu.execute_selection()
os.system('clear')

menu.down()
menu.update_screen()
menu.execute_selection()
os.system('clear')

#####

menu.up()
menu.update_screen()
menu.execute_selection()
os.system('clear')

menu.up()
menu.update_screen()
menu.execute_selection()
os.system('clear')

menu.up()
menu.update_screen()
menu.execute_selection()
os.system('clear')

menu.up()
menu.update_screen()
menu.execute_selection()
os.system('clear')
