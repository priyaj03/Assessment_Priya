'''Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old'''

import datetime


class age():
    def year(self):
        user_name = input('Enter your name :')
        user_age = int(input('Enter your age :'))
        years = 100 - user_age
        current_year = datetime.datetime.now().year
        year_100 = current_year + years
        print('You will be 100 years old in the year -', year_100)


object1 = age()
object1.year()
