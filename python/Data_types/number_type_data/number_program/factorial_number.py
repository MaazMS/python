# The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n.
# Example  factorial of 6 is 1*2*3*4*5*6 = 720 .
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
