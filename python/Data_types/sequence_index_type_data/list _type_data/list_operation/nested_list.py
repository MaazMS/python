nested_list = ['a', 'b', 'c' ,[1, 2, 3] ]
print(nested_list)

print("access outer list")

print("outer list", nested_list[0])
print("outer list", nested_list[1])
print("outer list", nested_list[2])
print("inner list ", nested_list[3])

print("access nested list with help of outer list index")
print("inner list ", nested_list[3][0])
print("inner list ", nested_list[3][1])
print("inner list ", nested_list[3][2])




