"""
Input and Output Operations in Python - Comprehensive Examples
Based on input_output_documentation.md

This program demonstrates:
1. Basic input and output operations
2. String formatting techniques
3. Multiple input handling
4. Input validation and processing
5. Advanced I/O methods
6. Interactive menu systems
7. Error handling and best practices
8. Real-world practical applications
"""

import sys
import time
from io import StringIO
import pprint

print("=" * 60)
print("INPUT AND OUTPUT IN PYTHON - COMPREHENSIVE EXAMPLES")
print("=" * 60)

# ============================================================================
# 1. BASIC OUTPUT OPERATIONS
# ============================================================================
print("\n1. BASIC OUTPUT OPERATIONS")
print("-" * 40)

# Simple print statements
print("1.1 Simple Print Statements:")
print("Hello, World!")
print("Python", "Programming")
print(42)
print(3.14159)

# Multiple values with default separator (space)
name = "Alice"
age = 25
print(f"\n1.2 Multiple Values:")
print("Name:", name, "Age:", age)

# Custom separator and ending
print(f"\n1.3 Custom Separators and Endings:")
print("apple", "banana", "cherry", sep=", ")
print("2024", "12", "25", sep="-")

# Custom ending (no newline)
print("Loading", end="")
for i in range(3):
    print(".", end="")
    time.sleep(0.2)
print(" Done!")

# Print to different outputs
print(f"\n1.4 Print to Different Streams:")
print("This goes to stdout", file=sys.stdout)
print("This goes to stderr", file=sys.stderr)

# ============================================================================
# 2. STRING FORMATTING TECHNIQUES
# ============================================================================
print("\n2. STRING FORMATTING TECHNIQUES")
print("-" * 40)

name = "Bob"
score = 87.5
attempts = 3

print("2.1 Different Formatting Methods:")

# Old-style % formatting
print("% formatting:", "Student: %s, Score: %.1f%%" % (name, score))

# .format() method
print(".format() method:", "Student: {}, Score: {:.1f}%".format(name, score))
print("Named .format():", "Student: {name}, Score: {score:.1f}%".format(name=name, score=score))

# f-strings (Python 3.6+) - Recommended
print("f-strings:", f"Student: {name}, Score: {score:.1f}%")
print("Zero-padded:", f"Attempts: {attempts:02d}")

# Advanced f-string formatting
from datetime import datetime
now = datetime.now()
print("Date formatting:", f"Current time: {now:%Y-%m-%d %H:%M:%S}")

# Expressions in f-strings
numbers = [1, 2, 3, 4, 5]
print("Expressions:", f"Sum: {sum(numbers)}, Average: {sum(numbers)/len(numbers):.2f}")

# ============================================================================
# 3. BASIC INPUT OPERATIONS
# ============================================================================
print("\n3. BASIC INPUT OPERATIONS")
print("-" * 40)

def demonstrate_basic_input():
    """Demonstrate basic input operations"""
    print("3.1 Basic Input Demonstration:")
    
    # Simple string input
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # Numeric input with validation
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Height must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Summary: {name} is {age} years old and {height}m tall")

# Uncomment to run interactive demo
# demonstrate_basic_input()

# ============================================================================
# 4. MULTIPLE INPUT HANDLING
# ============================================================================
print("\n4. MULTIPLE INPUT HANDLING")
print("-" * 40)

def demonstrate_multiple_input():
    """Demonstrate multiple input handling techniques"""
    print("4.1 Multiple Input Techniques:")
    
    # Space-separated input
    print("Enter 3 words separated by spaces:")
    words = input().split()
    print(f"You entered {len(words)} words: {words}")
    
    # Comma-separated input
    print("Enter numbers separated by commas:")
    try:
        numbers_str = input().split(',')
        numbers = [int(x.strip()) for x in numbers_str if x.strip()]
        print(f"Numbers: {numbers}")
        if numbers:
            print(f"Sum: {sum(numbers)}, Average: {sum(numbers)/len(numbers):.2f}")
    except ValueError:
        print("Please enter valid numbers!")
    
    # Multiple inputs with unpacking
    print("Enter your first and last name separated by space:")
    try:
        first_name, last_name = input().split()
        print(f"Full name: {first_name} {last_name}")
    except ValueError:
        print("Please enter exactly two names!")
    
    # Multiple numeric inputs
    print("Enter three numbers separated by spaces:")
    try:
        a, b, c = map(int, input().split())
        print(f"Numbers: {a}, {b}, {c}")
        print(f"Sum: {a + b + c}, Average: {(a + b + c) / 3:.2f}")
    except ValueError:
        print("Please enter exactly three valid numbers!")

# Uncomment to run interactive demo
# demonstrate_multiple_input()

# ============================================================================
# 5. INPUT VALIDATION AND PROCESSING
# ============================================================================
print("\n5. INPUT VALIDATION AND PROCESSING")
print("-" * 40)

def get_integer_input(prompt, min_val=None, max_val=None):
    """Get integer input with validation"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")

def get_choice_input(prompt, choices):
    """Get input from a list of valid choices"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in [c.lower() for c in choices]:
            return choice
        print(f"Please choose from: {', '.join(choices)}")

def get_email_input():
    """Get valid email input"""
    while True:
        email = input("Enter your email: ").strip()
        
        # Check for empty input
        if not email:
            print("Email cannot be empty!")
            continue
        
        # Basic email validation
        if '@' not in email:
            print("Email must contain @ symbol!")
            continue
        
        if email.count('@') != 1:
            print("Email must contain exactly one @ symbol!")
            continue
        
        local, domain = email.split('@')
        
        if not local or not domain:
            print("Invalid email format!")
            continue
        
        if '.' not in domain:
            print("Domain must contain a dot!")
            continue
        
        return email

def demonstrate_validation():
    """Demonstrate input validation techniques"""
    print("5.1 Input Validation Examples:")
    
    # Demonstrate validation functions
    age = get_integer_input("Enter your age (0-120): ", 0, 120)
    color = get_choice_input("Choose a color (red/green/blue): ", ['red', 'green', 'blue'])
    email = get_email_input()
    
    print(f"\nValidation Results:")
    print(f"Age: {age}")
    print(f"Color: {color}")
    print(f"Email: {email}")

# Uncomment to run interactive demo
# demonstrate_validation()

# ============================================================================
# 6. ADVANCED I/O METHODS
# ============================================================================
print("\n6. ADVANCED I/O METHODS")
print("-" * 40)

print("6.1 Advanced Print Methods:")

# Print with unpacking
data = ["apple", "banana", "cherry"]
print("Fruits:", *data)
print("Fruits with custom separator:", *data, sep=" | ", end=" (end of list)\n")

# Printing to string using StringIO
output = StringIO()
print("Hello", "World", file=output)
result = output.getvalue()
print(f"Captured output: '{result.strip()}'")

# Pretty printing for complex data
print("\n6.2 Pretty Printing:")
complex_data = {
    'users': [
        {'name': 'Alice', 'age': 25, 'skills': ['Python', 'JavaScript']},
        {'name': 'Bob', 'age': 30, 'skills': ['Java', 'C++', 'Python']}
    ],
    'settings': {'debug': True, 'version': '1.0.0'}
}

print("Regular print:")
print(complex_data)

print("\nPretty print:")
pprint.pprint(complex_data)

# ============================================================================
# 7. INTERACTIVE MENU SYSTEM
# ============================================================================
print("\n7. INTERACTIVE MENU SYSTEM")
print("-" * 40)

def display_menu(title, options):
    """Display a numbered menu"""
    print("\n" + "="*40)
    print(title.center(40))
    print("="*40)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("0. Exit")
    print("="*40)

def get_menu_choice(max_option):
    """Get valid menu choice"""
    while True:
        try:
            choice = int(input(f"Enter choice (0-{max_option}): "))
            if 0 <= choice <= max_option:
                return choice
            else:
                print(f"Please enter a number between 0 and {max_option}")
        except ValueError:
            print("Please enter a valid number")

def calculator_demo():
    """Interactive calculator demonstration"""
    operations = ["Add", "Subtract", "Multiply", "Divide"]
    
    print("7.1 Interactive Calculator Demo")
    
    # Simulate one calculation for demo
    display_menu("CALCULATOR", operations)
    print("Demo: Selecting option 1 (Add)")
    
    try:
        a = 10.5
        b = 5.2
        print(f"Demo inputs: {a} and {b}")
        result = a + b
        print(f"Result: {a} + {b} = {result}")
    except Exception as e:
        print(f"Error: {e}")

calculator_demo()

# ============================================================================
# 8. ERROR HANDLING EXAMPLES
# ============================================================================
print("\n8. ERROR HANDLING EXAMPLES")
print("-" * 40)

print("8.1 Input Type Conversion Errors:")

def safe_integer_input(prompt):
    """Safely get integer input with error handling"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid integer!")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            return None

# Demo with predefined values
print("Demo: Safe integer input function created")

print("\n8.2 String Formatting Error Handling:")

def safe_format_demo():
    """Demonstrate safe string formatting"""
    name = "Alice"
    age = 25
    
    # Show potential formatting errors
    try:
        # This would cause an error with wrong number of arguments
        # result = "Name: %s, Age: %s, Score: %s" % (name, age)
        print("Avoided formatting error by using correct number of arguments")
    except TypeError as e:
        print(f"Formatting error caught: {e}")
    
    # Correct formatting approaches
    result1 = "Name: %s, Age: %d" % (name, age)
    result2 = f"Name: {name}, Age: {age}"
    
    print(f"Safe % formatting: {result1}")
    print(f"Safe f-string formatting: {result2}")

safe_format_demo()

print("\n8.3 Input Processing Error Handling:")

def process_names_safely(input_string):
    """Safely process comma-separated names"""
    if not input_string or not input_string.strip():
        return []
    
    names = [name.strip() for name in input_string.split(',')]
    names = [name for name in names if name]  # Remove empty strings
    return names

# Test with various inputs
test_inputs = [
    "Alice, Bob, Charlie",
    "Alice,,Bob,Charlie",  # Empty values
    "",                    # Empty string
    "   ",                # Whitespace only
]

print("Name processing examples:")
for test_input in test_inputs:
    result = process_names_safely(test_input)
    print(f"Input: '{test_input}' -> Output: {result}")

print("\n8.4 Progress Display with Proper Flushing:")

def show_progress():
    """Show progress with proper output flushing"""
    print("Processing", end="", flush=True)
    for i in range(5):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print(" Done!")

show_progress()

# ============================================================================
# 9. PRACTICAL REAL-WORLD APPLICATIONS
# ============================================================================
print("\n9. PRACTICAL REAL-WORLD APPLICATIONS")
print("-" * 40)

print("9.1 User Registration System:")

class UserRegistration:
    """Simple user registration system with validation"""
    
    def __init__(self):
        self.users = []
    
    def validate_user_data(self, name, email, age):
        """Validate user registration data"""
        errors = []
        
        # Name validation
        if not name or len(name.strip()) < 2:
            errors.append("Name must be at least 2 characters long")
        
        # Email validation
        if not email or '@' not in email or email.count('@') != 1:
            errors.append("Invalid email format")
        
        # Age validation
        if not isinstance(age, int) or age < 13 or age > 120:
            errors.append("Age must be between 13 and 120")
        
        return errors
    
    def register_user_demo(self):
        """Demo user registration with sample data"""
        sample_users = [
            ("Alice Smith", "alice@email.com", 25),
            ("", "bob@email.com", 30),  # Invalid name
            ("Charlie", "invalid-email", 25),  # Invalid email
            ("Diana", "diana@email.com", 12),  # Invalid age
        ]
        
        print("User Registration Demo:")
        for name, email, age in sample_users:
            print(f"\nTesting: Name='{name}', Email='{email}', Age={age}")
            errors = self.validate_user_data(name, email, age)
            
            if errors:
                print("Registration failed:")
                for error in errors:
                    print(f"  - {error}")
            else:
                self.users.append({"name": name, "email": email, "age": age})
                print("Registration successful!")
        
        print(f"\nTotal registered users: {len(self.users)}")
        for user in self.users:
            print(f"  - {user['name']} ({user['email']})")

# Run registration demo
registration_system = UserRegistration()
registration_system.register_user_demo()

print("\n9.2 Data Collection and Analysis:")

def analyze_survey_data():
    """Analyze sample survey data"""
    # Sample survey responses
    responses = [
        {"age": 25, "satisfaction": 4, "recommend": True},
        {"age": 30, "satisfaction": 5, "recommend": True},
        {"age": 22, "satisfaction": 3, "recommend": False},
        {"age": 35, "satisfaction": 4, "recommend": True},
        {"age": 28, "satisfaction": 5, "recommend": True},
    ]
    
    print("Survey Data Analysis:")
    print(f"Total responses: {len(responses)}")
    
    # Calculate averages
    avg_age = sum(r["age"] for r in responses) / len(responses)
    avg_satisfaction = sum(r["satisfaction"] for r in responses) / len(responses)
    recommend_rate = sum(1 for r in responses if r["recommend"]) / len(responses) * 100
    
    print(f"Average age: {avg_age:.1f}")
    print(f"Average satisfaction: {avg_satisfaction:.1f}/5")
    print(f"Recommendation rate: {recommend_rate:.1f}%")
    
    # Display formatted results
    print("\nDetailed Results:")
    print("Age | Satisfaction | Recommend")
    print("-" * 30)
    for response in responses:
        recommend_text = "Yes" if response["recommend"] else "No"
        print(f"{response['age']:3d} | {response['satisfaction']:12d} | {recommend_text}")

analyze_survey_data()

print("\n9.3 Configuration Management:")

def manage_configuration():
    """Demonstrate configuration management"""
    default_config = {
        'debug': False,
        'timeout': 30,
        'retries': 3,
        'host': 'localhost',
        'port': 8080
    }
    
    user_overrides = {
        'debug': True,
        'timeout': 60,
        'port': 9000
    }
    
    # Merge configurations
    final_config = default_config.copy()
    final_config.update(user_overrides)
    
    print("Configuration Management Demo:")
    print("Default configuration:")
    for key, value in default_config.items():
        print(f"  {key}: {value}")
    
    print("\nUser overrides:")
    for key, value in user_overrides.items():
        print(f"  {key}: {value}")
    
    print("\nFinal configuration:")
    for key, value in final_config.items():
        print(f"  {key}: {value}")

manage_configuration()

print("\n9.4 Report Generation:")

def generate_report():
    """Generate a formatted report"""
    data = {
        'title': 'Monthly Sales Report',
        'period': 'December 2024',
        'sales': [
            {'product': 'Laptops', 'quantity': 45, 'revenue': 67500},
            {'product': 'Phones', 'quantity': 120, 'revenue': 48000},
            {'product': 'Tablets', 'quantity': 30, 'revenue': 15000},
        ]
    }
    
    print("Report Generation Demo:")
    print("=" * 50)
    print(f"{data['title']}".center(50))
    print(f"Period: {data['period']}".center(50))
    print("=" * 50)
    
    print(f"{'Product':<15} {'Quantity':<10} {'Revenue':<15}")
    print("-" * 40)
    
    total_quantity = 0
    total_revenue = 0
    
    for item in data['sales']:
        print(f"{item['product']:<15} {item['quantity']:<10} ${item['revenue']:<14,}")
        total_quantity += item['quantity']
        total_revenue += item['revenue']
    
    print("-" * 40)
    print(f"{'TOTAL':<15} {total_quantity:<10} ${total_revenue:<14,}")
    print("=" * 50)

generate_report()

# ============================================================================
# 10. BEST PRACTICES SUMMARY
# ============================================================================
print("\n10. BEST PRACTICES SUMMARY")
print("-" * 40)

best_practices = [
    "Always validate input - Check for empty strings, invalid types, and range limits",
    "Use try-except blocks for type conversions and file operations",
    "Handle edge cases - Empty input, whitespace, special characters",
    "Provide clear prompts - Tell users exactly what input is expected",
    "Give helpful error messages - Explain what went wrong and how to fix it",
    "Test with various inputs - Include edge cases, invalid data, and boundary values",
    "Use appropriate string formatting - Prefer f-strings for readability and performance",
    "Flush output when needed - For real-time display and progress indicators",
    "Handle encoding issues - Be aware of Unicode and character encoding problems",
    "Sanitize and validate all input - Never trust user input without validation"
]

print("Input/Output Best Practices:")
for i, practice in enumerate(best_practices, 1):
    print(f"{i:2d}. {practice}")

print("\n" + "=" * 60)
print("INPUT/OUTPUT PROGRAM COMPLETED SUCCESSFULLY")
print("All examples demonstrate proper I/O handling techniques!")
print("=" * 60)

# Note: Many interactive functions are defined but not called to avoid
# requiring user input during automated execution. Uncomment the function
# calls to test interactive features manually.
