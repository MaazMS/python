# Lists Are Ordered
number_list1 = [1, 2, 3, 4, 5, 6]
print("data type number list ",type(number_list1),number_list1)

number_list2 = [6, 5, 4, 3, 2, 1]
print("data type number list ",type(number_list2),number_list2)

string_list1 = ['Maaz',  'Shaikh']
print("data type string list  ",type(string_list1),string_list1)

string_list2 = ['Shaikh', 'Maaz']
print("data type string list  ",type(string_list2),string_list2)

if number_list1 == number_list2:
    print("list is not Ordered that means sequence not matter")
else:
    print("list is  Ordered that means sequence  matter ")

if string_list1 == string_list2:
    print("list is not Ordered that means sequence not matter")
else:
    print("list is  Ordered that means sequence  matter ")