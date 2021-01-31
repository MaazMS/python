class FactorialNumber:
    def find_factorial_number(self):

        no = int(input("Enter number"))

        if no < 0:
            print("Enter positive number")
        elif no == 0:
            print("The factorial od zero is 1")
        else:
            factorial = 1
            for i in range(1, no + 1):
                factorial = i * factorial
            print(factorial)


obj = FactorialNumber()
obj.find_factorial_number()
