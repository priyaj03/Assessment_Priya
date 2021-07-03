"""Take a list, say for example this one:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from
this list in it and print out this new list.Ask the user for a number and return a list that contains
only elements from the original list a that are smaller than that number given by the user."""


class three():
    def less5(self):
        new_list = []
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        for i in a:
            if i < 5:
                new_list.append(i)
        print(new_list)

    def less(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        new_list = []
        user_input = int(input('Enter a number :'))
        for i in a:
            if i < user_input:
                new_list.append(i)
        print(new_list)


object1 = three()
object1.less5()
object1.less()
