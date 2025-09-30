# 1. CLI Arguments Definition and Characteristics

## Definition

Command Line Interface (CLI) arguments are parameters passed to a Python script when it's executed from the command line. They allow users to provide input to the program without modifying the source code.

### Key Characteristics

#### 1.1 Stored in sys.argv

```python
import sys

# Example: python script.py arg1 arg2 arg3
print("Script name:", sys.argv[0])
print("All arguments:", sys.argv)
print("Number of arguments:", len(sys.argv))
```

#### 1.2 Always Strings by Default

```python
import sys

# Example: python calculator.py 10 20
if len(sys.argv) >= 3:
    # Arguments are strings by default
    num1 = sys.argv[1]  # "10" (string)
    num2 = sys.argv[2]  # "20" (string)
    
    # Type conversion needed for arithmetic
    result = int(num1) + int(num2)
    print(f"Sum: {result}")
```

#### 1.3 Zero-indexed List

```python
import sys

# Example: python greet.py John 25 Engineer
# sys.argv[0] = "greet.py"
# sys.argv[1] = "John"
# sys.argv[2] = "25"
# sys.argv[3] = "Engineer"

if len(sys.argv) >= 4:
    name = sys.argv[1]
    age = int(sys.argv[2])
    profession = sys.argv[3]
    print(f"Hello {name}, you are {age} years old and work as an {profession}")
```

#### 1.4 Space-separated by Default

```python
import sys

# Handling arguments with spaces
# Example: python script.py "John Doe" "Software Engineer"
if len(sys.argv) >= 3:
    full_name = sys.argv[1]      # "John Doe"
    job_title = sys.argv[2]      # "Software Engineer"
    print(f"Name: {full_name}, Job: {job_title}")
```

---

## 2. CLI Arguments Operations

### 2.1 Basic Argument Processing

```python
import sys

def process_basic_args():
    """Basic argument processing example"""
    if len(sys.argv) < 2:
        print("Usage: python script.py <operation> [arguments...]")
        return
    
    operation = sys.argv[1].lower()
    
    if operation == "greet":
        name = sys.argv[2] if len(sys.argv) > 2 else "World"
        print(f"Hello, {name}!")
    
    elif operation == "calculate":
        if len(sys.argv) >= 5:
            num1 = float(sys.argv[2])
            operator = sys.argv[3]
            num2 = float(sys.argv[4])
            
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid operator"
            
            print(f"Result: {result}")
        else:
            print("Usage: python script.py calculate <num1> <operator> <num2>")

if __name__ == "__main__":
    process_basic_args()
```

### 2.2 File Operations with CLI Arguments

```python
import sys
import os

def file_operations():
    """File operations using CLI arguments"""
    if len(sys.argv) < 3:
        print("Usage: python script.py <operation> <filename> [content]")
        return
    
    operation = sys.argv[1].lower()
    filename = sys.argv[2]
    
    if operation == "read":
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"Content of {filename}:")
                print(content)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
    
    elif operation == "write":
        if len(sys.argv) >= 4:
            content = " ".join(sys.argv[3:])  # Join remaining args as content
            with open(filename, 'w') as file:
                file.write(content)
            print(f"Content written to {filename}")
        else:
            print("Usage: python script.py write <filename> <content>")
    
    elif operation == "info":
        if os.path.exists(filename):
            stat = os.stat(filename)
            print(f"File: {filename}")
            print(f"Size: {stat.st_size} bytes")
            print(f"Modified: {stat.st_mtime}")
        else:
            print(f"File '{filename}' does not exist")

if __name__ == "__main__":
    file_operations()
```

### 2.3 Configuration and Settings Operations

```python
import sys
import json

def config_operations():
    """Configuration operations with CLI arguments"""
    if len(sys.argv) < 2:
        print("Usage: python config.py <operation> [key] [value]")
        return
    
    config_file = "config.json"
    operation = sys.argv[1].lower()
    
    # Load existing config or create empty one
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    
    if operation == "set":
        if len(sys.argv) >= 4:
            key = sys.argv[2]
            value = sys.argv[3]
            config[key] = value
            
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"Set {key} = {value}")
        else:
            print("Usage: python config.py set <key> <value>")
    
    elif operation == "get":
        if len(sys.argv) >= 3:
            key = sys.argv[2]
            value = config.get(key, "Key not found")
            print(f"{key} = {value}")
        else:
            print("All configuration:")
            for key, value in config.items():
                print(f"{key} = {value}")
    
    elif operation == "delete":
        if len(sys.argv) >= 3:
            key = sys.argv[2]
            if key in config:
                del config[key]
                with open(config_file, 'w') as f:
                    json.dump(config, f, indent=2)
                print(f"Deleted {key}")
            else:
                print(f"Key '{key}' not found")

if __name__ == "__main__":
    config_operations()
```

---

## 3. CLI Arguments Methods

### 3.1 Using sys.argv (Built-in Method)

```python
import sys

def basic_sys_argv():
    """Basic usage of sys.argv"""
    print("Script name:", sys.argv[0])
    print("Arguments:", sys.argv[1:])
    
    # Example usage: python script.py --name John --age 25
    for i, arg in enumerate(sys.argv):
        print(f"argv[{i}] = {arg}")

# Example with validation
def validated_args():
    """Validated argument processing"""
    if len(sys.argv) != 4:
        print("Error: Expected exactly 3 arguments")
        print("Usage: python script.py <name> <age> <city>")
        sys.exit(1)
    
    name = sys.argv[1]
    try:
        age = int(sys.argv[2])
    except ValueError:
        print("Error: Age must be a number")
        sys.exit(1)
    
    city = sys.argv[3]
    
    print(f"Name: {name}, Age: {age}, City: {city}")

if __name__ == "__main__":
    basic_sys_argv()
```

### 3.2 Using argparse Module (Recommended)

```python
import argparse

def argparse_basic():
    """Basic argparse usage"""
    parser = argparse.ArgumentParser(description="Process user information")
    
    # Positional arguments
    parser.add_argument("name", help="User's name")
    parser.add_argument("age", type=int, help="User's age")
    
    # Optional arguments
    parser.add_argument("--city", "-c", default="Unknown", help="User's city")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    if args.verbose:
        print("Verbose mode enabled")
    
    print(f"Name: {args.name}")
    print(f"Age: {args.age}")
    print(f"City: {args.city}")

def argparse_advanced():
    """Advanced argparse features"""
    parser = argparse.ArgumentParser(
        description="Advanced CLI tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python script.py --input file.txt --output result.txt
  python script.py -i data.csv -o processed.csv --format json
        """
    )
    
    # File arguments
    parser.add_argument("--input", "-i", required=True, help="Input file path")
    parser.add_argument("--output", "-o", default="output.txt", help="Output file path")
    
    # Choice arguments
    parser.add_argument("--format", choices=["json", "csv", "xml"], default="json",
                       help="Output format")
    
    # Multiple values
    parser.add_argument("--columns", nargs="+", help="Columns to process")
    
    # Boolean flags
    parser.add_argument("--compress", action="store_true", help="Compress output")
    parser.add_argument("--no-header", action="store_true", help="Skip header row")
    
    # Count arguments
    parser.add_argument("--verbose", "-v", action="count", default=0,
                       help="Increase verbosity (-v, -vv, -vvv)")
    
    args = parser.parse_args()
    
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"Format: {args.format}")
    print(f"Columns: {args.columns}")
    print(f"Compress: {args.compress}")
    print(f"No header: {args.no_header}")
    print(f"Verbosity level: {args.verbose}")

if __name__ == "__main__":
    argparse_advanced()
```

### 3.3 Using click Module (Third-party)

```python
import click

@click.command()
@click.argument('name')
@click.argument('age', type=int)
@click.option('--city', '-c', default='Unknown', help='User city')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
def greet_user(name, age, city, verbose):
    """Greet a user with their information."""
    if verbose:
        click.echo("Verbose mode enabled")
    
    click.echo(f"Hello {name}!")
    click.echo(f"Age: {age}")
    click.echo(f"City: {city}")

@click.group()
def cli():
    """A CLI tool with multiple commands."""
    pass

@cli.command()
@click.argument('filename')
@click.option('--lines', '-n', default=10, help='Number of lines to display')
def head(filename, lines):
    """Display the first N lines of a file."""
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= lines:
                    break
                click.echo(line.rstrip())
    except FileNotFoundError:
        click.echo(f"Error: File '{filename}' not found", err=True)

@cli.command()
@click.argument('text')
@click.option('--count', '-c', default=1, help='Number of repetitions')
def repeat(text, count):
    """Repeat text N times."""
    for _ in range(count):
        click.echo(text)

if __name__ == "__main__":
    cli()
```

---

## 4. Common Errors in CLI Arguments

### 4.1 Index Out of Range Error

```python
import sys

# WRONG WAY - No error handling
def wrong_way():
    name = sys.argv[1]  # IndexError if no arguments provided
    age = int(sys.argv[2])  # IndexError if less than 2 arguments
    print(f"Name: {name}, Age: {age}")

# CORRECT WAY - With error handling
def correct_way():
    if len(sys.argv) < 3:
        print("Error: Please provide name and age")
        print("Usage: python script.py <name> <age>")
        sys.exit(1)
    
    try:
        name = sys.argv[1]
        age = int(sys.argv[2])
        print(f"Name: {name}, Age: {age}")
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

# BEST WAY - Using argparse
import argparse

def best_way():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Person's name")
    parser.add_argument("age", type=int, help="Person's age")
    
    args = parser.parse_args()  # Automatically handles errors and shows help
    print(f"Name: {args.name}, Age: {args.age}")
```

### 4.2 Type Conversion Errors

```python
import sys

# WRONG WAY - No type validation
def wrong_type_handling():
    number = int(sys.argv[1])  # ValueError if not a number
    result = number * 2
    print(result)

# CORRECT WAY - With type validation
def correct_type_handling():
    if len(sys.argv) < 2:
        print("Error: Please provide a number")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        result = number * 2
        print(f"Result: {result}")
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid integer")
        sys.exit(1)

# ADVANCED - Multiple type handling
def advanced_type_handling():
    if len(sys.argv) < 2:
        print("Error: Please provide a number")
        sys.exit(1)
    
    value = sys.argv[1]
    
    # Try different number types
    try:
        # Try integer first
        if '.' not in value:
            number = int(value)
        else:
            number = float(value)
        
        result = number * 2
        print(f"Result: {result}")
    
    except ValueError:
        print(f"Error: '{value}' is not a valid number")
        sys.exit(1)
```

### 4.3 File Path and Permission Errors

```python
import sys
import os

# WRONG WAY - No file validation
def wrong_file_handling():
    filename = sys.argv[1]
    with open(filename, 'r') as f:  # FileNotFoundError, PermissionError possible
        content = f.read()
    print(content)

# CORRECT WAY - With comprehensive file handling
def correct_file_handling():
    if len(sys.argv) < 2:
        print("Error: Please provide a filename")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist")
        sys.exit(1)
    
    # Check if it's a file (not directory)
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a regular file")
        sys.exit(1)
    
    # Check read permissions
    if not os.access(filename, os.R_OK):
        print(f"Error: No read permission for '{filename}'")
        sys.exit(1)
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(content)
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
```

### 4.4 Argument Validation Errors

```python
import sys
import re

# WRONG WAY - No validation
def wrong_validation():
    email = sys.argv[1]
    port = int(sys.argv[2])
    # No validation - could be invalid email or port

# CORRECT WAY - With proper validation
def correct_validation():
    if len(sys.argv) < 3:
        print("Usage: python script.py <email> <port>")
        sys.exit(1)
    
    email = sys.argv[1]
    
    # Validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        print(f"Error: '{email}' is not a valid email address")
        sys.exit(1)
    
    # Validate and convert port
    try:
        port = int(sys.argv[2])
        if not (1 <= port <= 65535):
            raise ValueError("Port must be between 1 and 65535")
    except ValueError as e:
        print(f"Error: Invalid port - {e}")
        sys.exit(1)
    
    print(f"Email: {email}, Port: {port}")
```

### 4.5 Common Error Patterns and Solutions

#### Pattern 1: Silent Failures

```python
import sys

# WRONG - Silent failure
def silent_failure():
    if len(sys.argv) > 1:
        process_data(sys.argv[1])
    # Silently does nothing if no arguments

# CORRECT - Explicit error handling
def explicit_handling():
    if len(sys.argv) < 2:
        print("Error: Missing required argument", file=sys.stderr)
        print("Usage: python script.py <data>", file=sys.stderr)
        sys.exit(1)
    
    process_data(sys.argv[1])
```

#### Pattern 2: Poor Error Messages

```python
import sys

# WRONG - Vague error message
def vague_error():
    try:
        value = int(sys.argv[1])
    except:
        print("Error occurred")  # Not helpful

# CORRECT - Specific error messages
def specific_error():
    if len(sys.argv) < 2:
        print("Error: No argument provided")
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    try:
        value = int(sys.argv[1])
        print(f"Processing value: {value}")
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid integer")
        print("Please provide a whole number (e.g., 42, -17, 0)")
        sys.exit(1)
```

#### Pattern 3: No Usage Information

```python
import sys

# WRONG - No help for users
def no_help():
    if len(sys.argv) != 4:
        print("Wrong number of arguments")
        sys.exit(1)

# CORRECT - Clear usage information
def clear_usage():
    if len(sys.argv) != 4:
        print("Error: Expected exactly 3 arguments")
        print()
        print("Usage: python calculator.py <num1> <operator> <num2>")
        print()
        print("Examples:")
        print("  python calculator.py 10 + 5")
        print("  python calculator.py 20 - 8")
        print("  python calculator.py 6 * 7")
        print("  python calculator.py 15 / 3")
        sys.exit(1)
```

### Error Prevention Best Practices

```python
import sys
import argparse
import logging

def best_practices_example():
    """Example showing CLI argument best practices"""
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Use argparse for robust argument handling
    parser = argparse.ArgumentParser(
        description="Data processing tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python processor.py --input data.txt --format csv
  python processor.py -i data.json -f json --verbose
        """
    )
    
    # Required arguments
    parser.add_argument("--input", "-i", required=True,
                       help="Input file path")
    
    # Optional arguments with defaults
    parser.add_argument("--format", "-f", 
                       choices=["csv", "json", "xml"],
                       default="csv",
                       help="Input format (default: csv)")
    
    parser.add_argument("--output", "-o",
                       help="Output file (default: processed_<input>)")
    
    # Boolean flags
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Enable verbose logging")
    
    # Parse arguments
    try:
        args = parser.parse_args()
    except SystemExit:
        return  # argparse handles help and error messages
    
    # Set logging level based on verbose flag
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled")
    
    # Validate input file
    import os
    if not os.path.exists(args.input):
        logger.error(f"Input file '{args.input}' does not exist")
        sys.exit(1)
    
    # Set default output filename
    if not args.output:
        base_name = os.path.splitext(args.input)[0]
        args.output = f"processed_{base_name}.{args.format}"
    
    logger.info(f"Processing {args.input} -> {args.output}")
    logger.info(f"Format: {args.format}")
    
    # Process the file (placeholder)
    try:
        # Your processing logic here
        logger.info("Processing completed successfully")
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    best_practices_example()
```
