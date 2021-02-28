# count how many Vowels and  consonants in word.
#
class VowelsCOnsonant:
    def count_vowels(self):

        str1 = input("Please Enter Your Own String : ")
        vowels = 0

        for i in str1:
            if (
                i == "a"
                or i == "e"
                or i == "i"
                or i == "o"
                or i == "u"
                or i == "A"
                or i == "E"
                or i == "I"
                or i == "O"
                or i == "U"
            ):
                vowels = vowels + 1
        print("Total Number of Vowels in this String = ", vowels)

    def count_consonants(self):

        str1 = input("Please Enter Your Own String : ")
        Consonants = 0

        for i in str1:
            if (
                i != "a"
                and i != "e"
                and i != "i"
                and i != "o"
                and i != "u"
                and i != "A"
                and i != "E"
                and i != "I"
                and i != "O"
                and i != "U"
            ):
                Consonants = Consonants + 1
        print("Total Number of Consonants in this String = ", Consonants)


obj = VowelsCOnsonant()
obj.count_vowels()
obj.count_consonants()
