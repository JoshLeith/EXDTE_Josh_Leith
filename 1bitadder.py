import board
import digitalio

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP14)
led2.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP16)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP18)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

while True:
    if button1.value is False:
        if button2.value is True:
            
            
             led2.value = True
             led2.value = False
    if button2.value is False:
        if button1.value is True:
            
             led2.value = True
             led2.value = False
    if button1.value is False:
        if button2.value is False:
            led.value = True
            led.value = False
