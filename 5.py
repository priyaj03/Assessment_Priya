'''Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of different sizes.'''


class common_elements():
    def common(self):
        final_list = []
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for i in a:
            for j in b:
                if i == j and i not in final_list:
                    final_list.append(i)
        print(final_list)

    def common1(self):
        final_list = []
        no_of_elements_list1 = int(input('Enter the number of elements in list1:'))
        print('ENTER THE ELEMENTS OF LIST 1:')
        list1 = [int(input()) for x in range(no_of_elements_list1)]
        no_of_elements_list2 = int(input('Enter the number of elements in list2:'))
        print('ENTER THE ELEMENTS OF LIST 2:')
        list2 = [int(input()) for x in range(no_of_elements_list2)]
        for i in list1:
            for j in list2:
                if i == j and i not in final_list:
                    final_list.append(i)
        print(final_list)


obj = common_elements()
obj.common()
obj.common1()


