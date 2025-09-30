# copy one string to another string.
#
class CopyString:
    def copy_one_String_to_another_String(self):

        s1 = input("Enter string \t")
        s2 = s1
        print("first way to copy string ", s2)

        # The [:] makes a shallow copy of the array, hence allowing you to modify your copy without damaging the original.
        s3 = s1[:]
        print("Second way to copy string ", s2)

        s4 = ""

        for i in s1:
            s4 = s4 + i  # s4 = i + s4 is reverse string
        print("Third way to copy string ", s2)


obj = CopyString()
obj.copy_one_String_to_another_String()
