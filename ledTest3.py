import time
from Led import *

def clearAllLEDs():
    for i in range (0, 8):
        led.ledIndex(leds[i], 0, 0, 0)

led = Led()
            
leds = [0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x01, 0x02]

try:
    i = 0
    r = 25
    g = 25
    b = 25
    while True:
        for i in range (0, 8):
            led.ledIndex(leds[i], r, g, b)
            time.sleep(0.25)
        clearAllLEDs()
       
except KeyboardInterrupt:
    clearAllLEDs()


