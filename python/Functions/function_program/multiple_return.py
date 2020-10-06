def fun(a , b):
    addition = a+b
    subtraction = a -b
    multiplication = a * b
    return addition, subtraction, multiplication
result =fun(10, 20)
print(result)

for value in result:
    print(value)