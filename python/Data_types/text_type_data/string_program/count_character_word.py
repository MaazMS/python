class CharacterWord:
    def count_character(self):

        s1 = input("Enter string \t")
        total = 0
        for i in s1:
            total += 1
        print(total)

    def count_character_word(self):
        s1 = input("Enter string \t")
        total = 1
        for i in range(len(s1)):
            if s1[i] == " " or s1 == "\n" or s1 == "\t":
                total = total + 1
        print(total)


obj = CharacterWord()
obj.count_character()
obj.count_character_word()
