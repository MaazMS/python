#!/usr/bin/env python3
"""
File Handling Program
Based on File_documentation.md

This program demonstrates all aspects of Python file handling:
1. File definitions and characteristics with various modes
2. File operations (reading, writing, positioning)
3. File methods and advanced techniques
4. Common errors and their solutions
5. Best practices for file handling
"""

import os
import sys
import csv
import json
import pickle
import shutil
from datetime import datetime

def print_section(title):
    """Helper function to print section headers with proper formatting."""
    print(f"\n{'='*70}")
    print(f" {title}")
    print(f"{'='*70}")

def print_example(description):
    """Helper function to print example descriptions."""
    print(f"\n--- {description} ---")

def cleanup_files(*filenames):
    """Helper function to clean up test files."""
    for filename in filenames:
        if os.path.exists(filename):
            if os.path.isdir(filename):
                shutil.rmtree(filename)
            else:
                os.remove(filename)

# =============================================================================
# 1. FILE DEFINITIONS AND CHARACTERISTICS
# =============================================================================

def demonstrate_file_characteristics():
    """Demonstrate file definitions and characteristics."""
    print_section("1. FILE DEFINITIONS AND CHARACTERISTICS")
    
    print_example("File Creation with Different Modes")
    
    # Write mode (creates new file or overwrites existing)
    with open("demo_write.txt", "w") as f:
        f.write("This file was created in write mode.\n")
        f.write("Write mode overwrites existing content.\n")
    print("✓ Created file in write mode")
    
    # Read mode demonstration
    with open("demo_write.txt", "r") as f:
        content = f.read()
        print(f"Read mode content:\n{content}")
    
    # Append mode (adds to existing content)
    with open("demo_write.txt", "a") as f:
        f.write("This line was added in append mode.\n")
        f.write("Append mode preserves existing content.\n")
    print("✓ Added content in append mode")
    
    # Read updated content
    with open("demo_write.txt", "r") as f:
        updated_content = f.read()
        print(f"Updated content after append:\n{updated_content}")
    
    print_example("File Mode Characteristics")
    
    # Demonstrate different file modes
    modes_demo = {
        "r": "Read only (file must exist)",
        "w": "Write only (creates new or overwrites)",
        "a": "Append only (creates if not exists)",
        "r+": "Read and write (file must exist)",
        "w+": "Write and read (creates new or overwrites)",
        "a+": "Append and read (creates if not exists)"
    }
    
    for mode, description in modes_demo.items():
        print(f"Mode '{mode}': {description}")
    
    print_example("Binary vs Text Files")
    
    # Text file example
    text_data = "Hello, World! 🌍\nThis is a text file with Unicode."
    with open("text_demo.txt", "w", encoding="utf-8") as f:
        f.write(text_data)
    print("✓ Created text file with UTF-8 encoding")
    
    # Binary file example
    binary_data = b"This is binary data: \x48\x65\x6c\x6c\x6f"
    with open("binary_demo.bin", "wb") as f:
        f.write(binary_data)
    print("✓ Created binary file")
    
    # Read and compare
    with open("text_demo.txt", "r", encoding="utf-8") as f:
        text_content = f.read()
        print(f"Text file content: {repr(text_content)}")
    
    with open("binary_demo.bin", "rb") as f:
        binary_content = f.read()
        print(f"Binary file content: {binary_content}")
    
    # Clean up demonstration files
    cleanup_files("demo_write.txt", "text_demo.txt", "binary_demo.bin")

# =============================================================================
# 2. FILE OPERATIONS
# =============================================================================

def demonstrate_file_operations():
    """Demonstrate various file operations."""
    print_section("2. FILE OPERATIONS")
    
    print_example("Basic Reading Operations")
    
    # Create a sample file for reading demonstrations
    sample_content = """Line 1: Welcome to file handling
Line 2: This is the second line
Line 3: Python makes file operations easy
Line 4: Always remember to close files properly
Line 5: Context managers are your friend"""
    
    with open("sample_read.txt", "w") as f:
        f.write(sample_content)
    
    # read() - entire file
    print("Reading entire file:")
    with open("sample_read.txt", "r") as f:
        entire_content = f.read()
        print(f"Entire content:\n{entire_content}\n")
    
    # read(size) - specific number of characters
    print("Reading first 20 characters:")
    with open("sample_read.txt", "r") as f:
        partial_content = f.read(20)
        print(f"First 20 chars: '{partial_content}'\n")
    
    # readline() - one line at a time
    print("Reading line by line:")
    with open("sample_read.txt", "r") as f:
        line_num = 1
        while True:
            line = f.readline()
            if not line:  # End of file
                break
            print(f"Line {line_num}: {line.strip()}")
            line_num += 1
    
    # readlines() - all lines into a list
    print("\nReading all lines into a list:")
    with open("sample_read.txt", "r") as f:
        all_lines = f.readlines()
        for i, line in enumerate(all_lines, 1):
            print(f"List item {i}: {line.strip()}")
    
    print_example("Basic Writing Operations")
    
    # write() method
    with open("write_demo.txt", "w") as f:
        bytes_written = f.write("Hello, World!\n")
        print(f"Wrote {bytes_written} characters")
        
        f.write("This is the second line.\n")
        f.write("Third line with some numbers: 12345\n")
    
    # writelines() method
    lines_to_write = [
        "Line from list 1\n",
        "Line from list 2\n",
        "Line from list 3\n"
    ]
    
    with open("writelines_demo.txt", "w") as f:
        f.writelines(lines_to_write)
    
    # Verify written content
    with open("writelines_demo.txt", "r") as f:
        written_content = f.read()
        print(f"Content written with writelines():\n{written_content}")
    
    print_example("File Position Operations")
    
    # Create a file with known content for position testing
    position_content = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open("position_demo.txt", "w") as f:
        f.write(position_content)
    
    with open("position_demo.txt", "r") as f:
        print(f"Initial position: {f.tell()}")
        
        # Read 10 characters
        data = f.read(10)
        print(f"Read: '{data}', Position now: {f.tell()}")
        
        # Seek to position 20
        f.seek(20)
        print(f"After seek(20): position = {f.tell()}")
        
        # Read 5 characters from position 20
        data = f.read(5)
        print(f"Read from pos 20: '{data}', Position now: {f.tell()}")
        
        # Seek back to beginning
        f.seek(0)
        print(f"After seek(0): position = {f.tell()}")
    
    # Clean up operation files
    cleanup_files("sample_read.txt", "write_demo.txt", "writelines_demo.txt", "position_demo.txt")

# =============================================================================
# 3. ADVANCED FILE OPERATIONS
# =============================================================================

def demonstrate_advanced_operations():
    """Demonstrate advanced file operations."""
    print_section("3. ADVANCED FILE OPERATIONS")
    
    print_example("CSV File Operations")
    
    # Write CSV data
    csv_data = [
        ["Name", "Age", "City", "Salary"],
        ["Alice Johnson", 28, "New York", 75000],
        ["Bob Smith", 32, "Los Angeles", 82000],
        ["Charlie Brown", 25, "Chicago", 68000]
    ]
    
    # Write CSV file
    with open("employees.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)
    print("✓ Created CSV file with employee data")
    
    # Read and display CSV file
    print("Reading CSV file:")
    with open("employees.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row_num, row in enumerate(reader):
            if row_num == 0:
                print(f"Headers: {', '.join(row)}")
            else:
                print(f"Employee {row_num}: {row[0]}, {row[1]} years old, {row[2]}, ${row[3]}")
    
    print_example("JSON File Operations")
    
    # Create JSON data
    json_data = {
        "company": "Tech Solutions Inc.",
        "founded": 2010,
        "employees": [
            {
                "id": 1,
                "name": "Alice Johnson",
                "position": "Software Engineer",
                "skills": ["Python", "JavaScript", "SQL"],
                "salary": 85000
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "position": "Data Scientist",
                "skills": ["Python", "R", "Machine Learning"],
                "salary": 90000
            }
        ]
    }
    
    # Write JSON file
    with open("company_data.json", "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)
    print("✓ Created JSON file with company data")
    
    # Read JSON file
    with open("company_data.json", "r") as jsonfile:
        loaded_data = json.load(jsonfile)
        
    print(f"Company: {loaded_data['company']}")
    print(f"Founded: {loaded_data['founded']}")
    print(f"Number of employees: {len(loaded_data['employees'])}")
    
    for emp in loaded_data['employees']:
        print(f"Employee: {emp['name']}, Position: {emp['position']}")
        print(f"  Skills: {', '.join(emp['skills'])}")
    
    # Clean up advanced operation files
    cleanup_files("employees.csv", "company_data.json")

# =============================================================================
# 4. FILE METHODS AND OS OPERATIONS
# =============================================================================

def demonstrate_file_methods():
    """Demonstrate file methods and OS operations."""
    print_section("4. FILE METHODS AND OS OPERATIONS")
    
    print_example("File Object Methods")
    
    # Create a test file
    test_content = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n"
    with open("methods_demo.txt", "w") as f:
        f.write(test_content)
    
    # Demonstrate various file object methods
    with open("methods_demo.txt", "r") as f:
        print(f"File name: {f.name}")
        print(f"File mode: {f.mode}")
        print(f"Is closed: {f.closed}")
        print(f"Is readable: {f.readable()}")
        print(f"Is writable: {f.writable()}")
        print(f"Is seekable: {f.seekable()}")
        
        if hasattr(f, 'encoding'):
            print(f"File encoding: {f.encoding}")
    
    print(f"After closing - Is closed: {f.closed}")
    
    print_example("OS Module File Operations")
    
    # File existence and information
    test_files = ["methods_demo.txt", "nonexistent.txt"]
    
    for filename in test_files:
        print(f"\nChecking file: {filename}")
        print(f"  Exists: {os.path.exists(filename)}")
        print(f"  Is file: {os.path.isfile(filename)}")
        print(f"  Is directory: {os.path.isdir(filename)}")
        
        if os.path.exists(filename):
            stat_info = os.stat(filename)
            print(f"  Size: {stat_info.st_size} bytes")
            print(f"  Modified: {datetime.fromtimestamp(stat_info.st_mtime)}")
    
    # File operations
    print("\nFile operations:")
    
    # Copy file using shutil
    if os.path.exists("methods_demo.txt"):
        shutil.copy("methods_demo.txt", "methods_copy.txt")
        print("✓ Copied file using shutil.copy()")
    
    # Rename file
    if os.path.exists("methods_copy.txt"):
        os.rename("methods_copy.txt", "methods_renamed.txt")
        print("✓ Renamed file using os.rename()")
    
    # Get file paths
    if os.path.exists("methods_renamed.txt"):
        abs_path = os.path.abspath("methods_renamed.txt")
        base_name = os.path.basename("methods_renamed.txt")
        
        print(f"Absolute path: {abs_path}")
        print(f"Base name: {base_name}")
    
    print_example("Pickle Module Operations")
    
    # Create data structure
    data_to_pickle = {
        "string": "Hello, Pickle!",
        "number": 42,
        "list": [1, 2, 3, 4, 5],
        "nested_dict": {
            "inner_list": ["a", "b", "c"],
            "inner_number": 3.14159
        }
    }
    
    # Serialize to file
    with open("data.pickle", "wb") as f:
        pickle.dump(data_to_pickle, f)
    print("✓ Serialized data to pickle file")
    
    # Deserialize from file
    with open("data.pickle", "rb") as f:
        loaded_data = pickle.load(f)
    
    print("✓ Deserialized data from pickle file")
    print(f"Original data: {data_to_pickle}")
    print(f"Loaded data: {loaded_data}")
    print(f"Data integrity: {data_to_pickle == loaded_data}")
    
    # Clean up methods demonstration files
    cleanup_files("methods_demo.txt", "methods_renamed.txt", "data.pickle")

# =============================================================================
# 5. COMMON ERRORS AND SOLUTIONS
# =============================================================================

def demonstrate_error_handling():
    """Demonstrate common file errors and their solutions."""
    print_section("5. COMMON ERRORS AND SOLUTIONS")
    
    print_example("FileNotFoundError Handling")
    
    # Good approach (specific error handling)
    def good_file_reading(filename):
        """Example of proper error handling."""
        try:
            with open(filename, "r") as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"✗ Error: File '{filename}' not found")
            return None
        except PermissionError:
            print(f"✗ Error: Permission denied to read '{filename}'")
            return None
        except IsADirectoryError:
            print(f"✗ Error: '{filename}' is a directory, not a file")
            return None
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            return None
    
    # Test error handling
    test_files = ["nonexistent.txt", ".", "existing_file.txt"]
    
    # Create one existing file for testing
    with open("existing_file.txt", "w") as f:
        f.write("This file exists for testing.")
    
    for filename in test_files:
        print(f"\nTesting file: {filename}")
        result = good_file_reading(filename)
        if result:
            print(f"✓ Successfully read: {result[:50]}...")
        else:
            print("✗ Failed to read file")
    
    print_example("File Mode Errors")
    
    # Create test file
    with open("mode_test.txt", "w") as f:
        f.write("Initial content")
    
    # Error: Writing to read-only file
    try:
        with open("mode_test.txt", "r") as f:
            f.write("This will fail")
    except Exception as e:
        print(f"✗ Cannot write to read-only file: {type(e).__name__}")
    
    # Correct approach: Use appropriate modes
    print("✓ Correct approach:")
    
    # Read file
    with open("mode_test.txt", "r") as f:
        content = f.read()
        print(f"  Read content: {content}")
    
    # Write to file (overwrites)
    with open("mode_test.txt", "w") as f:
        f.write("New content")
        print("  ✓ Wrote new content")
    
    # Append to file
    with open("mode_test.txt", "a") as f:
        f.write(" - Appended text")
        print("  ✓ Appended content")
    
    print_example("Encoding Handling")
    
    # Text with Unicode characters
    unicode_text = "Hello, 世界! Café naïve résumé 🌍"
    
    print("Testing encoding handling:")
    
    # Good approach: Specify encoding explicitly
    try:
        with open("unicode_test.txt", "w", encoding="utf-8") as f:
            f.write(unicode_text)
        print("✓ Successfully wrote Unicode text with UTF-8 encoding")
        
        with open("unicode_test.txt", "r", encoding="utf-8") as f:
            read_text = f.read()
        print(f"✓ Successfully read Unicode text: {read_text}")
        
    except UnicodeError as e:
        print(f"✗ Encoding error: {e}")
    
    # Clean up error demonstration files
    cleanup_files("existing_file.txt", "mode_test.txt", "unicode_test.txt")

# =============================================================================
# 6. BEST PRACTICES DEMONSTRATION
# =============================================================================

def demonstrate_best_practices():
    """Demonstrate file handling best practices."""
    print_section("6. BEST PRACTICES DEMONSTRATION")
    
    print_example("Professional File Processor")
    
    def safe_file_processor(input_file, output_file, transform_func=None):
        """Process a file following best practices."""
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
                        # Apply transformation if provided
                        if transform_func:
                            line = transform_func(line)
                        
                        outfile.write(line)
                        line_count += 1
            
            print(f"✓ Successfully processed {line_count} lines")
            print(f"✓ Output written to: {output_file}")
            return True
            
        except FileNotFoundError as e:
            print(f"✗ File not found: {e}")
            return False
        except PermissionError as e:
            print(f"✗ Permission denied: {e}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            return False
    
    # Create a test file and process it
    test_input = "test_input.txt"
    test_output = "test_output.txt"
    
    with open(test_input, "w", encoding="utf-8") as f:
        f.write("hello world\n")
        f.write("python programming\n")
        f.write("file handling\n")
    
    # Process with uppercase transformation
    def uppercase_transform(line):
        return line.upper()
    
    success = safe_file_processor(test_input, test_output, uppercase_transform)
    
    if success and os.path.exists(test_output):
        with open(test_output, "r", encoding="utf-8") as f:
            result = f.read()
            print(f"Processed content:\n{result}")
    
    print_example("Best Practices Summary")
    
    best_practices = [
        "1. Always use context managers (with statement)",
        "2. Handle specific exceptions appropriately",
        "3. Specify encoding explicitly for text files",
        "4. Validate file paths for security",
        "5. Create directories as needed",
        "6. Use appropriate file modes",
        "7. Clean up temporary files",
        "8. Process large files in chunks when needed"
    ]
    
    print("\n✅ File Handling Best Practices:")
    for practice in best_practices:
        print(f"   {practice}")
    
    # Clean up demonstration files
    cleanup_files(test_input, test_output)

# =============================================================================
# MAIN EXECUTION FUNCTION
# =============================================================================

def main():
    """
    Main function to execute all file handling demonstrations.
    
    This function runs through all file handling examples in a logical
    progression from basic concepts to advanced techniques and best practices.
    """
    print("🐍 FILE HANDLING COMPREHENSIVE EXAMPLES")
    print("=" * 70)
    print("This program demonstrates all aspects of Python file handling")
    print("based on the comprehensive File_documentation.md")
    
    try:
        # Execute all demonstration functions
        demonstrate_file_characteristics()
        demonstrate_file_operations()
        demonstrate_advanced_operations()
        demonstrate_file_methods()
        demonstrate_error_handling()
        demonstrate_best_practices()
        
        # Final success message
        print(f"\n{'='*70}")
        print("🎉 ALL FILE HANDLING EXAMPLES COMPLETED SUCCESSFULLY!")
        print("📚 Check the documentation for detailed explanations.")
        print("💡 Remember: Always use context managers for file operations!")
        print("🔒 Handle exceptions appropriately and validate file paths!")
        print("📝 Specify encoding explicitly for text files!")
        print(f"{'='*70}")
        
    except KeyboardInterrupt:
        print(f"\n\n⚠️  Program interrupted by user")
        print("Cleaning up any remaining files...")
    except Exception as e:
        print(f"\n❌ Unexpected error occurred: {e}")
        print("Please check your Python installation and file permissions.")
        import traceback
        print("\nError details:")
        traceback.print_exc()

# Execute the program when run directly
if __name__ == "__main__":
    main()
