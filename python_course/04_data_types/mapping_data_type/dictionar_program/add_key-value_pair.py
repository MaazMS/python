class AddKeyValuePair:
    def add_key_value_by_update(self):
        key = input("Please enter the Key : ")
        value = input("Please enter the Value : ")

        mydict = {}
        mydict.update({key: value})

        print("add key and value by update ", mydict)

    def add_key_value_by_logic(self):
        key = input("Please enter the Key : ")
        value = input("Please enter the Value : ")

        mydict = {}
        mydict[key] = value

        print("add key and value by update ", mydict)


obj = AddKeyValuePair()
obj.add_key_value_by_update()
obj.add_key_value_by_logic()
