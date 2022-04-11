import RPi.GPIO as GPIO
import time

class Buttons:

	def __init__(self, button_up, button_down, button_left, button_right):
		self.button_up = button_up
		self.button_down = button_down
		self.button_left = button_left
		self.button_right = button_right
		self.button_state = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
		
	def init(self):
		"""
		Initialize pins with internal pull-up for the communication with the buttons
		"""
		RPIO.setup(self.button_up, RPIO.IN, pull_up_down=RPIO.PUD_UP)
		RPIO.setup(self.button_down, RPIO.IN, pull_up_down=RPIO.PUD_UP)
		RPIO.setup(self.button_left, RPIO.IN, pull_up_down=RPIO.PUD_UP)
		RPIO.setup(self.button_right, RPIO.IN, pull_up_down=RPIO.PUD_UP)
		print("Buttons are initialized")
	
	def poll(self):
		"""
		Get the current status of the buttons
		"""
		
		#debouncig delay
		time.sleep(0.001)	#sleep for 1ms
		
		#poll buttons
		button_state["UP"] = RPIO.input(button_up)
		button_state["DOWN"] = RPIO.input(button_down)
		button_state["LEFT"] = RPIO.input(button_left)
		button_state["RIGHT"] = RPIO.input(button_right)
		
		print("button up: " + str(self.button_state["UP"]))
		print("button down: " + str(self.button_state["DOWN"]))
		print("button left: " + str(self.button_state["LEFT"]))
		print("button right: " + str(self.button_state["RIGHT"]))
		
		return self.button_state
