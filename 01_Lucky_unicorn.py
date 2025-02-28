import random

print('-------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------')
print('welcome to Lucky Unicorn - Gambling Game!')
# Function to check that the input is within a valid range
def intcheck(question, low, high):
    valid = False
    error = "Please enter a number between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Start of the game
how_much = intcheck("How much money ($1-$10) would you like to play/lose with Today? 🤑: ", 1, 10)
print("You have chosen to play with ${}".format(how_much))

# Game rules explained
print('-------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------')
print('If you roll a UNICORN, you will leave with $5 more!')
print('If you roll a HORSE, you lose $3.')
print('If you roll a DONKEY, you lose $10!')
print('If you roll a ZEBRA, you lose $1.')
print("Remember this is your current game balance: ${}".format(how_much))
input('Press <Enter> To agree to the terms of service: ')
print('-------------------------------------------------------------------------------')
input('please enter your credit card number: ')
input('mm/yy: ')
input('Pin: ')
input('Numbers on the back: ')
input('phone number: ')
input('email address: ')
print('it cost $1 to play each round! ')
print('the game will begin now! ')
print('-------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------')

# Game begins here
balance = how_much

keep_playing = True
while keep_playing:
    play = input('Press <enter> to roll: ')
    if play == '':  # Player rolls
        balance -= 1  # Player pays $1 per roll
        random_number = random.random()
        
        # Random roll
        if random_number < 0.05:
          print('You rolled a Unicorn! You win $5!')
          balance += 5
        elif random_number < 0.25:
          print('You rolled a Zebra! You lose $1.')
          balance -= 1
        elif random_number < 0.30:
          print('You rolled a Horse! You lose $3.')
          balance -= 3
        elif random_number < 0.40:
          print('OH NO! You rolled a Donkey! You lose $10.')
          balance -= 10

        # Check if the player wants to continue or if they are out of money
        print(f"Your current balance is ${balance}.")
        if balance <= 0:
            print("Oops! You're out of money! Game over.")
            break  # End the game if balance reaches 0
        
        keep_playing = input("Would you like to keep playing? Press <Enter> to quit or type 'c' to continue: ").lower()
        if keep_playing == 'c':
            keep_playing = True

print("Thank you for playing Lucky Unicorn! come back soon, we will be taking anything you owe us from your account!")
print('-------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------')
