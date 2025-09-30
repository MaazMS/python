import re

str = "Take up one idea, One idea at a time"
result1 = re.search(r'o\w\w', str)
result2 = re.search(r'i\w', str)
print(result1.group())
print(result2.group())