import re

str = "Take up one idea, one idea at a time"
result = re.findall(r'i\w{1}',str)
result1 = re.findall(r'i\w{3}',str)
print(result)
print(result1)