print("if number is even then skip even number ")

number = int(input(" enter the number which is less then 20 and greater then 0\n"))
no = 0
while no <=number:
    no = no + 1
    if no % 2 == 0:
        continue
    print(no)


