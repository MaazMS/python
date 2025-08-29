# Regular Expressions Documentation

## 1. Definitions and Characteristics

### Regular Expressions

Regular expressions (also known as **REGEX** or **RegExp**) are sequences of characters that define search patterns. They are used for:

1. Pattern matching: Finding specific patterns in text
2. String validation: Checking if input follows a specific format (email, phone, password)
3. Text processing: Extracting, replacing, or splitting text based on patterns
4. Data cleaning: Removing unwanted characters or formatting text

**Characteristics:**

- Case-sensitive by default
- Uses special metacharacters with specific meanings
- Supports both literal and pattern matching
- Can be compiled for better performance

```python
import re

# Basic pattern matching
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
text = "user@example.com"
if re.match(email_pattern, text):
    print("Valid email")
```

### Sequence Characters

Sequence characters are predefined character classes that match specific types of characters:

| Character | Description | Example Match |
|-----------|-------------|---------------|
| `\d` | Any digit (0-9) | '5', '0', '9' |
| `\D` | Any non-digit | 'a', '@', ' ' |
| `\w` | Any word character (letters, digits, underscore) | 'A', '5', '_' |
| `\W` | Any non-word character | '@', ' ', '!' |
| `\s` | Any whitespace (space, tab, newline) | ' ', '\t', '\n' |
| `\S` | Any non-whitespace | 'a', '5', '@' |
| `\b` | Word boundary | Between word and non-word |
| `\A` | Start of string | Beginning only |
| `\Z` | End of string | End only |

```python
import re

text = "Hello World 123!"

# Find all digits
digits = re.findall(r'\d', text)  # ['1', '2', '3']

# Find all word characters
words = re.findall(r'\w+', text)  # ['Hello', 'World', '123']

# Find whitespace
spaces = re.findall(r'\s', text)  # [' ']
```

## 2. Operations

### Search Operations

```python
import re

text = "The price is $25.99 and tax is $3.75"

# Basic search - finds first match
price_match = re.search(r'\$\d+\.\d{2}', text)
if price_match:
    print(f"Found: {price_match.group()}")  # Found: $25.99

# Case-insensitive search
text2 = "HELLO world"
match = re.search(r'hello', text2, re.IGNORECASE)  # Matches "HELLO"

# Multiple patterns
email_or_phone = re.search(r'(\w+@\w+\.\w+|\d{3}-\d{3}-\d{4})', 
                          "Contact: john@email.com")
```

### Group Operations

```python
import re

text = "Born on 1990-05-15 in New York"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)

if match:
    print(f"Full match: {match.group()}")      # 1990-05-15
    print(f"Year: {match.group(1)}")           # 1990
    print(f"Month: {match.group(2)}")          # 05
    print(f"Day: {match.group(3)}")            # 15
    print(f"All groups: {match.groups()}")     # ('1990', '05', '15')
```

### FindAll Operations

```python
import re

log_text = """
2023-01-15 ERROR: Database connection failed
2023-01-15 INFO: Server started
2023-01-16 WARNING: Low disk space
2023-01-16 ERROR: Authentication failed
"""

# Find all dates
dates = re.findall(r'\d{4}-\d{2}-\d{2}', log_text)
# ['2023-01-15', '2023-01-15', '2023-01-16', '2023-01-16']

# Find all log levels
levels = re.findall(r'(ERROR|INFO|WARNING)', log_text)
# ['ERROR', 'INFO', 'WARNING', 'ERROR']

# Find complete log entries
entries = re.findall(r'(\d{4}-\d{2}-\d{2}) (\w+): (.+)', log_text)
# [('2023-01-15', 'ERROR', 'Database connection failed'), ...]
```

### Match Operations

```python
import re

# Match only at beginning of string
text1 = "Hello World"
text2 = "Say Hello World"

match1 = re.match(r'Hello', text1)  # Matches
match2 = re.match(r'Hello', text2)  # None (doesn't start with Hello)

# Using match with groups
email = "user@domain.com"
email_match = re.match(r'(\w+)@(\w+)\.(\w+)', email)
if email_match:
    username = email_match.group(1)  # 'user'
    domain = email_match.group(2)    # 'domain'
    extension = email_match.group(3) # 'com'
```

### Split Operations

```python
import re

# Split on multiple delimiters
text = "apple,banana;orange:grape|mango"
fruits = re.split(r'[,;:|]', text)
# ['apple', 'banana', 'orange', 'grape', 'mango']

# Split on whitespace (including multiple spaces)
sentence = "This   has    irregular     spacing"
words = re.split(r'\s+', sentence)
# ['This', 'has', 'irregular', 'spacing']

# Split and keep delimiters
text2 = "Section1::Section2::Section3"
parts = re.split(r'(::)', text2)
# ['Section1', '::', 'Section2', '::', 'Section3']

# Limit splits
text3 = "a-b-c-d-e"
limited = re.split(r'-', text3, maxsplit=2)
# ['a', 'b', 'c-d-e']
```

### Substitution Operations

```python
import re

# Basic substitution
text = "I have 5 apples and 3 oranges"
result = re.sub(r'\d+', 'many', text)
# "I have many apples and many oranges"

# Advanced substitution with groups
phone = "Call me at (555) 123-4567"
formatted = re.sub(r'\((\d{3})\) (\d{3})-(\d{4})', r'\1-\2-\3', phone)
# "Call me at 555-123-4567"

# Conditional substitution with function
def replace_numbers(match):
    num = int(match.group())
    return "small" if num < 10 else "large"

text2 = "I have 5 cats and 15 dogs"
result2 = re.sub(r'\d+', replace_numbers, text2)
# "I have small cats and large dogs"

# Count replacements
text3 = "red red red blue"
result3, count = re.subn(r'red', 'green', text3)
# result3: "green green green blue", count: 3
```

### Quantifiers

Quantifiers specify how many times a character or group should be matched:

| Quantifier | Description | Example |
|------------|-------------|---------||
| `+` | One or more | `\d+` matches "123" |
| `*` | Zero or more | `\d*` matches "" or "123" |
| `?` | Zero or one | `\d?` matches "" or "5" |
| `{n}` | Exactly n times | `\d{3}` matches "123" |
| `{n,}` | n or more times | `\d{3,}` matches "123" or "1234" |
| `{n,m}` | Between n and m times | `\d{2,4}` matches "12", "123", "1234" |

```python
import re

text = "Phone: 123-456-7890, Code: 12345"

# Find phone number pattern
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)  # "123-456-7890"

# Find any sequence of digits
all_numbers = re.findall(r'\d+', text)  # ['123', '456', '7890', '12345']

# Optional area code
pattern = r'\(?\d{3}\)?-?\d{3}-?\d{4}'
```

### Special Characters

Special characters have specific meanings in regex patterns:

| Character | Description | Example |
|-----------|-------------|---------||
| `.` | Any character except newline | `a.c` matches "abc", "a5c" |
| `^` | Start of string/line | `^Hello` matches "Hello world" |
| `$` | End of string/line | `world$` matches "Hello world" |
| `[]` | Character set | `[aeiou]` matches any vowel |
| `[^]` | Negated character set | `[^0-9]` matches non-digits |
| `()` | Grouping | `(ab)+` matches "ab", "abab" |
| `|` | Alternation (OR) | `cat|dog` matches "cat" or "dog" |
| `\` | Escape character | `\.` matches literal "." |

```python
import re

text = "Visit www.example.com or https://test.org"

# Match any website
websites = re.findall(r'www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

# Match start of string
starts_with = re.match(r'^Visit', text)  # Matches

# Character sets
vowels = re.findall(r'[aeiou]', text)  # All vowels
consonants = re.findall(r'[^aeiou\s]', text.lower())  # All consonants
```

## 3. Methods

### re.compile()

Pre-compile patterns for better performance:

```python
import re

# Compile pattern once, use multiple times
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

emails = ["user@example.com", "invalid.email", "test@domain.org"]
for email in emails:
    if email_pattern.match(email):
        print(f"{email} is valid")

# Compiled pattern methods
pattern = re.compile(r'\d+')
text = "I have 5 apples and 10 oranges"

# All methods available on compiled pattern
matches = pattern.findall(text)      # ['5', '10']
first_match = pattern.search(text)   # Match object for '5'
split_result = pattern.split(text)   # ['I have ', ' apples and ', ' oranges']
```

### Match Object Methods

```python
import re

text = "Contact: john.doe@email.com, Phone: 123-456-7890"
pattern = r'(\w+)\.(\w+)@(\w+)\.(\w+)'
match = re.search(pattern, text)

if match:
    # Group methods
    print(f"Full match: {match.group()}")      # john.doe@email.com
    print(f"First name: {match.group(1)}")     # john
    print(f"Last name: {match.group(2)}")      # doe
    print(f"Domain: {match.group(3)}")         # email
    print(f"Extension: {match.group(4)}")      # com
    
    # Position methods
    print(f"Start position: {match.start()}")  # 9
    print(f"End position: {match.end()}")      # 26
    print(f"Span: {match.span()}")             # (9, 26)
    
    # All groups
    print(f"All groups: {match.groups()}")     # ('john', 'doe', 'email', 'com')
```

### re.finditer()

Returns iterator of match objects:

```python
import re

text = "Prices: $10.50, $25.99, $5.00"
pattern = r'\$(\d+)\.(\d{2})'

for match in re.finditer(pattern, text):
    dollars = match.group(1)
    cents = match.group(2)
    start_pos = match.start()
    end_pos = match.end()
    print(f"Found ${dollars}.{cents} at position {start_pos}-{end_pos}")

# Output:
# Found $10.50 at position 8-14
# Found $25.99 at position 16-22
# Found $5.00 at position 24-29
```

### Named Groups

```python
import re

# Define pattern with named groups
log_pattern = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+): (?P<message>.+)')
log_entry = "2023-01-15 ERROR: Database connection failed"

match = log_pattern.match(log_entry)
if match:
    # Access by name
    print(f"Date: {match.group('date')}")      # 2023-01-15
    print(f"Level: {match.group('level')}")    # ERROR
    print(f"Message: {match.group('message')}")# Database connection failed
    
    # Get all named groups as dictionary
    print(f"All groups: {match.groupdict()}")
    # {'date': '2023-01-15', 'level': 'ERROR', 'message': 'Database connection failed'}
```

### Flags and Modifiers

```python
import re

text = """First Line
Second LINE
Third line"""

# Case insensitive
matches1 = re.findall(r'line', text, re.IGNORECASE)
# ['Line', 'LINE', 'line']

# Multiline mode (^ and $ match line boundaries)
matches2 = re.findall(r'^Second', text, re.MULTILINE)
# ['Second']

# Dot matches newline
matches3 = re.findall(r'First.*Third', text, re.DOTALL)
# ['First Line\nSecond LINE\nThird']

# Verbose mode (allows comments and whitespace)
email_pattern = re.compile(r'''
    ^                    # Start of string
    [a-zA-Z0-9._%+-]+    # Username part
    @                    # @ symbol
    [a-zA-Z0-9.-]+       # Domain name
    \.                   # Dot
    [a-zA-Z]{2,}         # Top-level domain
    $                    # End of string
''', re.VERBOSE)
```

## 4. Common Errors and Solutions

### Error 1: Forgetting to Escape Special Characters

```python
import re

# WRONG: Special characters not escaped
text = "Price: $25.99"
wrong = re.search(r'$25.99', text)  # Won't work - $ and . are special

# CORRECT: Escape special characters
correct = re.search(r'\$25\.99', text)  # Works correctly

# Alternative: Use re.escape()
price = "$25.99"
escaped_price = re.escape(price)
pattern = re.compile(escaped_price)

# Example of characters that need escaping
special_chars = r'. ^ $ * + ? { } [ ] \ | ( )'
```

### Error 2: Greedy vs Non-Greedy Matching

```python
import re

html = '<div>Content 1</div><div>Content 2</div>'

# WRONG: Greedy matching gets too much
greedy = re.search(r'<div>.*</div>', html)
print(greedy.group())  # Gets entire string: '<div>Content 1</div><div>Content 2</div>'

# CORRECT: Non-greedy matching
non_greedy = re.search(r'<div>.*?</div>', html)
print(non_greedy.group())  # Gets only first div: '<div>Content 1</div>'

# More examples of greedy vs non-greedy
text = 'The "quick" brown "fox" jumps'
greedy_quotes = re.findall(r'".*"', text)      # ['"quick" brown "fox"']
non_greedy_quotes = re.findall(r'".*?"', text) # ['"quick"', '"fox"']
```

### Error 3: Not Handling None Results

```python
import re

text = "No numbers here"

# WRONG: Can cause AttributeError
try:
    result = re.search(r'\d+', text)
    print(result.group())  # Error if no match
except AttributeError:
    print("No match found")

# CORRECT: Check for None
result = re.search(r'\d+', text)
if result:
    print(result.group())
else:
    print("No match found")

# BETTER: Using walrus operator (Python 3.8+)
if (result := re.search(r'\d+', text)):
    print(result.group())
else:
    print("No match found")
```

### Best Practices Summary

1. **Always check for None** before calling methods on match objects
2. **Escape special characters** when matching literal text using `re.escape()`
3. **Use non-greedy quantifiers** (`*?`, `+?`) when needed
4. **Compile patterns** that are used multiple times
5. **Use raw strings** (`r''`) for regex patterns
6. **Test patterns** with various inputs including edge cases
7. **Use named groups** for complex patterns to improve readability
8. **Be aware of greedy vs non-greedy** matching behavior
9. **Understand anchors** (`^`, `$`, `\b`) and their contexts
10. **Consider performance** implications of complex patterns
11. **Handle Unicode** properly when working with international text
12. **Use appropriate flags** (`re.IGNORECASE`, `re.MULTILINE`, etc.) when needed
