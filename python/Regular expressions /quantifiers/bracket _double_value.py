import re

str = "Take up one idea, one idea at a time"
result = re.findall(r'i\w{1,3}',str)
print(result)
