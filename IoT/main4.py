# LED 스탠드 만들기
# 스위치를 이용하여 LED의 밝기를 조절할 수 있는 스탠드 만들기

import RPi.GPIO as GPIO
import time

ledWhite = 12
swPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledWhite, GPIO.OUT)
GPIO.setup(swPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

ledWhitePwm = GPIO.PWM(ledWhite, 500)
ledWhitePwm.start(0)

try :
    while 1 :
        ledWhitePwm.ChangeDutyCycle(0)
        print("dyte:0")
        time.sleep(2)
        ledWhitePwm.ChangeDutyCycle(30)
        print("dyte:30")
        time.sleep(2)
        ledWhitePwm.ChangeDutyCycle(60)
        print("dyte:60")
        time.sleep(2)
        ledWhitePwm.ChangeDutyCycle(100)
        print("dyte:100")
        time.sleep(2)
    except KeyboardInterrupt :
        pass

GPIO.cleanup()