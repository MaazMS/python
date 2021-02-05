class SumEvenOdd:
    def sum_of_list(self):
        total = 0

        list1 = [
            int(list1) for list1 in input("Enter number separated by space \n").split()
        ]

        for i in list1:
            total = total + i
        print("Sum of item in list", total)


obj = SumEvenOdd()
obj.sum_of_list()
