class SplitJoinString:
    def split_String(self):

        s1 = input("Enter string \n")
        s2_split_wop = s1.split()
        print("Split string without parameter", s2_split_wop)
        s2_split_wip = s1.split(",")
        print("Split string with parameter", s2_split_wip)

    def split_join_String(self):
        s1 = input("Enter string \n")
        print("without join string \n")
        print("-".join(s1.split()))


obj = SplitJoinString()
obj.split_String()
obj.split_join_String()
