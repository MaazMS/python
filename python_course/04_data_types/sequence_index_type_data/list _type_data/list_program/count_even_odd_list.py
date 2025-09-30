class EvenOddListElement:
    def count_even_odd_element(self):

        list1 = [int(list1) for list1 in input().split()]
        Even_count = 0
        Odd_count = 0

        for i in list1:
            if i % 2 == 0:
                Even_count += 1
            elif i % 2 != 0:
                Odd_count += 1
        print("\nTotal Number of Even Numbers in this List =  ", Even_count)
        print("Total Number of Odd Numbers in this List = ", Odd_count)


obj = EvenOddListElement()
obj.count_even_odd_element()
