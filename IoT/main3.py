# 경찰차 경광등 만들기
# 빨간색, 파란색 LED를 깜빡이면서 경광등을 만들자
# 스위치를 추가하여 스위치로 경광등을 끄고 켤 수 있게 만들자

import RPi.GPIO as GPIO
import time

ledRed = 23
ledGreen = 24
swPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(swPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try :
    while 1 :
        swValue = GPIO.input(swPin)
        print(swValue)
        time.sleep(0.1)
    except KeyboardInterrupt :
        pass

    GPIO.cleanup()