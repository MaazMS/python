# a number (such as 16461) that remains the same when its digits are reversed
class PalindromeNumber:

    def find_palindrom_number(self):

        no = int(input("Enter number \t"))
        temp_no = no
        reverse_no = 0
        if no <= 0:
            print("Enter positive number ")
        else:
            while no > 0:
                dig = no % 10
                reverse_no = reverse_no * 10 + dig
                no = no // 10

            if temp_no == reverse_no:
                print("The number is palindrome!")
            else:
                print("Not a palindrome!")


obj = PalindromeNumber()
obj.find_palindrom_number()
