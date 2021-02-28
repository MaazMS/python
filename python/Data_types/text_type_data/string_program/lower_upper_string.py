# convert lower string to upper string and upper string to lower string
#
class LowerUpperString:
    def convert_lower_to_upper_string(self):

        lower_case_string = input("Enter lower case string ")
        print(lower_case_string.upper())

    def convert_upper_to_lower_string(self):
        upper_case_string = input("Enter upper case string ")
        print(upper_case_string.lower())


obj = LowerUpperString()
obj.convert_lower_to_upper_string()
obj.convert_upper_to_lower_string()
