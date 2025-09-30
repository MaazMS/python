# Python Loop Control Keywords Documentation

## 1. Definitions and Characteristics

### continue Statement

The `continue` statement is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration of the loop. It doesn't terminate the loop but jumps to the beginning of the loop for the next iteration.

#### Characteristics of continue

- **Skips current iteration**: Jumps to the next iteration without executing remaining code in the loop body
- **Loop continues**: The loop doesn't terminate, only the current iteration is skipped
- **Works with all loops**: Can be used in for loops, while loops, and nested loops
- **Conditional usage**: Typically used with if statements to skip based on conditions
- **No return value**: It's a control flow statement, not a function

#### Syntax of continue

```python
for item in sequence:
    if condition:
        continue  # Skip rest of this iteration
    # This code is skipped when continue executes
    statement(s)
```

#### Basic Example of continue

```python
# Print only odd numbers
for num in range(1, 11):
    if num % 2 == 0:  # If even number
        continue      # Skip to next iteration
    print(f"Odd number: {num}")
```

### break Statement

The `break` statement is used to exit/terminate a loop prematurely when a certain condition is met. It completely stops the execution of the loop and transfers control to the statement immediately after the loop.

#### Characteristics of break

- **Terminates loop**: Completely exits the loop when executed
- **Immediate exit**: Control transfers to the first statement after the loop
- **Works with all loops**: Can be used in for loops, while loops, and nested loops
- **Prevents infinite loops**: Useful for creating exit conditions in while loops
- **Affects innermost loop**: In nested loops, only exits the innermost loop containing the break

#### Syntax of break

```python
for item in sequence:
    if condition:
        break  # Exit the loop completely
    statement(s)
# Control comes here after break
```

#### Basic Example of break

```python
# Find first number divisible by 7
numbers = [12, 15, 21, 28, 33, 35]
for num in numbers:
    if num % 7 == 0:
        print(f"Found first number divisible by 7: {num}")
        break  # Exit loop after finding first match
    print(f"Checking {num}...")
```

### pass Statement

The `pass` statement is a null operation - it does nothing when executed. It's used as a placeholder where syntactically some code is required, but no action needs to be performed.

#### Characteristics of pass

- **Null operation**: Does absolutely nothing when executed
- **Syntactic placeholder**: Used where Python syntax requires a statement
- **No effect on execution**: Doesn't affect loop flow or program logic
- **Useful in development**: Allows creating empty code blocks during development
- **No performance impact**: Optimized away by Python interpreter

#### Syntax of pass

```python
if condition:
    pass  # Placeholder - do nothing
else:
    statement(s)
```

#### Basic Example of pass

```python
# Placeholder for future implementation
for num in range(1, 6):
    if num == 3:
        pass  # TODO: Add special handling for 3
    else:
        print(f"Processing number: {num}")
```

#### Comparison Table

| Keyword | Purpose | Effect on Loop | Use Case |
|---------|---------|----------------|----------|
| **continue** | Skip current iteration | Continues to next iteration | Skip specific values/conditions |
| **break** | Exit loop completely | Terminates loop | Early termination, found target |
| **pass** | Do nothing | No effect | Placeholder, empty code blocks |

## 2. Operations and Practical Examples

### continue Operations

#### Filtering with continue

```python
# Process only positive numbers
numbers = [5, -2, 8, -1, 12, 0, -7, 15]
positive_sum = 0

for num in numbers:
    if num <= 0:
        print(f"Skipping non-positive number: {num}")
        continue
    
    positive_sum += num
    print(f"Added {num}, running sum: {positive_sum}")

print(f"Total of positive numbers: {positive_sum}")
```

#### String Processing with continue

```python
# Count only alphabetic characters
text = "Hello, World! 123"
letter_count = 0

for char in text:
    if not char.isalpha():
        continue  # Skip non-alphabetic characters
    
    letter_count += 1
    print(f"Letter found: '{char}' (count: {letter_count})")

print(f"Total letters: {letter_count}")
```

#### Data Validation with continue

```python
# Process valid email addresses
emails = ["user@example.com", "invalid-email", "test@domain.org", "", "admin@site.net"]

valid_emails = []
for email in emails:
    # Skip empty or invalid emails
    if not email or "@" not in email or "." not in email:
        print(f"Skipping invalid email: '{email}'")
        continue
    
    valid_emails.append(email)
    print(f"Valid email added: {email}")

print(f"Total valid emails: {len(valid_emails)}")
```

### break Operations

#### Search Operations with break

```python
# Find student in class list
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target_student = "Charlie"

for i, student in enumerate(students):
    print(f"Checking student {i+1}: {student}")
    if student == target_student:
        print(f"Found {target_student} at position {i+1}")
        break
else:
    print(f"{target_student} not found in class list")
```

#### Input Validation with break

```python
# Get valid input from user
max_attempts = 3
attempt = 0

while attempt < max_attempts:
    try:
        age = int(input(f"Enter your age (Attempt {attempt + 1}): "))
        if 0 <= age <= 120:
            print(f"Valid age entered: {age}")
            break  # Exit loop on valid input
        else:
            print("Age must be between 0 and 120")
    except ValueError:
        print("Please enter a valid number")
    
    attempt += 1
else:
    print("Maximum attempts exceeded")
```

#### Game Loop with break

```python
import random

# Simple number guessing game
secret = random.randint(1, 20)
attempts = 0
max_attempts = 5

print(f"Guess the number between 1 and 20! You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: "))
        attempts += 1
        
        if guess == secret:
            print(f"🎉 Correct! You guessed {secret} in {attempts} attempts!")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
            
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"You have {remaining} attempts left")
            
    except ValueError:
        print("Please enter a valid number")
        attempts -= 1  # Don't count invalid input
else:
    print(f"😞 Game over! The number was {secret}")
```

### pass Operations

#### Placeholder in Development

```python
# Code structure during development
def process_data(data):
    """Process incoming data - implementation pending"""
    
    # Input validation
    if not data:
        return None
    
    # Data cleaning (TODO)
    if len(data) > 1000:
        pass  # TODO: Implement data chunking
    
    # Data transformation (TODO)
    for item in data:
        if item.startswith('ERROR'):
            pass  # TODO: Implement error handling
        elif item.startswith('WARNING'):
            pass  # TODO: Implement warning processing
        else:
            print(f"Processing: {item}")
    
    return data
```

#### Exception Handling Placeholder

```python
# Graceful error handling
files = ["data1.txt", "data2.txt", "missing.txt", "data3.txt"]

for filename in files:
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Successfully read {filename}")
    except FileNotFoundError:
        print(f"Warning: {filename} not found")
        pass  # Continue processing other files
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        pass  # Continue with other files
```

#### Class Definition Placeholder

```python
# Abstract base classes during design phase
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass  # Subclasses will implement this
    
    def move(self):
        pass  # Subclasses will implement this

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says Woof!"
    
    def move(self):
        return f"{self.name} runs on four legs"

# Usage
dog = Dog("Buddy")
print(dog.make_sound())
print(dog.move())
```

## 3. Methods and Advanced Usage

### continue in Different Loop Types

#### continue in while loops

```python
# Process user input until valid
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    user_input = input("Enter a positive number: ")
    attempts += 1
    
    try:
        number = float(user_input)
        if number <= 0:
            print("Number must be positive")
            continue  # Skip to next iteration
        
        # Valid input - process it
        print(f"Processing number: {number}")
        print(f"Square: {number ** 2}")
        break
        
    except ValueError:
        print("Invalid input - please enter a number")
        continue  # Skip to next iteration

if attempts >= max_attempts:
    print("Maximum attempts exceeded")
```

#### continue with enumerate

```python
# Process list items with index, skip specific indices
items = ["apple", "banana", "cherry", "date", "elderberry"]
skip_indices = {1, 3}  # Skip banana and date

for index, item in enumerate(items):
    if index in skip_indices:
        print(f"Skipping item {index}: {item}")
        continue
    
    print(f"Processing item {index}: {item.upper()}")
```

### break in Different Contexts

#### break with nested loops

```python
# Find first pair that sums to target
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
target = 10
found = False

print(f"Looking for two numbers that sum to {target}:")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Found pair: {numbers[i]} + {numbers[j]} = {target}")
            found = True
            break  # Break inner loop
    
    if found:
        break  # Break outer loop

if not found:
    print("No pair found")
```

#### break with else clause

```python
# Search for prime number
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Found divisor
    return True

# Find first prime number in range
start_range = 20
for num in range(start_range, start_range + 20):
    if is_prime(num):
        print(f"First prime number >= {start_range}: {num}")
        break
else:
    print(f"No prime number found in range {start_range}-{start_range + 19}")
```

### pass in Advanced Scenarios

#### pass in exception handling

```python
# Robust file processing with selective error handling
import os

def process_files(file_list):
    processed = 0
    errors = []
    
    for filename in file_list:
        try:
            # Simulate file processing
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File not found: {filename}")
            
            # Process file here
            print(f"Processing {filename}...")
            processed += 1
            
        except FileNotFoundError as e:
            errors.append(str(e))
            pass  # Continue with next file
            
        except PermissionError:
            errors.append(f"Permission denied: {filename}")
            pass  # Continue with next file
            
        except Exception as e:
            # Log unexpected errors but continue
            errors.append(f"Unexpected error with {filename}: {e}")
            pass
    
    return processed, errors
```

## 4. Common Errors and How to Avoid Them

### continue Statement Errors

#### Error 1: continue Outside Loop

```python
# ❌ Incorrect - continue outside loop
def process_number(num):
    if num < 0:
        continue  # SyntaxError: 'continue' not properly in loop
    return num * 2

# ✅ Correct - Use return or conditional logic
def process_number(num):
    if num < 0:
        return None  # or raise exception
    return num * 2
```

#### Error 2: Infinite Loop with continue

```python
# ❌ Incorrect - Infinite loop
count = 0
while count < 10:
    if count % 2 == 0:
        continue  # count never incremented!
    print(count)
    count += 1

# ✅ Correct - Increment before continue
count = 0
while count < 10:
    count += 1  # Increment first
    if count % 2 == 0:
        continue
    print(count)
```

### break Statement Errors

#### Error 3: break Outside Loop

```python
# ❌ Incorrect - break outside loop
def find_item(items, target):
    if target in items:
        break  # SyntaxError: 'break' outside loop

# ✅ Correct - Use return or proper loop structure
def find_item(items, target):
    if target in items:
        return True
    return False
```

#### Error 4: break in nested loops confusion

```python
# ❌ Problematic - break only exits inner loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5

for row in matrix:
    for num in row:
        if num == target:
            print(f"Found {target}")
            break  # Only exits inner loop
    print("This still executes for remaining rows")

# ✅ Correct - Use flag or function return
found = False
for row in matrix:
    for num in row:
        if num == target:
            print(f"Found {target}")
            found = True
            break
    if found:
        break
```

### pass Statement Errors

#### Error 5: Unnecessary pass usage

```python
# ❌ Unnecessary - pass not needed here
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        pass  # Unnecessary - else block can be empty or omitted

# ✅ Better - Omit unnecessary else or use meaningful action
def greet(name):
    if name:
        print(f"Hello, {name}!")
    # No else needed
```

#### Error 6: pass where action is needed

```python
# ❌ Problematic - pass where error handling is needed
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        pass  # Silent failure - bad practice!

# ✅ Correct - Proper error handling
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Or raise exception
```

### Best Practices to Avoid Errors

1. **Use continue and break only inside loops**
2. **Always ensure loop variables are updated** before continue
3. **Use flags or functions** to break out of nested loops
4. **Understand loop-else behavior** - else executes when break is NOT used
5. **Use pass sparingly** - only as genuine placeholder
6. **Don't ignore errors with pass** - handle them appropriately
7. **Comment your intentions** when using these keywords
8. **Consider more Pythonic alternatives** like list comprehensions

#### Example of Good Practices

```python
def process_user_data(users):
    """
    Process user data with proper error handling and loop control.
    Demonstrates best practices for continue, break, and pass.
    """
    processed_users = []
    error_count = 0
    
    for user in users:
        try:
            # Skip invalid users
            if not user or not isinstance(user, dict):
                print(f"Skipping invalid user data: {user}")
                continue
            
            # Required field validation
            if 'name' not in user or 'email' not in user:
                print(f"Skipping user with missing required fields: {user}")
                continue
            
            # Email validation
            email = user['email']
            if '@' not in email or '.' not in email:
                print(f"Skipping user with invalid email: {email}")
                continue
            
            # Process valid user
            processed_user = {
                'name': user['name'].strip().title(),
                'email': email.lower().strip(),
                'id': len(processed_users) + 1
            }
            
            processed_users.append(processed_user)
            print(f"Processed user: {processed_user['name']}")
            
            # Stop if we've processed enough users
            if len(processed_users) >= 10:
                print("Reached maximum user limit")
                break
                
        except Exception as e:
            error_count += 1
            print(f"Error processing user {user}: {e}")
            # Continue processing other users instead of failing completely
            continue
    
    return processed_users, error_count

# Example usage
sample_users = [
    {'name': 'alice', 'email': 'alice@example.com'},
    {'name': 'bob'},  # Missing email
    {'name': 'charlie', 'email': 'invalid-email'},
    {'name': 'diana', 'email': 'diana@test.org'},
    None,  # Invalid user data
]

processed, errors = process_user_data(sample_users)
print(f"\nSummary: {len(processed)} users processed, {errors} errors encountered")
```
