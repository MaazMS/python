# Count Alphabets Digits and Special Characters in a String


class AlphabetsDigitsSpecialChr:
    def count_alphabets(self):
        s1 = input("Enter string")
        alphabets = 0
        for i in range(len(s1)):
            if s1[i].isalpha():
                alphabets += 1
        print(alphabets)

    def count_digits(self):
        s1 = input("Enter string")
        digits = 0
        for i in range(len(s1)):
            if s1[i].isdigit():
                digits += 1
        print(digits)

    def count_special(self):
        s1 = input("Enter string")
        special = 0
        for i in range(len(s1)):
            if s1[i].isdigit():
                continue
            elif s1[i].isalpha():
                continue
            else:
                special += 1
        print(special)

    def count_(self):
        s1 = input("Enter string")
        special = 0
        for i in s1:
            if i.isdigit():
                continue
            elif i.isalpha():
                continue
            else:
                special += 1
        print(special)


obj = AlphabetsDigitsSpecialChr()
obj.count_alphabets()
obj.count_digits()
obj.count_special()
obj.count_()
