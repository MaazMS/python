import re
str = "Take up one idea, one idea at a time"
result = re.findall(r'o\w\w', str)
result1 = re.findall(r'i\w', str)
print(result)
print(result1)
