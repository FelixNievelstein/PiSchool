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

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print counter
                        setFace(counter)
                clkLastState = clkState
                sleep(0.01)
finally:
        GPIO.cleanup()

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
        r = int(1 * 255.0)
        g = int(0.0 * 255.0)
        b = int(0.0 * 255.0)
        rgbmatrix5x5.set_pixel(0, 0, r, g, b)
        rgbmatrix5x5.set_pixel(0, 4, r, g, b)
        rgbmatrix5x5.show()
    else:
        for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
            rgbmatrix5x5.set_pixel(0, 0, r, g, b)
            rgbmatrix5x5.show()


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