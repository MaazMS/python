def sequence(no1 , no2):
    while no1 <no2:
        yield no1
        no1 += 1

result = sequence(10 , 30)
for number in result:
    print(number)