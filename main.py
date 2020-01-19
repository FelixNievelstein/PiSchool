import time
import colorsys

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

from rgbmatrix5x5 import RGBMatrix5x5
from RPi import GPIO
from time import sleep

clk = 17
dt = 18
buttonA = 9
buttonB = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonA, GPIO.IN)
GPIO.setup(buttonB, GPIO.IN)

counter = 0
clkLastState = GPIO.input(clk)
lastStateBtnA = GPIO.input(buttonA)

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.5)

height = rgbmatrix5x5.height
width = rgbmatrix5x5.width

if height == width:
    delta = 0
else:
    delta = 2

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
        rgbmatrix5x5.set_pixel(0, 4, r, g, b)
        rgbmatrix5x5.set_pixel(2, 4, r, g, b)
        rgbmatrix5x5.set_pixel(4, 4, r, g, b)
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
        for y in range(height):
            for x in range(width):
                rgbmatrix5x5.set_pixel(x, y, 0, 0, 0)
        rgbmatrix5x5.show()

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                btnAState = GPIO.input(buttonA)
                btnBState = GPIO.input(buttonB)

                if btnAState != lastStateBtnA
                    print("Button A")
                    print(buttonAState)
                    lastStateBtnA = btnAState
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print(counter)
                        setFace(counter)
                clkLastState = clkState
                sleep(0.0001)
finally:
        GPIO.cleanup()






""" def make_gaussian(fwhm):
    x = numpy.arange(0, 5, 1, float)
    y = x[:, numpy.newaxis]
    x0, y0 = 2, 2
    fwhm = fwhm
    gauss = numpy.exp(-4 * numpy.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
    return gauss


while True:
    for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
        fwhm = 5.0 / z
        gauss = make_gaussian(fwhm)
        start = time.time()
        
        r = int(1 * 255.0)
        g = int(0.0 * 255.0)
        b = int(0.0 * 255.0)
        rgbmatrix5x5.set_pixel(0, 0, r, g, b)
        rgbmatrix5x5.show()
        end = time.time()
        t = end - start
        if t < 0.04:
            time.sleep(0.04 - t) """