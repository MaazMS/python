# String Data Type Documentation

## 1. String Creations

Strings in Python can be created using three different quote styles:

### 1.1 Single Quotes

```python
first_name = 'Maaz'
message = 'Hello World'
single_quote_string = 'I\'m learning Python'  # Escape single quote
```

### 1.2 Double Quotes

```python
last_name = "Shaikh"
message = "Hello World"
double_quote_string = "She said, \"Hello!\""  # Escape double quote
```

### 1.3 Triple Quotes (Multiline Strings)

```python
# Triple single quotes
multiline_text = '''This is a 
multiline string that 
spans multiple lines'''

# Triple double quotes
full_name = """My name is 
Maaz Shaikh
and I'm a developer"""

# Useful for documentation strings
def example_function():
    """
    This is a docstring
    that explains what the function does
    """
    pass
```

### 1.4 Raw Strings

```python
# Raw strings (prefix with r) - useful for regex and file paths
raw_string = r"C:\Users\Name\Documents"
regex_pattern = r"\d+\.\d+"
```

### 1.5 Formatted Strings (f-strings)

```python
name = "Maaz"
age = 25
formatted_string = f"My name is {name} and I'm {age} years old"
```

## 2. String Operations

### 2.1 Concatenation (+)

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"

# Multiple concatenation
greeting = "Hello" + " " + "Beautiful" + " " + "World"
```

### 2.2 Repetition (*)

```python
username = "Maaz\n"
repeated = username * 5  # Repeats "Maaz\n" 5 times

separator = "-" * 20  # Creates "--------------------"
```

### 2.3 Membership Testing (in, not in)

```python
text = "Python Programming"
print("Python" in text)      # True
print("Java" in text)        # False
print("Script" not in text)  # True
```

### 2.4 String Indexing

```python
str_example = "MaazMS"
print(str_example[0])   # 'M' (first character)
print(str_example[-1])  # 'S' (last character)
print(str_example[-2])  # 'M' (second last)
```

### 2.5 String Slicing

```python
text = "abcdef"
print(text[0:6])    # "abcdef" (start:end)
print(text[1:4])    # "bcd"
print(text[:3])     # "abc" (from start)
print(text[3:])     # "def" (to end)
print(text[::2])    # "ace" (every 2nd character)
print(text[::-1])   # "fedcba" (reverse)
```

### 2.6 String Comparison

```python
str1 = "apple"
str2 = "banana"
print(str1 < str2)   # True (lexicographical order)
print(str1 == str2)  # False
print(str1 != str2)  # True
```

## 3. String Methods

### 3.1 Case Conversion Methods

```python
text = "maaz shaikh"

# Capitalize first letter of entire string
print(text.capitalize())  # "Maaz shaikh"

# Title case - first letter of each word
print(text.title())       # "Maaz Shaikh"

# Convert to uppercase
print(text.upper())       # "MAAZ SHAIKH"

# Convert to lowercase
print(text.lower())       # "maaz shaikh"

# Case folding (aggressive lowercase)
mixed_case = "MAAZ Shaikh"
print(mixed_case.casefold())  # "maaz shaikh"

# Swap case
print(text.swapcase())    # "MAAZ SHAIKH"
```

### 3.2 Search and Count Methods

```python
text = "Hello World, Hello Python"

# Count occurrences
print(text.count('l'))        # 3
print(text.count('Hello'))    # 2

# Find substring (returns index or -1)
print(text.find('World'))     # 6
print(text.find('Java'))      # -1

# Find from right
print(text.rfind('Hello'))    # 13

# Index (similar to find but raises exception if not found)
print(text.index('World'))    # 6
# print(text.index('Java'))   # Raises ValueError

# Check if starts/ends with
print(text.startswith('Hello'))  # True
print(text.endswith('Python'))   # True
```

### 3.3 String Validation Methods

```python
# Check if alphanumeric
text1 = "Fitness123"
print(text1.isalnum())    # True

text2 = "Fitness"
print(text2.isalpha())    # True

text3 = "123"
print(text3.isdecimal())  # True
print(text3.isdigit())    # True
print(text3.isnumeric())  # True

# Check if valid identifier
identifier = "_user_123"
print(identifier.isidentifier())  # True

# Check case
print("HELLO".isupper())  # True
print("hello".islower())  # True
print("Hello World".istitle())  # True

# Check whitespace
print("   ".isspace())    # True
print("".isspace())       # False
```

### 3.4 String Formatting Methods

```python
# Format method
name = "Maaz"
age = 25
formatted = "My name is {} and I'm {} years old".format(name, age)
print(formatted)

# Format with named placeholders
lunch = {"Food": "Pizza", "Drink": "Wine", "mobile": "Mi"}
formatted_lunch = "Lunch: {Food}, {Drink}, {mobile}".format_map(lunch)
print(formatted_lunch)

# f-string (Python 3.6+)
result = f"My name is {name} and I'm {age} years old"
print(result)

# Format with alignment and padding
number = 42
print(f"{number:>10}")    # Right align in 10 characters
print(f"{number:<10}")    # Left align in 10 characters
print(f"{number:^10}")    # Center align in 10 characters
print(f"{number:010}")    # Zero padding
```

### 3.5 String Modification Methods

```python
text = "  Hello World  "

# Remove whitespace
print(text.strip())       # "Hello World"
print(text.lstrip())      # "Hello World  "
print(text.rstrip())      # "  Hello World"

# Replace substring
message = "Hello World"
print(message.replace("World", "Python"))  # "Hello Python"
print(message.replace("l", "L", 1))         # "HeLlo World" (replace only first)

# Split string
sentence = "Python,Java,JavaScript,C++"
languages = sentence.split(",")
print(languages)  # ['Python', 'Java', 'JavaScript', 'C++']

# Join strings
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(joined)  # "Python is awesome"

# Partition
text = "name=value"
result = text.partition("=")
print(result)  # ('name', '=', 'value')
```

### 3.6 String Alignment Methods

```python
text = "Python"

# Center align
print(text.center(20, '-'))  # "-------Python-------"

# Left justify
print(text.ljust(20, '-'))   # "Python--------------"

# Right justify
print(text.rjust(20, '-'))   # "--------------Python"

# Zero fill
number = "42"
print(number.zfill(5))       # "00042"
```

## 4. Common Errors in String

### 4.1 String Immutability Error

```python
# ❌ WRONG - Strings are immutable(unchangeable)
text = "Hello"
# text[0] = 'h'  # TypeError: 'str' object does not support item assignment

# ✅ CORRECT - Create new string
text = "Hello"
text = 'h' + text[1:]  # "hello"
```

### 4.2 Index Out of Range Error

```python
text = "Python"
# ❌ WRONG
# print(text[10])  # IndexError: string index out of range

# ✅ CORRECT - Check length first
if len(text) > 10:
    print(text[10])
else:
    print("Index out of range")
```

### 4.3 Type Conversion Errors

```python
# ❌ WRONG - Concatenating string with number
name = "Age: "
age = 25
# result = name + age  # TypeError: can only concatenate str to str

# ✅ CORRECT - Convert to string first
result = name + str(age)
# Or use f-string
result = f"{name}{age}"
```

### 4.4 Encoding/Decoding Errors

```python
# ❌ WRONG - Mixing bytes and strings
text = "Hello"
# result = text + b"World"  # TypeError: can only concatenate str to str

# ✅ CORRECT - Convert appropriately
text = "Hello"
byte_text = b"World"
result = text + byte_text.decode('utf-8')
```

### 4.5 Escape Character Errors

```python
# ❌ WRONG - Forgetting to escape
# path = "C:\Users\Name\Documents"  # Invalid escape sequence

# ✅ CORRECT - Use raw strings or double backslashes
path = r"C:\Users\Name\Documents"
# or
path = "C:\\Users\\Name\\Documents"
```

### 4.6 Method Return Value Errors

```python
# ❌ WRONG - Expecting methods to modify original string
text = "hello world"
text.upper()  # This doesn't change 'text'
print(text)   # Still "hello world"

# ✅ CORRECT - Assign the return value
text = "hello world"
text = text.upper()
print(text)   # "HELLO WORLD"
```

### 4.7 String Comparison Errors

```python
# ❌ WRONG - Case-sensitive comparison
user_input = "YES"
# if user_input == "yes":  # This will be False

# ✅ CORRECT - Case-insensitive comparison
if user_input.lower() == "yes":
    print("User confirmed")
```

### 4.8 Split Method Errors

```python
# ❌ WRONG - Not handling empty strings
text = ""
# parts = text.split(",")  # Returns [''] not []

# ✅ CORRECT - Check for empty string
text = ""
parts = text.split(",") if text else []
```

### 4.9 Format String Errors

```python
# ❌ WRONG - Mismatched placeholders
name = "Maaz"
# result = "Hello {} and {}".format(name)  # IndexError: tuple index out of range

# ✅ CORRECT - Match placeholders with arguments
result = "Hello {} and welcome".format(name)
# or
result = "Hello {name} and welcome".format(name=name)
```

### 4.10 Unicode Handling Errors

```python
# ❌ WRONG - Not handling special characters
text = "café"
# encoded = text.encode('ascii')  # UnicodeEncodeError

# ✅ CORRECT - Handle encoding errors
encoded = text.encode('ascii', errors='ignore')  # b'caf'
# or
encoded = text.encode('utf-8')  # b'caf\xc3\xa9'
```
