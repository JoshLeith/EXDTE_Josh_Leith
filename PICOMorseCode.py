import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(7)
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(7)
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(7)
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(1)
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(7)
