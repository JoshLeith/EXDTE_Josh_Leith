import board
import digitalio

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP14)
led2.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP16)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

while True:
    if button1.value is True:
        led.value = False
        led2.value = True
    else:
        led.value = True
        led2.value = False
