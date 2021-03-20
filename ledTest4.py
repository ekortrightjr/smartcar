import time
import sys
from Led import *

def clearAllLEDs():
    led.ledIndex(255, 0, 0, 0)

def clearAllLEDs_bak():    
    s = 0
    for i in range (0, 8):
        led.ledIndex(leds[i], 0, 0, 0)
        s += leds[i]
    print(s)

led = Led()
            
leds = [0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x01, 0x02]

try:
    i = 0
    r = 25
    g = 25
    b = 25
    delay = float(sys.argv[1])
    while True:
        for i in range (0, 8):
            led.ledIndex(leds[i], r, g, b)
            time.sleep(delay)
        for i in range (7, -1, -1):
            led.ledIndex(leds[i], 0, 0, 0)
            time.sleep(delay)
       
except KeyboardInterrupt:
    clearAllLEDs()


