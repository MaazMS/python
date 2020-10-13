import re
str = "Take up 123 idea, one idea at 132 time"
result = re.split(r'\d+', str)
print(result)