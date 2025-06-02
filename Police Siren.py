import board
import digitalio
import time

speed = 0.15

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP15)
led2.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(speed)
    led.value = False
    time.sleep(speed)
    led2.value = True
    time.sleep(speed)
    led2.value = False
    time.sleep(speed)
