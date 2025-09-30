# count how many character is repeated in word.
#
class RepeatedCharacter:
    def count_first_occurrence(self):

        s1 = input("Enter string \t")
        char = input("enter your own Character \t")

        flag = 0
        for i in range(len(s1)):
            if s1[i] == char:
                flag = 1
                print("position of character ", i)
                break

        if flag == 0:
            print("Sorry! We haven't found the Search Character in this string ")
        else:
            print("We haven found the Search Character in this string")

    def count_last_occurrence(self):

        s1 = input("Enter string \t")
        char = input("enter your own Character \t")
        flag = 1
        for i in range(len(s1)):
            if s1[i] == char:
                flag = i
        if flag == 1:
            print("Sorry! We haven't found the Search Character in this string ")
        else:
            print("We haven found the Search Character in this string")
        print("position of character ", i)


obj = RepeatedCharacter()
obj.count_first_occurrence()
obj.count_last_occurrence()
