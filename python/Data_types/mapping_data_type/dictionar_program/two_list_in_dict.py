class MapTwoList:
    def map_two_list_in_dict(self):

        keys = [list1 for list1 in input("Enter list1 item separated by space").split()]
        values = [
            list2 for list2 in input("Enter list2 item separated by space").split()
        ]

        mydict = {key: value for key, value in zip(keys, values)}
        print(mydict)


obj = MapTwoList()
obj.map_two_list_in_dict()
