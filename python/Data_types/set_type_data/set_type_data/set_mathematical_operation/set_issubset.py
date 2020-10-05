# number1 set_type_data all element present in number set_type_data means number1 is subset of number
number = {1, 2 ,3 ,4, 5, 6}
number1 = {1, 2, 3}
print("issubset using operator is | ")
print( number1 <= number)

print("issubset method is union ")
print(number1.issubset(number))
