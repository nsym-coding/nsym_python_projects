import random

def main():
    guesses_taken = 1 #initialise guesses

    print('Welcome to the guess the number!')

    print('Hello, what is your name?')
    my_name = input()

    number = random.randint(1,20)
    print('Well ' + my_name + ', I am thinking of a number between 1 and 20.')

    guess = int(input('Guess what that number is: \n'))

    while guess != number:
        if guess > number:
            print('Your guess is too high!')
            guess = int(input('Guess again: \n'))
            guesses_taken = guesses_taken + 1
		
        elif guess < number:
            print('Your guess is too low!')
            guess = int(input('Guess again: \n'))
            guesses_taken = guesses_taken + 1

    if guess == number:
        print('Well done, ' + my_name +  ' you got it in ' + str(guesses_taken) + ' tries!')

while True:
    main()
    if input('Play again? (y/n)') != 'y':
        break
