# Armstrong number is a number that is equal to the sum of cubes of its digits
#  153 is  Armstrong.
#  1 + 125 + 27 = 153
class Armstrong_Number:
    def find_armstrong_number(self):

        no = int(input("Enter Number \t"))
        temp_no = no
        cube = 0
        if no <0:
            print("Enter positive number")
        else:
            while temp_no > 0:
                digit = temp_no % 10
                cube += digit ** 3
                temp_no //= 10

            if no == cube:
                print(no, "is an Armstrong number")
            else:
                print(no, "is not an Armstrong number")


obj = Armstrong_Number()
obj.find_armstrong_number()
