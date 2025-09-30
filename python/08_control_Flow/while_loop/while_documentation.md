# Python While Loop Documentation

## 1. Definition and Characteristics

### While Loop

The `while` loop in Python is used to execute a block of statements repeatedly as long as a specified condition remains `True`. It's a pre-test loop, meaning the condition is evaluated before each iteration.

#### Characteristics

- **Pre-test loop**: Condition is checked before each iteration
- **Indefinite iteration**: Number of iterations depends on when condition becomes `False`
- **Condition-controlled**: Continues as long as condition evaluates to `True`
- **Flexible termination**: Can be controlled by multiple factors
- **Supports loop control**: Works with `break`, `continue`, and `else` statements
- **Risk of infinite loops**: If condition never becomes `False`

#### Syntax

```python
while condition:
    statement(s)
    # Optional: update variables that affect condition
```

#### Basic Example

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Important: update condition variable
print("Loop finished!")
```

#### Key Components

1. **Initialization**: Set up variables before the loop
2. **Condition**: Boolean expression that controls loop execution
3. **Body**: Statements executed in each iteration
4. **Update**: Modify variables to eventually make condition `False`

#### Comparison with For Loop

| Aspect | While Loop | For Loop |
|--------|------------|----------|
| **Best for** | Unknown number of iterations | Known number of iterations |
| **Control** | Condition-based | Sequence-based |
| **Initialization** | Manual (before loop) | Automatic |
| **Update** | Manual (in loop body) | Automatic |
| **Risk** | Infinite loops if not careful | Safer, finite iterations |

## 2. Operations and Practical Examples

### Basic While Loop Operations

#### Simple Counting

```python
# Count up
counter = 1
while counter <= 10:
    print(f"Number: {counter}")
    counter += 1

# Count down
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off! 🚀")
```

#### Sum Calculation

```python
# Calculate sum of numbers 1 to n
n = 10
total = 0
current = 1

while current <= n:
    total += current
    current += 1

print(f"Sum of numbers 1 to {n}: {total}")
```

#### Input Validation

```python
# Keep asking for valid input
while True:
    try:
        age = int(input("Enter your age (0-120): "))
        if 0 <= age <= 120:
            print(f"Valid age: {age}")
            break
        else:
            print("Age must be between 0 and 120")
    except ValueError:
        print("Please enter a valid number")
```

### Advanced While Loop Operations

#### Menu-Driven Program

```python
def show_menu():
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

running = True
while running:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("Thank you for using the calculator!")
        running = False
    elif choice in ['1', '2', '3', '4']:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                result = a + b
                operation = "addition"
            elif choice == '2':
                result = a - b
                operation = "subtraction"
            elif choice == '3':
                result = a * b
                operation = "multiplication"
            elif choice == '4':
                if b != 0:
                    result = a / b
                    operation = "division"
                else:
                    print("Error: Division by zero!")
                    continue
            
            print(f"Result of {operation}: {result}")
        except ValueError:
            print("Error: Please enter valid numbers!")
    else:
        print("Invalid choice! Please select 1-5.")
```

#### Game Loop Example

```python
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🎮 Number Guessing Game!")
    print(f"Guess a number between 1 and 100. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed {secret_number} in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.")
                
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input as attempt
    else:
        print(f"😞 Game over! The secret number was {secret_number}")

# Run the game
guessing_game()
```

### While Loop with Different Conditions

#### String Processing

```python
# Process characters until specific character found
text = "Hello, World!"
index = 0

while index < len(text) and text[index] != ',':
    print(f"Character at position {index}: '{text[index]}'")
    index += 1

if index < len(text):
    print(f"Found comma at position {index}")
```

#### Mathematical Sequences

```python
# Generate Fibonacci sequence until value exceeds 1000
a, b = 0, 1
fibonacci_sequence = [a, b]

while b <= 1000:
    next_fib = a + b
    if next_fib > 1000:
        break
    fibonacci_sequence.append(next_fib)
    a, b = b, next_fib

print("Fibonacci sequence (≤ 1000):")
print(fibonacci_sequence)
```

### Loop Control in While Loops

#### Using break

```python
# Search for item in list
items = ["apple", "banana", "cherry", "date", "elderberry"]
search_item = "cherry"
index = 0
found = False

while index < len(items):
    if items[index] == search_item:
        print(f"Found '{search_item}' at index {index}")
        found = True
        break
    index += 1

if not found:
    print(f"'{search_item}' not found in the list")
```

#### Using continue

```python
# Process only even numbers
number = 0
processed_count = 0

while processed_count < 5:
    number += 1
    
    if number % 2 != 0:  # Skip odd numbers
        continue
    
    print(f"Processing even number: {number}")
    processed_count += 1
```

#### Using else clause

```python
# Search with while-else
password_attempts = 0
max_attempts = 3
correct_password = "secret123"

while password_attempts < max_attempts:
    password = input(f"Enter password (Attempt {password_attempts + 1}/{max_attempts}): ")
    password_attempts += 1
    
    if password == correct_password:
        print("🔓 Access granted!")
        break
    else:
        remaining = max_attempts - password_attempts
        if remaining > 0:
            print(f"❌ Incorrect password. {remaining} attempts remaining.")
else:
    print("🔒 Access denied! Maximum attempts exceeded.")
```

## 3. Common Errors and How to Avoid Them

### Syntax Errors

#### Error 1: Missing Colon

```python
# ❌ Incorrect
while count < 10
    print(count)
    count += 1

# ✅ Correct
while count < 10:
    print(count)
    count += 1
```

#### Error 2: Incorrect Indentation

```python
# ❌ Incorrect
while count < 5:
print(count)  # Missing indentation
count += 1    # Missing indentation

# ✅ Correct
while count < 5:
    print(count)  # Properly indented
    count += 1    # Properly indented
```

### Logic Errors

#### Error 3: Infinite Loop (Most Common)

```python
# ❌ Incorrect - Infinite loop
count = 0
while count < 10:
    print(count)
    # Missing increment! count never changes

# ✅ Correct - Proper increment
count = 0
while count < 10:
    print(count)
    count += 1  # Essential update

# ❌ Another infinite loop example
while True:
    print("This will run forever!")
    # No break statement or condition change

# ✅ Correct - Proper exit condition
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
```

#### Error 4: Off-by-One Errors

```python
# ❌ Incorrect - Misses last iteration
count = 1
while count < 10:  # Should be <= 10 to include 10
    print(count)
    count += 1
# Prints 1-9, misses 10

# ✅ Correct
count = 1
while count <= 10:  # Includes 10
    print(count)
    count += 1
# Prints 1-10
```

#### Error 5: Wrong Condition Logic

```python
# ❌ Incorrect - Condition never becomes False
password = ""
while password == "correct":  # Wrong logic
    password = input("Enter password: ")
    if password == "correct":
        print("Access granted!")

# ✅ Correct - Proper condition
password = ""
while password != "correct":
    password = input("Enter password: ")
    if password == "correct":
        print("Access granted!")
```

#### Error 6: Modifying Loop Variable Incorrectly

```python
# ❌ Incorrect - Unexpected behavior
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers.remove(numbers[i])  # Changes list size during iteration
    i += 1  # May skip elements

# ✅ Correct - Iterate backwards or use different approach
numbers = [1, 2, 3, 4, 5]
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 == 0:
        numbers.pop(i)
    i -= 1
```

### Best Practices to Avoid Errors

1. **Always update loop variables** that affect the condition
2. **Initialize variables properly** before the loop
3. **Use meaningful variable names** for loop counters and conditions
4. **Add safety checks** to prevent infinite loops (maximum iteration counters)
5. **Choose the right loop type** - while for unknown iterations, for for known iterations
6. **Test edge cases** - empty inputs, boundary values
7. **Use break and continue wisely** to control loop flow
8. **Consider using flags** for complex termination conditions

#### Example of Good Practice

```python
def safe_input_processing():
    """
    Demonstrates best practices for while loop usage.
    """
    max_attempts = 5
    attempt_count = 0
    valid_input = False
    result = None
    
    print("Enter a number between 1 and 100:")
    
    while not valid_input and attempt_count < max_attempts:
        try:
            user_input = input(f"Attempt {attempt_count + 1}/{max_attempts}: ")
            
            # Check for exit condition
            if user_input.lower() in ['quit', 'exit']:
                print("Operation cancelled by user.")
                break
            
            # Convert and validate input
            number = float(user_input)
            
            if 1 <= number <= 100:
                result = number
                valid_input = True
                print(f"✅ Valid input received: {result}")
            else:
                print("❌ Number must be between 1 and 100")
                
        except ValueError:
            print("❌ Please enter a valid number")
        
        attempt_count += 1
        
        # Provide feedback on remaining attempts
        if not valid_input and attempt_count < max_attempts:
            remaining = max_attempts - attempt_count
            print(f"You have {remaining} attempts remaining.")
    
    else:  # while-else: executes if loop wasn't broken
        if not valid_input:
            print("❌ Maximum attempts exceeded. Operation failed.")
    
    return result

# Example usage
result = safe_input_processing()
if result is not None:
    print(f"Processing number: {result}")
```

### Debugging While Loops

#### Common Debugging Techniques

```python
# Add debug prints to track loop progress
count = 0
max_iterations = 1000  # Safety net

while count < 10 and max_iterations > 0:
    print(f"DEBUG: count = {count}, max_iterations = {max_iterations}")
    
    # Your loop logic here
    count += 1
    max_iterations -= 1  # Safety counter
    
    if max_iterations == 0:
        print("WARNING: Maximum iterations reached - possible infinite loop!")
        break
```
