#!/usr/bin/env python
import ADC0832 as ADC
import RPi.GPIO as GPIO
import time
import math

sleep_time = 1
adjustment_value = 0.97

def setup():
	ADC.setup()
	#GPIO.setwarnings(False)

def convert_to_temperature(adc_val):
	#B = 3950.0 # Thermistor constant from thermistor datasheet
    	#R0 = 10000.0 # Resistance of the thermistor being used
    	#t0 = 273.15 # 0 deg C in K
    	#t25 = t0 + 25.0 # 25 deg C in K
    	# Steinhart-Hart equation
    	#inv_T = 1/t25 + (1/B) * math.log(adc_val/R0)
    	#T = (1/inv_T - t0) * adjustment_value
	#return T
    	#return T * 9.0 / 5.0 + 32.0 # Convert C to F

	R0 = 10000
	Vr = 5 * float(adc_val) / 255
        Rt = R0 * Vr / (5 - Vr)
        temp = 1/(((math.log(Rt / R0)) / 3950) + (1 / (273.15+25)))
        temp = temp - 273.15
	return temp

def loop():
	while True:
		analogVal = ADC.getResult(0)
		print 'adcval:', analogVal
		if analogVal > 0:
			print 'temp:', convert_to_temperature(analogVal)
		time.sleep(sleep_time)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	
