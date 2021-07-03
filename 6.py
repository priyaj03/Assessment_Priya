'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome
is a string that reads the same forwards and backwards.)'''


class pal():
    def palindrome(self):
        user_input = input('Enter a string:')
        print('The given string is palindrome' if user_input == user_input[::-1] else
              'The given string is not a palindrome')


obj = pal()
obj.palindrome()
