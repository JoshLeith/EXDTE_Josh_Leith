#How fast can you react?  You have been asked to make a reaction time game.  The game will have the following minimum specifications:

#import libraries
# Debounce Code
import time
import board
import analogio
import pwmio
from adafruit_debouncer import Debouncer

#variables - pins
button_pin = digitalio.DigitalInOut(board.GP12)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP
my_button = Debouncer(button_pin)

#blue LED

#button

#Start time
#knob value

#while True
    #Turn Blue LED on
    #Blue LED on stand by

    #update button
    #The user will press a button that will utilise debounce
    #LED will turn off when once button is released

    #after an amount of time the LED will turn back on
    #record start time
    #Turn LED on
    #once the LED is on the user needs to press it as fast as possable
    #when button pressed
    #calculate target time (start time + knob value / 10000 + _1)
    #the time delay will be based on the position of the potentiometer (use value / 10000)
    #use PWM to run led at half brightness

    #print reaction time
while True:
my_button.update()
	if my_button.value is True:
        print('not pressed')
    if my_button.value is False:
        print('pressed')



#Blue LED indicates the game is in standby.
#The user will press a button that will utilise debounce code
#The LED will turn off once they release the button
#After an amount of time the LED will turn back on
#Once the LED comes on the user needs to press the button again as quickly as possible
#It should print their time to the console
#The time delay will be based on the position of a potentiometer (use value / 10000 +1)
#Use PWM to run the LED at half brightness
#Optionally, you could add some or all of the following features:
#If the reaction time is within a set time it could turn on a green LED, otherwise it could turn on a red LED
#The target time could either be hard coded or based on the position of a second potentiometer
#The LED brightness could be automatically adjusted based on ambient light levels (using an LDR)
#Add a random element to the timing
#Replace the blue LED with multiple blue LEDs using a transistor
#Put the program in a loop so they can try again
#Create a file on the pico that contains the user's best reaction time, overwriting it when necessary.
#Or anything else you think will make your product better.
