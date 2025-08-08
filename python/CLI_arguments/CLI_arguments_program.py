#!/usr/bin/env python3
"""
Enhanced CLI Arguments Program
Demonstrates various CLI argument processing techniques based on documentation.

This program showcases:
1. Basic argument processing with sys.argv
2. Input validation and error handling
3. Multiple operation modes (greet, calculate, file operations, config)
4. Proper usage messages and help
5. Type conversion with validation
6. File operations with error handling
7. Best practices for CLI argument processing

Usage Examples:
    python CLI_arguments_program.py info
    python CLI_arguments_program.py greet John
    python CLI_arguments_program.py calculate 10 + 5
    python CLI_arguments_program.py file read example.txt
    python CLI_arguments_program.py file write example.txt "Hello World"
    python CLI_arguments_program.py config set name "John Doe"
    python CLI_arguments_program.py config get name
"""

import sys
import os
import json
from typing import List, Optional


def show_basic_info():
    """Display basic information about command line arguments"""
    print("=== Basic CLI Arguments Information ===")
    print(f"Script name: {sys.argv[0]}")
    print(f"Number of arguments: {len(sys.argv)}")
    print(f"All arguments: {sys.argv}")
    
    if len(sys.argv) > 1:
        print("\nArgument details:")
        for i, arg in enumerate(sys.argv):
            print(f"  argv[{i}] = '{arg}'")
    else:
        print("\nNo additional arguments provided")


def show_help():
    """Display comprehensive help information"""
    help_text = """
=== CLI Arguments Program Help ===

USAGE:
    python CLI_arguments_program.py <operation> [arguments...]

OPERATIONS:
    info                           - Show basic argument information
    help                          - Show this help message
    
    greet [name]                  - Greet user (default: "World")
    
    calculate <num1> <op> <num2>  - Perform calculation
        Operations: +, -, *, /
        Example: python CLI_arguments_program.py calculate 10 + 5
    
    file <operation> <filename> [content]
        read <filename>           - Read and display file content
        write <filename> <content> - Write content to file
        info <filename>           - Show file information
        
    config <operation> [key] [value]
        set <key> <value>         - Set configuration value
        get [key]                 - Get configuration value (all if no key)
        delete <key>              - Delete configuration key

EXAMPLES:
    python CLI_arguments_program.py info
    python CLI_arguments_program.py greet Alice
    python CLI_arguments_program.py calculate 15 / 3
    python CLI_arguments_program.py file read data.txt
    python CLI_arguments_program.py file write output.txt "Hello, World!"
    python CLI_arguments_program.py config set username "john_doe"
    python CLI_arguments_program.py config get
"""
    print(help_text)


def greet_operation(args: List[str]):
    """Handle greet operation with optional name parameter"""
    if len(args) < 2:
        name = "World"
    else:
        name = args[1]
    
    print(f"Hello, {name}!")
    
    # Show additional info if more arguments provided
    if len(args) > 2:
        print(f"Additional arguments provided: {args[2:]}")


def calculate_operation(args: List[str]):
    """Handle calculator operations with proper validation"""
    if len(args) < 4:
        print("Error: Calculator requires 3 arguments")
        print("Usage: python CLI_arguments_program.py calculate <num1> <operator> <num2>")
        print("Example: python CLI_arguments_program.py calculate 10 + 5")
        sys.exit(1)
    
    try:
        num1 = float(args[1])
        operator = args[2]
        num2 = float(args[3])
    except ValueError as e:
        print(f"Error: Invalid number format - {e}")
        print("Please ensure both numbers are valid (integers or decimals)")
        sys.exit(1)
    
    # Perform calculation based on operator
    result = None
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed")
            sys.exit(1)
        result = num1 / num2
    else:
        print(f"Error: Unsupported operator '{operator}'")
        print("Supported operators: +, -, *, /")
        sys.exit(1)
    
    # Display result with appropriate formatting
    if result == int(result):
        print(f"Result: {num1} {operator} {num2} = {int(result)}")
    else:
        print(f"Result: {num1} {operator} {num2} = {result:.2f}")


def file_operation(args: List[str]):
    """Handle file operations with comprehensive error handling"""
    if len(args) < 3:
        print("Error: File operation requires at least 2 arguments")
        print("Usage: python CLI_arguments_program.py file <operation> <filename> [content]")
        print("Operations: read, write, info")
        sys.exit(1)
    
    operation = args[1].lower()
    filename = args[2]
    
    if operation == "read":
        try:
            # Check if file exists and is readable
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' does not exist")
                sys.exit(1)
            
            if not os.path.isfile(filename):
                print(f"Error: '{filename}' is not a regular file")
                sys.exit(1)
            
            if not os.access(filename, os.R_OK):
                print(f"Error: No read permission for '{filename}'")
                sys.exit(1)
            
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"Content of '{filename}':")
                print("-" * 40)
                print(content)
                print("-" * 40)
                print(f"File size: {len(content)} characters")
                
        except IOError as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Error: '{filename}' contains non-text data or uses unsupported encoding")
            sys.exit(1)
    
    elif operation == "write":
        if len(args) < 4:
            print("Error: Write operation requires content")
            print("Usage: python CLI_arguments_program.py file write <filename> <content>")
            sys.exit(1)
        
        # Join remaining arguments as content
        content = " ".join(args[3:])
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Successfully wrote {len(content)} characters to '{filename}'")
            
        except IOError as e:
            print(f"Error writing file: {e}")
            sys.exit(1)
    
    elif operation == "info":
        if os.path.exists(filename):
            try:
                stat = os.stat(filename)
                print(f"File Information for '{filename}':")
                print(f"  Size: {stat.st_size} bytes")
                print(f"  Modified: {stat.st_mtime}")
                print(f"  Is file: {os.path.isfile(filename)}")
                print(f"  Is directory: {os.path.isdir(filename)}")
                print(f"  Readable: {os.access(filename, os.R_OK)}")
                print(f"  Writable: {os.access(filename, os.W_OK)}")
                print(f"  Executable: {os.access(filename, os.X_OK)}")
            except OSError as e:
                print(f"Error getting file info: {e}")
                sys.exit(1)
        else:
            print(f"Error: '{filename}' does not exist")
            sys.exit(1)
    
    else:
        print(f"Error: Unknown file operation '{operation}'")
        print("Supported operations: read, write, info")
        sys.exit(1)


def config_operation(args: List[str]):
    """Handle configuration operations with JSON storage"""
    if len(args) < 2:
        print("Error: Config operation requires at least 1 argument")
        print("Usage: python CLI_arguments_program.py config <operation> [key] [value]")
        print("Operations: set, get, delete")
        sys.exit(1)
    
    config_file = "cli_config.json"
    operation = args[1].lower()
    
    # Load existing config or create empty one
    try:
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            config = {}
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading config file: {e}")
        print("Creating new config...")
        config = {}
    
    if operation == "set":
        if len(args) < 4:
            print("Error: Set operation requires key and value")
            print("Usage: python CLI_arguments_program.py config set <key> <value>")
            sys.exit(1)
        
        key = args[2]
        value = " ".join(args[3:])  # Join remaining args as value
        
        config[key] = value
        
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            print(f"Successfully set '{key}' = '{value}'")
        except IOError as e:
            print(f"Error saving config: {e}")
            sys.exit(1)
    
    elif operation == "get":
        if len(args) >= 3:
            # Get specific key
            key = args[2]
            if key in config:
                print(f"'{key}' = '{config[key]}'")
            else:
                print(f"Error: Key '{key}' not found in configuration")
                sys.exit(1)
        else:
            # Get all configuration
            if config:
                print("Current configuration:")
                for key, value in config.items():
                    print(f"  '{key}' = '{value}'")
            else:
                print("Configuration is empty")
    
    elif operation == "delete":
        if len(args) < 3:
            print("Error: Delete operation requires a key")
            print("Usage: python CLI_arguments_program.py config delete <key>")
            sys.exit(1)
        
        key = args[2]
        if key in config:
            del config[key]
            try:
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=2, ensure_ascii=False)
                print(f"Successfully deleted key '{key}'")
            except IOError as e:
                print(f"Error saving config: {e}")
                sys.exit(1)
        else:
            print(f"Error: Key '{key}' not found in configuration")
            sys.exit(1)
    
    else:
        print(f"Error: Unknown config operation '{operation}'")
        print("Supported operations: set, get, delete")
        sys.exit(1)


def main():
    """Main function to handle CLI argument processing"""
    # Check if any arguments provided
    if len(sys.argv) < 2:
        print("Error: No operation specified")
        print("Use 'help' to see available operations")
        print("Example: python CLI_arguments_program.py help")
        sys.exit(1)
    
    operation = sys.argv[1].lower()
    
    # Route to appropriate operation handler
    try:
        if operation == "info":
            show_basic_info()
        elif operation == "help":
            show_help()
        elif operation == "greet":
            greet_operation(sys.argv[1:])
        elif operation == "calculate":
            calculate_operation(sys.argv[1:])
        elif operation == "file":
            file_operation(sys.argv[1:])
        elif operation == "config":
            config_operation(sys.argv[1:])
        else:
            print(f"Error: Unknown operation '{operation}'")
            print("Available operations: info, help, greet, calculate, file, config")
            print("Use 'help' for detailed usage information")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()