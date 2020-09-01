import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

import sys
import LedConfig as leds
import ButtonConfig as btns
import LcdStuff as lcd

lcd.screenOn();

lcd.setText("Test Line 1", "Test Line 2", "Test Line 3", "Test Line 4")
sleep(5)

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
lcd.screenOff();
	
sleep(5)
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
lcd.clearText();
	
sleep(5)

lcd.SetText("scroll up", "1", "2", "3")
sleep(3)
lcd.addTextToBottom("4")
sleep(0.5)
lcd.addTextToBottom("5")
sleep(0.5)
lcd.addTextToBottom("6")
sleep(0.5)
lcd.addTextToBottom("7")
	
sleep(5)

lcd.SetText("3", "2", "1", "scroll down")
sleep(3)
lcd.addTextToTop("4")
sleep(0.5)
lcd.addTextToTop("5")
sleep(0.5)
lcd.addTextToTop("6")
sleep(0.5)
lcd.addTextToTop("7")

sleep(5)

lcd.clearText();
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