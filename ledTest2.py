import time
from Led import *

led = Led()

leds = [0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x01, 0x02]
led.ledIndex(leds[0]+leds[1]+leds[2], 67, 79, 121)
time.sleep(5)
led.ledIndex(0,0,0,0)
