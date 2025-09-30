import re

str = "Take up one idea, one idea at a time"
result = re.findall(r'i\w+',str)
print(result)