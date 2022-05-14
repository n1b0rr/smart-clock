try:
	from i2cDisplay import *
except:
	from spiDisplay import *

class Menu:

    def __init__(self, max_lines):
        self.__functions = {}
        self.__current_position = 0
        self.__start_draw_from = 0
        self.__scroll_detect = 0
        self.__max_lines = max_lines
        
    def add_function(self,name,function_reference):
        """
        Add a function to the menu

        Returns
        -------
        Dictionary of functions

        """
        self.__functions[name] = function_reference
        return self.__functions[name]
    
    def delete_function(self,name):
        """
        Deletes a function from the menu

        Returns
        -------
        Dictionary of functions

        """
        self.__functions.pop(name)
        self.__current_position = 0
        self.__start_draw_from = 0
        self.__scroll_detect = 0
        return self.__functions
        
    def up(self):
        """
        Move the cursor up

        Returns
        -------
        Cursor position

        """
       
        
        if(self.__current_position):
            self.__current_position -= 1
            
            #Should we also scroll the screen?
            self.__scroll_detect -= 1
            if(self.__scroll_detect == -1):
                self.__scroll_detect = 0
                self.__start_draw_from -= 1
        
        return self.__current_position
        
    def down(self):
        """
        Move the cursor down

        Returns
        -------
        Cursor position

        """
        if(self.__current_position < len(self.__functions) - 1):
            self.__current_position += 1
            
            #Should we also scroll the screen?
            self.__scroll_detect += 1
            if(self.__scroll_detect == self.__max_lines):
                self.__scroll_detect -= 1
                self.__start_draw_from += 1
        
        return self.__current_position
    
    def update_screen(self):
        """
        Draw the menu to the screen
        """
        
        
        last_draw = self.__start_draw_from + self.__max_lines
        it = 0
        
        if(last_draw > len(self.__functions)):
            last_draw = len(self.__functions)
        
        for menu_text in range(self.__start_draw_from,last_draw):
            if(menu_text == self.__current_position):
                write_buffer(0,it,list(self.__functions.keys())[menu_text] + "<--")
                it += 1
            else:
                write_buffer(0,it,list(self.__functions.keys())[menu_text])
                it += 1
        
        send_buffer()
        

    def execute_selection(self):
        """
        Execute current selected option        
        """
        list(self.__functions.values())[self.__current_position]()
