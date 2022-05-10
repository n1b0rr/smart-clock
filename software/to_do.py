try:
    from i2cDisplay import *
except:
    from spiDisplay import *

from menu import Menu
import global_variable
import pickle


x = 0

def render():
    """ 
    Display to do's to the display.

    Returns
    -------
    None.
    """
    
    
    with open('todolist.bin', 'rb') as f:
        global_variable.to_do_list = pickle.load(f)

    menu = None
    menu = Menu(5)
    for i in global_variable.to_do_list:
        menu.add_function(global_variable.to_do_list[i], None)

    menu_function(menu)


def remove():
    """ 
    Remove an entry from the display

    Returns
    -------
    None.
    """
    global x
    
    if(len(global_variable.to_do_list) > 0):
        global_variable.to_do_list.pop(list(global_variable.to_do_list)[x])
        with open('todolist.bin', 'wb') as f:
            pickle.dump(global_variable.to_do_list, f)
        x=0
    render()


def show_to_do_list():
    """
    Initialize hardware and menu

    Returns
    -------
    None.

    """
    global x
    
    x = 0

    with open('todolist.bin', 'wb') as f:
        pickle.dump(global_variable.to_do_list, f)

    with open('todolist.bin', 'rb') as f:
        global_variable.to_do_list = pickle.load(f)

    render()



def menu_function(menu_object):
    """
    Show the to do list.
    
    Returns
    -------
    None.

    """
    global x
    button_state = None
    buttons = global_variable.buttons

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
            if(x < len(global_variable.to_do_list)):
                x+=1

            
        elif(button_state["RIGHT"]):
            buttons.wait_released()
            remove()
            break
            
        elif(button_state["LEFT"]):
            buttons.wait_released()
            break
