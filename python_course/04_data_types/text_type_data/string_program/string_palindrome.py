# A string is said to be a palindrome if the string read from left to right is equal to the string read from right to left.
#
class PalindromeString:
    def palindrome_String(self):

        s1 = input("Enter string")
        # [::-1] This is slice for reverse string
        if s1 == s1[::-1]:
            print("This is a Palindrome String")
        else:
            print("This is not a Palindrome String")

    def palindrome_String_by_variable(self):

        s1 = input("Enter string")
        s2 = ""
        for i in s1:
            s2 = i + s2 # s2 = s2 + i is copy s1 to s2

        if s1 == s2:
            print("This is a Palindrome String")
        else:
            print("This is not a Palindrome String")


obj = PalindromeString()
obj.palindrome_String()
obj.palindrome_String_by_variable()
