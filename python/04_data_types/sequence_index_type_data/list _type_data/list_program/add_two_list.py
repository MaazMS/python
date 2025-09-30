class TwoListAdd:
    def add_two_list_plus_operator(self):
        list1 = input("Enter a list1 element separated by space ").split()
        list2 = input("Enter a list2 element separated by space ").split()
        list3 = list1 + list2
        print("addition of two list", list3)

    def add_two_list_using_append(self):
        list1 = input("Enter a list1 element separated by space ").split()
        list2 = input("Enter a list2 element separated by space ").split()
        list3 = []
        for i in list1:
            list3.append(i)

        for i in list2:
            list3.append(i)

        print("addition of two list", list3)

    def add_two_list_using_extend(self):
        list1 = input("Enter a list1 element separated by space ").split()
        list2 = input("Enter a list2 element separated by space ").split()
        list3 = []

        list3.extend(list1)
        list3.extend(list2)
        print("addition of two list", list3)


obj = TwoListAdd()
obj.add_two_list_plus_operator()
obj.add_two_list_using_append()
obj.add_two_list_using_extend()
