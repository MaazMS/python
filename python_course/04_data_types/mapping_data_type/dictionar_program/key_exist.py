class KeyExistORNot:
    def key_exist_by_key(self):
        keys = input("Please enter the Key \n  ")
        values = input("Please enter the Value \n ")
        key = input("Please enter the Key for exist or not \n")

        mydict = {}
        mydict.update({keys: values})

        if key in mydict.keys():
            print("\nKey Exists in this Dictionary")
        else:
            print("\nKey Not Exists in this Dictionary")

    def key_exist_by_logic(self):
        keys = input("Please enter the Key \n  ")
        values = input("Please enter the Value \n ")
        key = input("Please enter the Key for exist or not \n")

        mydict = {}
        mydict.update({keys: values})

        if key in mydict:
            print("\nKey Exists in this Dictionary")
        else:
            print("\nKey Not Exists in this Dictionary")


obj = KeyExistORNot()
# obj.key_exist_by_key()
obj.key_exist_by_logic()
