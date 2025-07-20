import time
import board
import digitalio

led_green = digitalio.DigitalInOut(board.GP15)
led_green.direction = digitalio.Direction.OUTPUT

ledred1 = digitalio.DigitalInOut(board.GP14)
ledred1.direction = digitalio.Direction.OUTPUT

ledred2 = digitalio.DigitalInOut(board.GP13)
ledred2.direction = digitalio.Direction.OUTPUT

ledred3 = digitalio.DigitalInOut(board.GP12)
ledred3.direction = digitalio.Direction.OUTPUT

ledred4 = digitalio.DigitalInOut(board.GP11)
ledred4.direction = digitalio.Direction.OUTPUT

ledred5 = digitalio.DigitalInOut(board.GP10)
ledred5.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP16)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

while True:
    if button1.value is True:
        ledred5.value = False
        ledred4.value = False
        ledred3.value = False
        ledred2.value = False
        ledred1.value = False
        led_green.value = False
    else:
        ledred5.value = True
        time.sleep(0.05)
        ledred4.value = True
        time.sleep(0.06)
        ledred3.value = True
        time.sleep(0.07)
        ledred2.value = True
        time.sleep(0.08)
        ledred1.value = True
        time.sleep(0.09)
        led_green.value = True
        time.sleep(1.0)
