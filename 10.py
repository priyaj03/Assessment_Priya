"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes
a new list of only the first and last elements of the given list."""


class First_Last():
    def first_last(self):
        a = [5, 10, 15, 20, 25]
        print('New List -', [a[0], a[-1]])

    def first_Last(self):
        no_of_elements = int(input('Enter the no of elements:'))
        print('Enter the elements :')
        list1 = [int(input('')) for x in range(no_of_elements)]
        new_list = [list1[0], list1[-1]]
        print(new_list)


object1 = First_Last()
object1.first_last()
object1.first_Last()
