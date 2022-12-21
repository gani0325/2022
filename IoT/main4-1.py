# LED 스탠드 만들기
# 스위치를 누를 때마다 LED 밝기를 0 -> 30 -> 60 -> 100% 밝기로 조절

import RPi.GPIO as GPIO
import time

ledWhite = 12
swPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledWhite, GPIO.OUT)
GPIO.setup(swPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

ledWhitePwm = GPIO.PWM(ledWhite, 500)
ledWhitePwm.start(0)

swState = 0
newSw = 0
oldSw =0

def swOn():
    global newSw
    global oldSw
    newSw = GPIO.input(swPin)

    if newSw != oldSw :
        oldSw = newSw
        if newSw == 1:
            return 1

    return 0

try :
    while 1 :
        if swOn() == 1 :
            swState = swState + 1
            if swState >= 4 :
                swState = 0
            time.sleep(0.2)
            print(swState)
            if swState == 0:
                ledWhitePwm.ChangeDutyCycle(0)
                print("dyte:0")
            elif swState == 1 :
                ledWhitePwm.ChangeDutyCycle(30)
                print("dyte:30")
            elif swState == 2 :
                ledWhitePwm.ChangeDutyCycle(60)
                print("dyte:60")
            elif swState == 3 :
                ledWhitePwm.ChangeDutyCycle(100)
            print("dyte:100")

    except KeyboardInterrupt :
        pass

GPIO.cleanup()