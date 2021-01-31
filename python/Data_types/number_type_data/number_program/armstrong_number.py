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
