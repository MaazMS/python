import re
str = "Take up one idea, one idea at a time"
result = re.sub(r'one', 'two', str)
print(result)