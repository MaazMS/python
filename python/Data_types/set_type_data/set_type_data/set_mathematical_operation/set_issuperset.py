# number set_type_data have all element that are present in number1.

number = {1, 2 ,3 ,4, 5, 6}
number1 = {1, 2, 3}
print("issuperset using operator is >= ")
print( number >= number1)

print("issuperset method is union ")
print(number.issuperset(number1))
