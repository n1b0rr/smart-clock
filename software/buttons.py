import RPi.GPIO as GPIO
import time

class Buttons:

    def __init__(self, button_up, button_down, button_left, button_right):
        self.button_up = button_up
        self.button_down = button_down
        self.button_left = button_left
        self.button_right = button_right
        
    def init(self):
        """
        Initialize pins with internal pull-up for the communication with the buttons
        """
        GPIO.setup(self.button_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("Buttons are initialized")
    
    def poll(self):
        """
        Get the current status of the buttons
        """
        
        #debouncig delay
        time.sleep(0.001)    #sleep for 1ms
        
        #poll buttons
        button_state = {}
        button_state["UP"] = not(GPIO.input(self.button_up))
        button_state["DOWN"] = not (GPIO.input(self.button_down))
        button_state["LEFT"] = not (GPIO.input(self.button_left))
        button_state["RIGHT"] = not (GPIO.input(self.button_right))
        
        return button_state

    def wait_released(self):
        """
        Wait until all buttons are released
        """
        
        status = self.poll()
        
        while(status["UP"] or status["DOWN"] or status["LEFT"] or status["RIGHT"]):
            status = self.poll()