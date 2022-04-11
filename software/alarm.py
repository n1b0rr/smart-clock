import RPi.GPIO as GPIO


class Alarm:

	def __init__(self, pin):
		self.pin = pin

	def init(self):
		"""
		Initialize the pin for the communication with the active buzzer
		"""
	
		RPIO.setup(self.pin, RPIO.OUT, initial=RPIO.LOW)
		print("Alarm has been set to pin " + str(self.pin))
	
	def enable(self):
		RPIO.output(self.pin, True)
		print("Alarm enabled")
		
	def disable(self):
		RPIO.output(self.pin, False)
		print("Alarm disabled")
