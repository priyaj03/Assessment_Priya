'''Ask the user for a number. Depending on whether the number is even or odd, print out an
appropriate message to the user. If the number is a multiple of 4, print out a different message.'''


class number():
    def odd_even(self):
        user_input = int(input('Enter a number : '))
        if user_input % 4 == 0:
            print('This number is multiple of 4')
        elif user_input % 2 != 0:
            print('Hey! This number is odd')
        else:
            print('Hey! This number is even')


object1 = number()
object1.odd_even()
