class LargestSmallestNumber:
    def largest_max_smallest_min(self):
        list1 = [
            int(list1) for list1 in input("Enter number separated by space \n").split()
        ]

        print("largest number in list", max(list1))
        print("smallest number in list", min(list1))

    def largest_smallest_sort(self):
        list1 = [
            int(list1) for list1 in input("Enter number separated by space \n").split()
        ]
        length_of_list1 = len(list1)
        list1.sort()
        print("largest number in list", list1[length_of_list1 - 1])
        print("smallest number in list", list1[0])

    def largest_smallest_logic(self):
        list1 = [
            int(list1) for list1 in input("Enter number separated by space \n").split()
        ]
        largest = smallest = list1[0]
        for i in list1:
            if i > largest:
                largest = i
            if i < smallest:
                smallest = i

        print("largest number in list", largest)
        print("smallest number in list", smallest)


obj = LargestSmallestNumber()
# obj.largest_max_smallest_min()
# obj.largest_smallest_sort()
obj.largest_smallest_logic()
