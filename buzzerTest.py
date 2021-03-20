from Buzzer import *
import time

buzzer = Buzzer()

for i in range (1, 6):
    buzzer.run("1")
    time.sleep(0.25)
    buzzer.run("0")
    time.sleep(0.25)
