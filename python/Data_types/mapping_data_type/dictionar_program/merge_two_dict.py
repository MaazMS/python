class MergeDict:
    def merge_two_dict_by_update(self):
        first_Dict = {"a": 1, "b": 2, "c": 3}
        second_Dict = {1: "a", 2: "b", 3: "c"}

        first_Dict.update(second_Dict)
        print("Concatenating two Dictionaries", first_Dict)

    def merge_n_dict_by_dict(self):
        # key is always string not other then string
        first_Dict = {"a": 1, "b": 2, "c": 3}
        second_Dict = {
            "d": 4,
            "e": 5,
        }
        print(dict(first_Dict, **second_Dict))


obj = MergeDict()
obj.merge_two_dict_by_update()
obj.merge_n_dict_by_dict()
