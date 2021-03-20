from ADC import *
from Motor import *
import time
from Led import *
from Ultrasonic import *
from Buzzer import *

adc = Adc()
motor = Motor()
ultrasonic = Ultrasonic()
buzzer = Buzzer()

leds = [0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x01, 0x02]

def move(mode):
    if (mode == "fwd"):
        print('moveForward')
        motor.setMotorModel(750,750,750,750)
        signal("off")
        brakeLights("off")
    elif (mode == "fwd-left"):
        print('moveLeft')
        motor.setMotorModel(-500,-500,1800,1800)
        signal("left")
        brakeLights("off")
    elif (mode == "fwd-right"):
        print('moveRight')
        motor.setMotorModel(1800,1800,-500,-500)
        signal("right")
        brakeLights("off")
    elif (mode == "stop"):
        print('stop')
        motor.setMotorModel(0,0,0,0)
        brakeLights("on")
    else:
        print('stop')
        motor.setMotorModel(0,0,0,0)
        brakeLights("on")
        
def beep(mode):
    if (mode == "on"):
        buzzer.run("1")
    else:
        buzzer.run("0")
        
def clearAllSignals():
    led.ledIndex(leds[1]+leds[2]+leds[5]+leds[6],0,0,0)

def signal(mode):
    if (mode == "left"):
        led.ledIndex(leds[2]+leds[1],225,128,0)
        time.sleep(0.25)
        led.ledIndex(leds[2]+leds[1],0,0,0)
    elif (mode == "right"):
        led.ledIndex(leds[5]+leds[6],225,128,0)
        time.sleep(0.25)
        led.ledIndex(leds[5]+leds[6],0,0,0)
    else:
        clearAllSignals()
        time.sleep(0.25)


def headLights(mode):
    if (mode == "drive"):
        led.ledIndex(leds[3]+leds[4],100,100,100)
    elif (mode == "low"):
        led.ledIndex(leds[3]+leds[4],175,175,175)
    elif (mode == "high"):
        led.ledIndex(leds[3]+leds[4],225,225,225)
    else:
        led.ledIndex(leds[3]+leds[4],0,0,0)

def brakeLights(mode):
    if (mode == "on"):
        led.ledIndex(leds[0]+leds[7],200,0,0)
    else:
        led.ledIndex(leds[0]+leds[7],0,0,0)

def moveForward():
    print('moveForward')
    motor.setMotorModel(750,750,750,750)
    signal("off")
    brakeLights("off")

def moveLeft():
    print('moveLeft')
    motor.setMotorModel(-500,-500,1800,1800)
    signal("left")
    brakeLights("off")

def moveRight():
    print('moveRight')
    motor.setMotorModel(1800,1800,-500,-500)
    signal("right")
    brakeLights("off")

def stop():
    print('stop')
    motor.setMotorModel(0,0,0,0)
    brakeLights("on")

try:
    while True:
        time.sleep(0.25)
        Left_IDR = adc.recvADC(0)
        print ("The photoresistor voltage on the left is " + str(Left_IDR) + "V")
        Right_IDR = adc.recvADC(1)
        print ("The photoresistor voltage on the right is " + str(Right_IDR) + "V")
        print ()

        if (Left_IDR < 1.7) or (Right_IDR < 1.7):
            headLights("low")
        else:
            headLights("drive")

        distance = ultrasonic.get_distance()
        print ("distance: " + str(distance) + "CM")
        if (distance < 15):
            move("stop")
            beep("on")
        elif (Left_IDR > Right_IDR + 0.3):
            print ("turn left")
            move("fwd-left")
            beep("off")
        elif (Right_IDR > Left_IDR + 0.3):
            print("turn right")
            move("fwd-right")
            beep("off")
        else:
            print ("move forward")
            move("fwd")
            beep("off")
except KeyboardInterrupt:
    print ("End of Program")
    move("stop")
    time.sleep(3)
    brakeLights("off")
    headLights("off")
    signal("off")
    beep("off")


