from functools import reduce

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = reduce(lambda no1, no2: no1 + no2, ls)
print(result)
