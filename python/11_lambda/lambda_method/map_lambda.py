"""
map() function returns a map object which is an iterator
Example list element is pass to lambda function and lambda function is under filter method.
result = list(filter(lambda no: print(no) , ls))
"""

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map(lambda no: no * 2, ls))
print(result)
