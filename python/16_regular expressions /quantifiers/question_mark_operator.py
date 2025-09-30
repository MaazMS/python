import re

str = "Take up one idea, one idea at a time"
result = re.findall(r'a\w?',str)
result1 = re.findall(r'z\w?',str)
print(result)
print(result1)