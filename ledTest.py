import time
from Led import *

led = Led()

try:
	while True:
            led.ledIndex(0x01,150,0,0)
            led.ledIndex(0x10,0,0,150)
            time.sleep(0.5)
            led.ledIndex(0x01,0,0,0)
            led.ledIndex(0x10,0,0,0)
            
            led.ledIndex(0x08,0,0,150)
            led.ledIndex(0x80,150,0,0)
            time.sleep(.5)
            led.ledIndex(0x08,0,0,0)
            led.ledIndex(0x80,0,0,0)

except KeyboardInterrupt:
	led.ledIndex(0x01,0,0,0)
	led.ledIndex(0x10,0,0,0)
	led.ledIndex(0x08,0,0,0)
	led.ledIndex(0x80,0,0,0)

