class PositiveNegativeNo:
    def count_positive_negative(self):

        list1 = [int(list1) for list1 in input().split()]

        count_positive_number = 0
        count_negative_number = 0
        for i in list1:
            if i > 0:
                count_positive_number += 1
            elif i < 0:
                count_negative_number += 1

        print("count negative number is ", count_negative_number)
        print("count positive number is ", count_positive_number)


obj = PositiveNegativeNo()
obj.count_positive_negative()
