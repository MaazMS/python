# Python Conditional Statements Documentation

## 1. Definitions and Characteristics

### if Statement

The `if` statement is used to execute a block of code only when a specified condition evaluates to `True`. It's the most basic form of conditional execution in Python.

**Characteristics:**

- Executes code block only if condition is `True`
- Single condition evaluation
- No alternative execution path
- Uses indentation to define code blocks

**Syntax:**

```python
if condition:
    statement(s)
```

**Example:**

```python
age = 18
if age >= 18:
    print("You are eligible to vote!")
```

### if..else Statement

The `if..else` statement provides two execution paths: one when the condition is `True` and another when it's `False`. It ensures that one of the two blocks will always execute.

**Characteristics:**

- Provides binary decision making
- Guarantees one block will execute
- Mutually exclusive execution paths
- Covers all possible outcomes for a single condition

**Syntax:**

```python
if condition:
    statement(s)
else:
    statement(s)
```

**Example:**

```python
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot today.")
```

### if..elif Statement

The `if..elif` statement allows multiple condition checking in sequence. It evaluates conditions one by one until a `True` condition is found, then executes that block and skips the rest.

**Characteristics:**

- Multiple condition evaluation
- Sequential condition checking (short-circuit evaluation)
- First `True` condition wins
- Can be combined with `else` for default case
- More efficient than multiple separate `if` statements

**Syntax:**

```python
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
# ... more elif blocks as needed
else:  # optional
    statement(s)
```

**Example:**

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

## 2. Operations and Practical Examples

### if Statement Operations

**Basic Comparison:**

```python
# Numeric comparison
number = 10
if number > 5:
    print(f"{number} is greater than 5")

# String comparison
name = "Alice"
if name == "Alice":
    print("Hello Alice!")

# Boolean check
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
```

**Membership Testing:**

```python
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is available!")

# String containment
text = "Hello World"
if "World" in text:
    print("Found 'World' in the text")
```

**Type Checking:**

```python
value = 42
if isinstance(value, int):
    print("Value is an integer")
```

### if..else Statement Operations

**Input Validation:**

```python
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

**File Operations:**

```python
import os
filename = "data.txt"
if os.path.exists(filename):
    print(f"File {filename} exists. Reading content...")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
else:
    print(f"File {filename} not found. Creating new file...")
    with open(filename, 'w') as file:
        file.write("New file created!")
```

**Authentication Logic:**

```python
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Access granted!")
else:
    print("Access denied! Invalid credentials.")
```

### if..elif Statement Operations

**Menu System:**

```python
def display_menu():
    print("1. Create new file")
    print("2. Open existing file")
    print("3. Delete file")
    print("4. Exit")
    
choice = input("Enter your choice (1-4): ")

if choice == "1":
    filename = input("Enter filename: ")
    print(f"Creating file: {filename}")
elif choice == "2":
    filename = input("Enter filename to open: ")
    print(f"Opening file: {filename}")
elif choice == "3":
    filename = input("Enter filename to delete: ")
    print(f"Deleting file: {filename}")
elif choice == "4":
    print("Goodbye!")
else:
    print("Invalid choice! Please select 1-4.")
```

**Grade Calculator:**

```python
def calculate_grade(percentage):
    if percentage >= 97:
        return "A+"
    elif percentage >= 93:
        return "A"
    elif percentage >= 90:
        return "A-"
    elif percentage >= 87:
        return "B+"
    elif percentage >= 83:
        return "B"
    elif percentage >= 80:
        return "B-"
    elif percentage >= 77:
        return "C+"
    elif percentage >= 73:
        return "C"
    elif percentage >= 70:
        return "C-"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

student_score = 85
grade = calculate_grade(student_score)
print(f"Score: {student_score}% - Grade: {grade}")
```

**Complex Condition Handling:**

```python
age = 25
income = 50000
credit_score = 750

if age >= 18 and income >= 30000 and credit_score >= 700:
    print("Loan approved!")
elif age >= 21 and income >= 25000 and credit_score >= 650:
    print("Loan approved with higher interest rate")
elif age >= 18 and (income >= 40000 or credit_score >= 800):
    print("Loan approved with collateral required")
else:
    print("Loan application rejected")
```

## 3. Common Errors and How to Avoid Them

### Syntax Errors

#### Error 1: Missing Colon

```python
# ❌ Incorrect
if x > 5
    print("Greater than 5")

# ✅ Correct
if x > 5:
    print("Greater than 5")
```

#### Error 2: Incorrect Indentation

```python
# ❌ Incorrect
if x > 5:
print("Greater than 5")  # Missing indentation

# ✅ Correct
if x > 5:
    print("Greater than 5")  # Properly indented
```

#### Error 3: Missing Condition in elif

```python
# ❌ Incorrect
if score >= 90:
    print("A grade")
elif:  # Missing condition
    print("Other grade")

# ✅ Correct
if score >= 90:
    print("A grade")
elif score >= 80:  # Condition provided
    print("B grade")
```

### Logic Errors

#### Error 4: Unreachable Code

```python
# ❌ Incorrect - Second condition will never be reached
if score >= 80:
    print("Good score")
elif score >= 90:  # This will never execute
    print("Excellent score")

# ✅ Correct - Order conditions from most specific to least specific
if score >= 90:
    print("Excellent score")
elif score >= 80:
    print("Good score")
```

#### Error 5: Using Assignment (=) Instead of Comparison (==)

```python
# ❌ Incorrect
if x = 5:  # Assignment, not comparison
    print("x is 5")

# ✅ Correct
if x == 5:  # Comparison
    print("x is 5")
```

#### Error 6: Comparing Different Data Types

```python
# ❌ Potentially problematic
age = input("Enter age: ")  # Returns string
if age > 18:  # Comparing string with integer
    print("Adult")

# ✅ Correct
age = int(input("Enter age: "))  # Convert to integer
if age > 18:
    print("Adult")
```

### Best Practices to Avoid Errors

1. Always use proper indentation (4 spaces recommended)
2. Don't forget the colon (:) after conditions
3. Use parentheses for complex conditions to improve readability
4. Order elif conditions from most specific to most general
5. Use meaningful variable names
6. Test edge cases and boundary conditions
7. Consider using elif instead of multiple separate if statements when conditions are mutually exclusive

#### Example of Good Practice

```python
def categorize_temperature(temp):
    """Categorize temperature with proper error handling."""
    if not isinstance(temp, (int, float)):
        return "Invalid temperature type"
    
    if temp < -273.15:
        return "Invalid temperature (below absolute zero)"
    elif temp < 0:
        return "Freezing"
    elif temp < 20:
        return "Cold"
    elif temp < 30:
        return "Comfortable"
    elif temp < 40:
        return "Hot"
    else:
        return "Extremely hot"

# Test the function
print(categorize_temperature(25))    # Comfortable
print(categorize_temperature(-5))    # Freezing
print(categorize_temperature("hot")) # Invalid temperature type
```
