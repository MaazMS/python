class RemoveDictKey:
    def remove_keys_dict(self):
        first_Dict = {"a": 1, "b": 2, "c": 3}
        print(first_Dict, "\n")
        key = input("Enter key for delete\n")

        if key in first_Dict:
            del first_Dict[key]
        else:
            print("Key is not exist in dictionary")

        print(first_Dict, "\n")


obj = RemoveDictKey()
obj.remove_keys_dict()
