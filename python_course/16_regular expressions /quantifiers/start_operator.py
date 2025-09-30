import re

str = "Take up one idea, one idea at a time"
result = re.findall(r'a\w*',str)
print(result)