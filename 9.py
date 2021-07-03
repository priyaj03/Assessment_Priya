"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right. Keep the game going until the user
types “exit”. Keep track of how many guesses the user has taken, and when the game ends, print this out."""
import random


def guess():
    random_number = random.randint(1, 10)
    guess_number1 = 0
    user_input1 = input('Are you ready to play the game? [yes/exit] :')
    if user_input1 == 'yes':
        guess_number = int(input('Enter your guess :'))
        guess_number1 = guess_number1 + 1
        if guess_number != random_number:
            if guess_number > random_number:
                print('High')
            elif guess_number < random_number:
                print('Low')
            guess()

        else:
            print('Exactly right')


    elif user_input1 == 'exit':
        print('Random number is',random_number)
        return 0
    print('guesses',guess_number1)


guess()
