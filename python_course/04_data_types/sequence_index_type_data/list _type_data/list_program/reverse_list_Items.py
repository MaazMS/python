class ReverseListItems:
    def list_items_reverse(self):

        list1 = [
            list1
            for list1 in input(
                "Enter string or character separated by space \n"
            ).split()
        ]
        print("Display list without reverse", list1)
        list1.reverse()
        print("Display list with reverse", list1)

    def list_items_reverse_logic(self):
        list1 = [
            list1
            for list1 in input(
                "Enter string or character separated by space \n"
            ).split()
        ]

        j = len(list1)
        i = 0

        while i < j:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

            i += 1
            j += 1

        print("Display list without reverse", list1)
        print("Display list with reverse", list1)


obj = ReverseListItems()
obj.list_items_reverse()
