class ConverListTupe:
    def convert_list_to_tuple(self):
        list1 = [list1 for list1 in input("Enter item separated by space \n").split()]
        convert_lsit_to_tuple = tuple(list1)
        print(type(convert_lsit_to_tuple), "\n", convert_lsit_to_tuple, "\n")

    def convert_tuple_to_list(self):
        tuple1 = tuple([eval(x) for x in input("enter the values: ").split()])
        convert_tuple_to_lsit = list(tuple1)
        print(type(convert_tuple_to_lsit), "\n", convert_tuple_to_lsit, "\n")


obj = ConverListTupe()
# obj.convert_list_to_tuple()
obj.convert_tuple_to_list()
