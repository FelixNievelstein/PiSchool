import time
import colorsys
import random
try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")
from rgbmatrix5x5 import RGBMatrix5x5
from RPi import GPIO
from time import sleep
from models.ColorModel import ColorModel, ColorHelper

# Used GPIO Pins
clk = 17
dt = 18
buttonA = 9
buttonB = 10

# Set GPIO Mode and Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonA, GPIO.IN)
GPIO.setup(buttonB, GPIO.IN)

# Counter for rotarty encoder
counter = 0
clkLastState = GPIO.input(clk)

# Last state of GPIO for buttons
lastStateBtnA = GPIO.input(buttonA)
lastStateBtnB = GPIO.input(buttonB)

# Configure RGB matrix
rgbmatrix5x5 = RGBMatrix5x5()
rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.5)
height = rgbmatrix5x5.height
width = rgbmatrix5x5.width

def clearDisplay():
    for y in range(height):
        for x in range(width):
            rgbmatrix5x5.set_pixel(x, y, 0, 0, 0)
        rgbmatrix5x5.show()

# Sets one of the smiley faces to the rgb matrix
def setFace(number):
    if number is 2:
        r = int(234.0)
        g = int(43.0)
        b = int(93.0)
        rgbmatrix5x5.set_pixel(0, 0, r, g, b)
        rgbmatrix5x5.set_pixel(4, 0, r, g, b)
        rgbmatrix5x5.set_pixel(1, 1, r, g, b)
        rgbmatrix5x5.set_pixel(3, 1, r, g, b)
        rgbmatrix5x5.set_pixel(1, 3, r, g, b)
        rgbmatrix5x5.set_pixel(3, 3, r, g, b)
        rgbmatrix5x5.set_pixel(0, 3, r, g, b)
        rgbmatrix5x5.set_pixel(2, 3, r, g, b)
        rgbmatrix5x5.set_pixel(4, 3, r, g, b)
        rgbmatrix5x5.set_brightness(0.16)
        rgbmatrix5x5.show()
    elif number is 4:
        r = int(190.0)
        g = int(112.0)
        b = int(241.0)
        rgbmatrix5x5.set_pixel(1, 0, r, g, b)
        rgbmatrix5x5.set_pixel(3, 0, r, g, b)
        rgbmatrix5x5.set_pixel(1, 3, r, g, b)
        rgbmatrix5x5.set_pixel(2, 3, r, g, b)
        rgbmatrix5x5.set_pixel(3, 3, r, g, b)
        rgbmatrix5x5.set_pixel(0, 4, r, g, b)
        rgbmatrix5x5.set_pixel(4, 4, r, g, b)
        rgbmatrix5x5.set_brightness(0.32)
        rgbmatrix5x5.show()
    elif number is 6:
        r = int(0.0)
        g = int(163.0)
        b = int(248.0)
        rgbmatrix5x5.set_pixel(1, 0, r, g, b)
        rgbmatrix5x5.set_pixel(3, 0, r, g, b)
        rgbmatrix5x5.set_pixel(0, 3, r, g, b)
        rgbmatrix5x5.set_pixel(1, 3, r, g, b)
        rgbmatrix5x5.set_pixel(2, 3, r, g, b)
        rgbmatrix5x5.set_pixel(3, 3, r, g, b)
        rgbmatrix5x5.set_pixel(4, 3, r, g, b)
        rgbmatrix5x5.set_brightness(0.48)
        rgbmatrix5x5.show()
    elif number is 8:
        r = int(79.0)
        g = int(216.0)
        b = int(84.0)
        rgbmatrix5x5.set_pixel(1, 0, r, g, b)
        rgbmatrix5x5.set_pixel(3, 0, r, g, b)
        rgbmatrix5x5.set_pixel(0, 2, r, g, b)
        rgbmatrix5x5.set_pixel(4, 2, r, g, b)
        rgbmatrix5x5.set_pixel(1, 3, r, g, b)
        rgbmatrix5x5.set_pixel(2, 3, r, g, b)
        rgbmatrix5x5.set_pixel(3, 3, r, g, b)        
        rgbmatrix5x5.set_brightness(0.64)
        rgbmatrix5x5.show()
    elif number is 10:
        r = int(251.0)
        g = int(185.0)
        b = int(61.0)
        rgbmatrix5x5.set_pixel(1, 0, r, g, b)
        rgbmatrix5x5.set_pixel(3, 0, r, g, b)
        rgbmatrix5x5.set_pixel(0, 2, r, g, b)
        rgbmatrix5x5.set_pixel(1, 2, r, g, b)
        rgbmatrix5x5.set_pixel(2, 2, r, g, b)
        rgbmatrix5x5.set_pixel(3, 2, r, g, b) 
        rgbmatrix5x5.set_pixel(4, 2, r, g, b)
        rgbmatrix5x5.set_pixel(0, 3, r, g, b)
        rgbmatrix5x5.set_pixel(1, 3, 255, 255, 255)
        rgbmatrix5x5.set_pixel(2, 3, 255, 255, 255)
        rgbmatrix5x5.set_pixel(3, 3, 255, 255, 255)
        rgbmatrix5x5.set_pixel(4, 3, r, g, b)
        rgbmatrix5x5.set_pixel(1, 4, r, g, b)
        rgbmatrix5x5.set_pixel(2, 4, r, g, b)
        rgbmatrix5x5.set_pixel(3, 4, r, g, b)
        rgbmatrix5x5.set_brightness(0.8)
        rgbmatrix5x5.show()
    elif number is 12:
        r = int(243.0)
        g = int(37.0)
        b = int(24.0)
        rgbmatrix5x5.set_pixel(1, 0, r, g, b)
        rgbmatrix5x5.set_pixel(3, 0, r, g, b)
        rgbmatrix5x5.set_pixel(0, 1, r, g, b)
        rgbmatrix5x5.set_pixel(1, 1, r, g, b)
        rgbmatrix5x5.set_pixel(2, 1, r, g, b)
        rgbmatrix5x5.set_pixel(3, 1, r, g, b) 
        rgbmatrix5x5.set_pixel(4, 1, r, g, b)
        rgbmatrix5x5.set_pixel(0, 2, r, g, b)
        rgbmatrix5x5.set_pixel(1, 2, r, g, b)
        rgbmatrix5x5.set_pixel(2, 2, r, g, b)
        rgbmatrix5x5.set_pixel(3, 2, r, g, b) 
        rgbmatrix5x5.set_pixel(4, 2, r, g, b)
        rgbmatrix5x5.set_pixel(1, 3, r, g, b)
        rgbmatrix5x5.set_pixel(2, 3, r, g, b)
        rgbmatrix5x5.set_pixel(3, 3, r, g, b)
        rgbmatrix5x5.set_pixel(2, 4, r, g, b)
        rgbmatrix5x5.set_brightness(1.0)
        rgbmatrix5x5.show()
    else:
        clearDisplay()

# Show random number
def setRandom():
    clearDisplay()
    number = random.randrange(5)
    white = ColorHelper.whiteColor()
    if number is 0:
        rgbmatrix5x5.set_pixel(2, 2, white.r, white.g, white.b)
        rgbmatrix5x5.show()
    elif number is 1:
        rgbmatrix5x5.set_pixel(1, 3, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(3, 1, white.r, white.g, white.b)
        rgbmatrix5x5.show()
    elif number is 2:
        rgbmatrix5x5.set_pixel(0, 4, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(2, 2, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(4, 0, white.r, white.g, white.b)
        rgbmatrix5x5.show()
    elif number is 3:
        rgbmatrix5x5.set_pixel(1, 1, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(1, 3, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(3, 1, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(3, 3, white.r, white.g, white.b)
        rgbmatrix5x5.show()
    elif number is 4:
        rgbmatrix5x5.set_pixel(0, 0, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(0, 4, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(4, 0, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(4, 4, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(2, 2, white.r, white.g, white.b)
        rgbmatrix5x5.show()
    elif number is 5:
        rgbmatrix5x5.set_pixel(1, 0, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(3, 0, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(1, 2, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(3, 2, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(1, 4, white.r, white.g, white.b)
        rgbmatrix5x5.set_pixel(3, 4, white.r, white.g, white.b)
        rgbmatrix5x5.show()

    print(number)

# Run script for the program
try:
        clearDisplay()
        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                btnAState = GPIO.input(buttonA)
                btnBState = GPIO.input(buttonB)

                if btnAState != lastStateBtnA:
                    print("Button A")
                    print(btnAState)
                    lastStateBtnA = btnAState
                if btnBState != lastStateBtnB:
                    if btnBState is 1:
                        setRandom()
                    lastStateBtnB = btnBState
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        if counter >= 14:
                            counter = 0
                        if counter < 0:
                            counter = 13
                        print(counter)
                        setFace(counter)
                clkLastState = clkState
                sleep(0.0001)
finally:
        GPIO.cleanup()
