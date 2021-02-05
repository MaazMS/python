class LengthTuple:
    def find_length_tuple(self):

        list1 = [list1 for list1 in input("Enter item separated by space \n").split()]
        convert_lsit_to_tuple = tuple(list1)
        print(len(convert_lsit_to_tuple))


obj = LengthTuple()
obj.find_length_tuple()
