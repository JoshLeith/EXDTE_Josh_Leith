import random

#introduce the game
print('-------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------')
print('Welcome to Higher or lower! ')
print('Guess the random number between 1-100! ')
print('-------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------')
start_playing = input('Bot will think off a random number! enter "c" to continue').lower()
if start_playing == 'c':
  start_playing = True

keep_playing = True
while keep_playing:
  random_number = 72
  print('bot has thought of number')
  guess = int(input('Time to guess: '))
  
  if guess < random_number:
    print('WRONG! too low! ')
  elif guess > random_number:
    print('WRONG! too high!')
  elif guess == random_number:
    print('you got it! Press enter To exit! ')
  
  keep_playing = input("Press <Enter> to quit or type 't' to try agin: ").lower()
  if keep_playing == 't':
    keep_playing = True

print('-------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------')
print('Thanks for playing!')