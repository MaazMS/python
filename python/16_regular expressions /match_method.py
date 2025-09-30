import re
str = "Take up one idea, one idea at a Time"
result = re.match(r'o\w\w', str)
result1 = re.match(r'T\w', str)
print(result)
print(result1.group())
