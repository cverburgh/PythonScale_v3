from RPi_GPIO_i2c_LCD import lcd
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

    lcdDisplay.clear()

def setTextOnLine(text, line):
    text = fillLine(text)
    lcdDisplay.set(text, line)

def setText(line1 = "", line2 = "", line3 = "", line4 = ""):
    lcdDisplay.set(fillLine(line1), 1)
    lcdDisplay.set(fillLine(line2), 2)
    lcdDisplay.set(fillLine(line3), 3)
    lcdDisplay.set(fillLine(line4), 4)

def addTextToTop(text):
    # add to top, lose the bottom
    lcdDisplay.set(fillLine(lcdDisplay.get(3)), 4)
    lcdDisplay.set(fillLine(lcdDisplay.get(2)), 3)
    lcdDisplay.set(fillLine(lcdDisplay.get(1)), 2)
    lcdDisplay.set(fillLine(text), 1)

def addTextToBottom(text):
    # add to bottom, lose the first line
    lcdDisplay.set(fillLine(lcdDisplay.get(2)), 1)
    lcdDisplay.set(fillLine(lcdDisplay.get(3)), 2)
    lcdDisplay.set(fillLine(lcdDisplay.get(4)), 3)
    lcdDisplay.set(fillLine(text), 4)

def fillLine(text):
    while (len(text) < 40):
        text = text + " "

    return text