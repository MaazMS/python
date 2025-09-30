class SwapNumber:
    def swap_no_by_third_variable(self):
        no1 = int(input("Enter number1\t"))
        no2 = int(input("Enter number2\t"))
        print("display number1\t", no1)
        print("display number2\t", no2)
        temp = no1
        no1 = no2
        no2 = temp
        print("display number1\t", no1)
        print("display number2\t", no2)

    def swap_no_without_third_variable(self):
        no1 = int(input("Enter number1\t"))
        no2 = int(input("Enter number2\t"))
        print("display number1\t", no1)
        print("display number2\t", no2)
        no1 = no1 + no2
        no2 = no1 - no2
        print("no2", no2)
        no1 = no1 - no2
        print("no1", no1)
        print("display number1\t", no1)
        print("display number2\t", no2)


obj = SwapNumber()
obj.swap_no_by_third_variable()
obj.swap_no_without_third_variable()
