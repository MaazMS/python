# find first digit of number using  //
# find last digit of number using  %
#
class FirstLastDigitNumber:

    def find_first_digit_number(self):

        no = int(input("Enter number \t"))

        if no <= 0:
            print("Enter positive number")
        else:
            while no >= 10:
                no = no // 10
            print(no)

    def find_last_digit_number(self):

        no = int(input("Enter number \t"))

        if no <= 0:
            print("Enter positive number")
        else:
            last_digit = no % 10
            print(last_digit)

obj = FirstLastDigitNumber()
# obj.find_first_digit_number()
obj.find_last_digit_number()