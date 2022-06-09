import RPi.GPIO as GPIO


class Alarm:

    def __init__(self, pin):
        self.pin = pin

    def init(self):
        """
        Initialize the pin for the communication with the active buzzer
        """
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)
        print("Alarm has been set to pin " + str(self.pin))
    
    def enable(self):
        GPIO.output(self.pin, True)
        print("Alarm enabled")
        
    def disable(self):
        GPIO.output(self.pin, False)
        print("Alarm disabled")
