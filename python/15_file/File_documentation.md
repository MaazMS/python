# File Handling Documentation

## 1. Files Definition and Characteristics

### Files Definition

Files are persistent storage units where we organize and store data on the computer's disk. In Python, files are objects that provide an interface to read from and write to the underlying storage system.

### Files Characteristics

- **Persistent**: Data remains stored even after program termination
- **Sequential**: Data is typically accessed in order from beginning to end
- **Buffered**: Python uses internal buffers for efficient I/O operations
- **Resource**: Files are system resources that need to be properly managed
- **Typed**: Can handle text files (strings) or binary files (bytes)

### File Object Creation

```python
# Basic syntax
file_object = open(filename, mode, buffering, encoding)

# Common examples
f = open("data.txt", "r")           # Read text file
f = open("data.txt", "w")           # Write text file
f = open("image.jpg", "rb")         # Read binary file
f = open("output.txt", "w", 1024)   # With custom buffer size
```

### File Modes

#### Text File Modes

- **'r'**: Read mode (default) - Opens file for reading
- **'w'**: Write mode - Creates new file or overwrites existing
- **'a'**: Append mode - Adds content to end of existing file
- **'x'**: Exclusive creation - Creates new file, fails if exists

#### Combined Modes

- **'r+'**: Read and write - File must exist
- **'w+'**: Write and read - Creates new file or overwrites
- **'a+'**: Append and read - Creates file if doesn't exist

#### Binary Modes

- **'rb'**: Read binary
- **'wb'**: Write binary
- **'ab'**: Append binary
- **'rb+'**: Read and write binary

### File Mode Examples

```python
# Read mode example
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# Write mode example (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("This will overwrite any existing content")

# Append mode example (adds to existing content)
with open("log.txt", "a") as file:
    file.write("New log entry\n")

# Binary mode example
with open("image.jpg", "rb") as file:
    binary_data = file.read(1024)  # Read first 1024 bytes
```

### Buffer Characteristics

```python
# Default buffering (system decides - usually 4096 or 8192 bytes)
f = open("data.txt", "r")

# Custom buffer size
f = open("data.txt", "r", buffering=1024)

# Line buffering (for text files)
f = open("data.txt", "w", buffering=1)

# Unbuffered (binary files only)
f = open("data.bin", "wb", buffering=0)
```

## 2. Files Operations

### Basic File Operations

#### Opening and Closing Files

```python
# Traditional approach (manual closing required)
file = open("data.txt", "r")
content = file.read()
file.close()  # Must remember to close

# Context manager approach (automatic closing)
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed here
```

#### Reading Operations

```python
# Read entire file
with open("story.txt", "r") as file:
    entire_content = file.read()
    print(f"Full content: {entire_content}")

# Read specific number of characters
with open("story.txt", "r") as file:
    first_100_chars = file.read(100)
    print(f"First 100 characters: {first_100_chars}")

# Read line by line
with open("story.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Read all lines into a list
with open("story.txt", "r") as file:
    all_lines = file.readlines()
    print(f"Total lines: {len(all_lines)}")

# Read one line at a time
with open("story.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(f"First line: {first_line.strip()}")
    print(f"Second line: {second_line.strip()}")
```

#### Writing Operations

```python
# Write string to file (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append to existing file
with open("log.txt", "a") as file:
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Log entry\n")

# Write with formatting
data = {"name": "Alice", "age": 30, "city": "New York"}
with open("user_data.txt", "w") as file:
    for key, value in data.items():
        file.write(f"{key}: {value}\n")
```

#### File Position Operations

```python
# Working with file position
with open("data.txt", "r") as file:
    # Get current position
    position = file.tell()
    print(f"Current position: {position}")
    
    # Read some data
    data = file.read(10)
    print(f"Read: {data}")
    
    # Check new position
    new_position = file.tell()
    print(f"New position: {new_position}")
    
    # Seek to beginning
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")
    
    # Seek to specific position
    file.seek(5)
    remaining_data = file.read()
    print(f"Data from position 5: {remaining_data}")
```

### Advanced File Operations

#### File Copying

```python
# Copy text file
def copy_text_file(source, destination):
    with open(source, "r") as src:
        with open(destination, "w") as dst:
            dst.write(src.read())
    print(f"Copied {source} to {destination}")

# Copy binary file
def copy_binary_file(source, destination):
    with open(source, "rb") as src:
        with open(destination, "wb") as dst:
            while True:
                chunk = src.read(1024)  # Read in 1KB chunks
                if not chunk:
                    break
                dst.write(chunk)
    print(f"Copied binary file {source} to {destination}")
```

#### CSV File Operations

```python
import csv

# Write CSV file
def write_csv_file():
    data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]
    
    with open("people.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print("CSV file created successfully")

# Read CSV file
def read_csv_file():
    with open("people.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row_number, row in enumerate(reader):
            if row_number == 0:
                print(f"Headers: {row}")
            else:
                print(f"Row {row_number}: {row}")
```

#### JSON File Operations

```python
import json

# Write JSON file
def write_json_file():
    data = {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "metadata": {
            "version": "1.0",
            "created": "2024-01-01"
        }
    }
    
    with open("data.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)
    print("JSON file created successfully")

# Read JSON file
def read_json_file():
    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)
        print(f"Users: {data['users']}")
        print(f"Metadata: {data['metadata']}")
```

## 3. Files Methods

### Built-in File Methods

#### Reading Methods

```python
# Demonstrate all reading methods
def demonstrate_reading_methods():
    # Create a sample file first
    with open("sample.txt", "w") as f:
        f.write("Line 1: Hello World\n")
        f.write("Line 2: Python Programming\n")
        f.write("Line 3: File Handling\n")
    
    print("=== read() method ===")
    with open("sample.txt", "r") as file:
        content = file.read()  # Read entire file
        print(f"Entire content:\n{content}")
    
    print("=== read(size) method ===")
    with open("sample.txt", "r") as file:
        partial = file.read(10)  # Read first 10 characters
        print(f"First 10 characters: '{partial}'")
    
    print("=== readline() method ===")
    with open("sample.txt", "r") as file:
        line1 = file.readline()  # Read first line
        line2 = file.readline()  # Read second line
        print(f"First line: {line1.strip()}")
        print(f"Second line: {line2.strip()}")
    
    print("=== readlines() method ===")
    with open("sample.txt", "r") as file:
        all_lines = file.readlines()  # Read all lines into list
        for i, line in enumerate(all_lines):
            print(f"Line {i+1}: {line.strip()}")
```

#### Writing Methods

```python
# Demonstrate writing methods
def demonstrate_writing_methods():
    print("=== write() method ===")
    with open("write_demo.txt", "w") as file:
        bytes_written = file.write("Hello, World!")
        print(f"Bytes written: {bytes_written}")
        
        file.write("\n")  # Add newline
        file.write("Second line")
    
    print("=== writelines() method ===")
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    with open("writelines_demo.txt", "w") as file:
        file.writelines(lines)
    
    # Read back to verify
    with open("writelines_demo.txt", "r") as file:
        content = file.read()
        print(f"Written content:\n{content}")
```

#### File Position Methods

```python
# Demonstrate file position methods
def demonstrate_position_methods():
    # Create a test file
    with open("position_demo.txt", "w") as f:
        f.write("0123456789ABCDEFGHIJ")
    
    print("=== tell() and seek() methods ===")
    with open("position_demo.txt", "r") as file:
        print(f"Initial position: {file.tell()}")
        
        # Read 5 characters
        data = file.read(5)
        print(f"Read: '{data}', Position now: {file.tell()}")
        
        # Seek to position 10
        file.seek(10)
        print(f"After seek(10): {file.tell()}")
        
        # Read from new position
        data = file.read(5)
        print(f"Read: '{data}', Position now: {file.tell()}")
        
        # Seek to beginning
        file.seek(0)
        print(f"After seek(0): {file.tell()}")
```

### OS Module Methods for Files

```python
import os
import shutil

def demonstrate_os_methods():
    print("=== OS Module File Methods ===")
    
    # Create test files
    with open("test1.txt", "w") as f:
        f.write("Content of test1.txt")
    
    # File existence checks
    print(f"test1.txt exists: {os.path.exists('test1.txt')}")
    print(f"test1.txt is file: {os.path.isfile('test1.txt')}")
    
    # File information
    stat_info = os.stat("test1.txt")
    print(f"File size: {stat_info.st_size} bytes")
    
    # File operations
    print("=== File Operations ===")
    
    # Rename file
    os.rename("test1.txt", "renamed_test.txt")
    print("Renamed test1.txt to renamed_test.txt")
    
    # Get file paths
    print(f"Absolute path: {os.path.abspath('renamed_test.txt')}")
    print(f"Base name: {os.path.basename('renamed_test.txt')}")
    
    # Clean up
    os.remove("renamed_test.txt")
```

### Pickle Module Methods

```python
import pickle

def demonstrate_pickle_methods():
    print("=== Pickle Module Methods ===")
    
    # Create sample data
    data = {
        "name": "Alice",
        "age": 30,
        "hobbies": ["reading", "coding", "hiking"],
        "scores": [85, 92, 78, 96]
    }
    
    # Serialize (dump) object to file
    print("Serializing data to file...")
    with open("data.pickle", "wb") as f:
        pickle.dump(data, f)
    
    # Deserialize (load) object from file
    print("Deserializing data from file...")
    with open("data.pickle", "rb") as f:
        loaded_data = pickle.load(f)
    
    print(f"Original data: {data}")
    print(f"Loaded data: {loaded_data}")
    print(f"Data matches: {data == loaded_data}")
    
    # Clean up
    os.remove("data.pickle")
```

## 4. Common Errors in Files

### File Not Found Errors

```python
def demonstrate_file_not_found_errors():
    print("=== File Not Found Errors ===")
    
    # ❌ WRONG: Not handling FileNotFoundError
    def bad_file_reading():
        file = open("nonexistent.txt", "r")  # Will raise FileNotFoundError
        content = file.read()
        file.close()
        return content
    
    # ✅ CORRECT: Handle FileNotFoundError
    def good_file_reading(filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            return None
        except PermissionError:
            print(f"Error: Permission denied to read '{filename}'")
            return None
    
    # Test the correct approach
    content = good_file_reading("nonexistent.txt")
    if content:
        print(f"File content: {content}")
    else:
        print("Failed to read file")
```

### File Closing Errors

```python
def demonstrate_file_closing_errors():
    print("=== File Closing Errors ===")
    
    # ❌ WRONG: Forgetting to close files
    def bad_file_handling():
        file = open("test.txt", "w")
        file.write("Some content")
        # Forgot to close the file!
        return "File written"
    
    # ✅ CORRECT: Using context manager
    def good_file_handling():
        with open("test.txt", "w") as file:
            file.write("Some content")
        # File automatically closed here
        return "File written successfully"
    
    # Test the correct approach
    result = good_file_handling()
    print(result)
    
    # Clean up
    if os.path.exists("test.txt"):
        os.remove("test.txt")
```

### File Mode Errors

```python
def demonstrate_file_mode_errors():
    print("=== File Mode Errors ===")
    
    # Create a test file
    with open("mode_test.txt", "w") as f:
        f.write("Initial content")
    
    # ❌ WRONG: Trying to write to read-only file
    def bad_mode_usage():
        try:
            with open("mode_test.txt", "r") as file:
                file.write("This will fail")  # io.UnsupportedOperation
        except Exception as e:
            print(f"Error: Cannot write to read-only file")
    
    # ✅ CORRECT: Using appropriate modes
    def correct_mode_usage():
        # Read from file
        with open("mode_test.txt", "r") as file:
            content = file.read()
            print(f"Read content: {content}")
        
        # Write to file
        with open("mode_test.txt", "w") as file:
            file.write("New content")
        
        # Append to file
        with open("mode_test.txt", "a") as file:
            file.write("\nAppended content")
    
    bad_mode_usage()
    correct_mode_usage()
    
    # Clean up
    os.remove("mode_test.txt")
```

### Encoding Errors

```python
def demonstrate_encoding_errors():
    print("=== Encoding Errors ===")
    
    # Create a file with special characters
    text_with_unicode = "Hello, 世界! Café naïve résumé"
    
    # ✅ CORRECT: Explicitly specify encoding
    def good_encoding_handling():
        try:
            # Write with UTF-8 encoding
            with open("unicode_test.txt", "w", encoding="utf-8") as f:
                f.write(text_with_unicode)
            
            # Read with UTF-8 encoding
            with open("unicode_test.txt", "r", encoding="utf-8") as f:
                content = f.read()
                return content
        except UnicodeDecodeError as e:
            print(f"Encoding error: {e}")
            return None
    
    # Test encoding handling
    content = good_encoding_handling()
    if content:
        print(f"Content (UTF-8): {content}")
    
    # Clean up
    if os.path.exists("unicode_test.txt"):
        os.remove("unicode_test.txt")
```

### Best Practices Summary

```python
def file_handling_best_practices():
    print("=== File Handling Best Practices ===")
    
    best_practices = [
        "1. Always use context managers (with statement) for file operations",
        "2. Handle exceptions appropriately (FileNotFoundError, PermissionError, etc.)",
        "3. Specify encoding explicitly for text files",
        "4. Use os.path.join() for cross-platform path construction",
        "5. Check if files/directories exist before operations",
        "6. Close files properly to free system resources",
        "7. Use appropriate file modes for your needs",
        "8. Handle large files with buffering or chunked reading",
        "9. Validate file paths and sanitize user input",
        "10. Use pathlib for modern path handling"
    ]
    
    for practice in best_practices:
        print(f"✅ {practice}")
    
    # Example of following best practices
    print("\n=== Best Practice Example ===")
    
    def robust_file_processor(input_file, output_file):
        """Process a file following all best practices."""
        try:
            # Check if input file exists
            if not os.path.exists(input_file):
                raise FileNotFoundError(f"Input file '{input_file}' not found")
            
            # Create output directory if needed
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)
            
            # Process the file
            with open(input_file, "r", encoding="utf-8") as infile:
                with open(output_file, "w", encoding="utf-8") as outfile:
                    line_count = 0
                    for line in infile:
                        # Process each line (example: convert to uppercase)
                        processed_line = line.upper()
                        outfile.write(processed_line)
                        line_count += 1
            
            print(f"Successfully processed {line_count} lines")
            print(f"Output written to: {output_file}")
            return True
            
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return False
        except PermissionError as e:
            print(f"Permission denied: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    # Create a test file and process it
    test_input = "test_input.txt"
    test_output = "test_output.txt"
    
    with open(test_input, "w", encoding="utf-8") as f:
        f.write("hello world\n")
        f.write("python programming\n")
        f.write("file handling\n")
    
    success = robust_file_processor(test_input, test_output)
    
    if success and os.path.exists(test_output):
        with open(test_output, "r", encoding="utf-8") as f:
            result = f.read()
            print(f"Processed content:\n{result}")
    
    # Clean up
    if os.path.exists(test_input):
        os.remove(test_input)
    if os.path.exists(test_output):
        os.remove(test_output)
```
