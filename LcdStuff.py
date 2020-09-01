﻿from RPi_GPIO_i2c_LCD import lcd
# Address of i2c backpack on screen
i2c_address = 0x27

# initialize the display
lcdDisplay = lcd.HD44780(i2c_address)

def screenOn():
    lcdDisplay.backlight("on")

def screenOff():
    lcdDisplay.backlight("off")

def clearText():
    lcdDisplay.set("                                        ", 1)
    lcdDisplay.set("                                        ", 2)
    lcdDisplay.set("                                        ", 3)
    lcdDisplay.set("                                        ", 4)

    #lcdDisplay.clear()

def clearLine(line):
    lcdDisplay.set("                                        ", line)

def setTextOnLine(text, line):
    text = fillLine(text)
    clearLine(line)
    lcdDisplay.set(text, line)

def setText(line1 = "", line2 = "", line3 = "", line4 = ""):
    clearText()

    lcdDisplay.set(line1, 1)
    lcdDisplay.set(line2, 2)
    lcdDisplay.set(line3, 3)
    lcdDisplay.set(line4, 4)

def addTextToTop(text):
    # add to top, lose the bottom
    clearLine(4)
    lcdDisplay.set(lcdDisplay.get(3), 4)
    clearLine(3)
    lcdDisplay.set(lcdDisplay.get(2), 3)
    clearLine(2)
    lcdDisplay.set(lcdDisplay.get(1), 2)
    clearLine(1)
    lcdDisplay.set(text, 1)

def addTextToBottom(text):
    # add to bottom, lose the first line
    clearLine(1)
    lcdDisplay.set(lcdDisplay.get(2), 1)
    clearLine(2)
    lcdDisplay.set(lcdDisplay.get(3), 2)
    clearLine(3)
    lcdDisplay.set(lcdDisplay.get(4), 3)
    clearLine(4)
    lcdDisplay.set(text, 4)

def fillLine(text):
    while (len(text) < 40):
        text = text + " "

    return text