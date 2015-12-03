import RPi.GPIO as GPIO
import time

LedPin = 11
sleepTime = 0.3

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin, GPIO.OUT)

def loop():
	state = False
	while True:
		GPIO.output(LedPin, state)
		state = not state
		time.sleep(sleepTime)

def destroy():
	GPIO.output(LedPin, 1)
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
