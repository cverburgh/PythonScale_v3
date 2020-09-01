from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

import sys
import LedConfig as leds
import ButtonConfig as btns
import LcdStuff as lcd

lcd.screenOn();

def testLeds():
	lcd.addTextToTop("Status LED > ON")
	leds.setStatusLed("on")
	
	sleep(3)

	lcd.addTextToTop("Status LED > OFF")
	leds.setStatusLed("off")

	sleep(3)

	lcd.addTextToBottom("Blinking No Go")
	leds.blinkNoGoLeds()

	sleep(3)

	lcd.addTextToBottom("CycleLeds 1")
	leds.cycleLeds()

	sleep(3)

	lcd.addTextToBottom("CycleLeds 2")
	leds.cycleLeds2()

	sleep(3)

	lcd.addTextToBottom("Blink all LEDs")
	leds.blinkAll()

	sleep(3)



def testLcd():
	lcd.setText("Test Line 1", "Test Line 2", "Test Line 3", "Test Line 4")

	sleep(3)
	lcd.clearText()

	lcd.setText("Turning off LCD", "in", "   5   ","seconds")
	sleep(1)
	lcd.setTextOnLine("    4    ", 3)
	sleep(1)
	lcd.setTextOnLine("    3    ", 3)
	sleep(1)
	lcd.setTextOnLine("    2    ", 3)
	sleep(1)
	lcd.setTextOnLine("    1    ", 3)
	sleep(1)
	lcd.setTextOnLine("    0    ", 3)
	lcd.screenOff()
	
	sleep(5)
	lcd.clearText()
	lcd.screenOn()

	lcd.setText("Clearing screen", "in", "   5   ","seconds")
	sleep(1)
	lcd.setTextOnLine("    4    ", 3)
	sleep(1)
	lcd.setTextOnLine("    3    ", 3)
	sleep(1)
	lcd.setTextOnLine("    2    ", 3)
	sleep(1)
	lcd.setTextOnLine("    1    ", 3)
	sleep(1)
	lcd.setTextOnLine("    0    ", 3)

	sleep(5)
	lcd.clearText()

	lcd.setText("scroll up", "1", "2", "3")
	sleep(3)
	lcd.addTextToBottom("4")
	sleep(0.5)
	lcd.addTextToBottom("5")
	sleep(0.5)
	lcd.addTextToBottom("6")
	sleep(0.5)
	lcd.addTextToBottom("7")
	
	sleep(5)
	lcd.clearText()

	lcd.setText("3", "2", "1", "scroll down")
	sleep(3)
	lcd.addTextToTop("4")
	sleep(0.5)
	lcd.addTextToTop("5")
	sleep(0.5)
	lcd.addTextToTop("6")
	sleep(0.5)
	lcd.addTextToTop("7")

	sleep(5)
	lcd.clearText()

	lcd.setText("powering off", "in 5 seconds")
	sleep(1)
	lcd.setTextOnLine("    4    ", 3)
	sleep(1)
	lcd.setTextOnLine("    3    ", 3)
	sleep(1)
	lcd.setTextOnLine("    2    ", 3)
	sleep(1)
	lcd.setTextOnLine("    1    ", 3)
	sleep(1)
	lcd.setTextOnLine("    0    ", 3)
	lcd.clearText()
	sleep(1)
	lcd.screenOff()

testLeds()
testLcd()
