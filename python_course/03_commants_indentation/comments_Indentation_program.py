#!/usr/bin/env python3
"""
Comments and Indentation Program
Based on comments_Indentation_documentation.md

This program demonstrates all aspects of Python comments and indentation:
1. Types of comments and their proper usage
2. Indentation rules and best practices
3. Comment and indentation operations
4. Methods for writing effective comments
5. Common errors and their solutions
6. Best practices for maintainable code
"""

import re
import math

def print_section(title):
    """Helper function to print section headers with proper formatting."""
    print(f"\n{'='*70}")
    print(f" {title}")
    print(f"{'='*70}")

def print_example(description):
    """Helper function to print example descriptions."""
    print(f"\n--- {description} ---")

# =============================================================================
# 1. TYPES OF COMMENTS DEMONSTRATION
# =============================================================================

def demonstrate_comment_types():
    """Demonstrate all four types of comments in Python."""
    print_section("1. TYPES OF COMMENTS")
    
    # 1. Single-line comments demonstration
    print_example("Single-line Comments")
    # This is a single-line comment explaining the next line
    greeting = "Hello, World!"  # This is an inline comment
    print(f"Greeting: {greeting}")
    
    # 2. Multi-line comments demonstration
    print_example("Multi-line Comments")
    # This is a multi-line comment that explains
    # the purpose of the following function
    # Each line starts with a hash symbol
    def calculate_rectangle_area(length, width):
        return length * width
    
    area = calculate_rectangle_area(5, 3)
    print(f"Rectangle area: {area}")
    
    # 3. Docstrings demonstration
    print_example("Docstrings (Documentation Strings)")
    
    def calculate_circle_area(radius):
        """
        Calculate the area of a circle using the formula π * r².
        
        Args:
            radius (float): The radius of the circle in units
            
        Returns:
            float: The area of the circle in square units
        """
        pi = 3.14159
        return pi * radius ** 2
    
    circle_area = calculate_circle_area(7)
    print(f"Circle area (radius=7): {circle_area:.2f}")
    
    # 4. Inline comments demonstration
    print_example("Inline Comments")
    x = 10  # Initialize counter variable
    y = x * 2  # Double the value for processing
    z = y + 5  # Add offset for final calculation
    print(f"Final result: x={x}, y={y}, z={z}")

# =============================================================================
# 2. INDENTATION DEMONSTRATION
# =============================================================================

def demonstrate_indentation_basics():
    """Demonstrate proper indentation rules and structure."""
    print_section("2. INDENTATION BASICS")
    
    print_example("Basic Indentation Rules")
    # Demonstrating 4-space indentation standard
    if True:
        print("First level: 4 spaces")
        if True:
            print("Second level: 8 spaces")
            if True:
                print("Third level: 12 spaces")
    
    print_example("Control Flow Indentation")
    number = 15
    
    # Conditional statements with proper indentation
    if number > 0:
        print(f"{number} is positive")
        if number > 10:
            print(f"{number} is greater than 10")
            if number > 20:
                print(f"{number} is greater than 20")
            else:
                print(f"{number} is between 11 and 20")
        else:
            print(f"{number} is between 1 and 10")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")
    
    print_example("Loop Indentation")
    # Nested loops with proper indentation
    print("Multiplication table (1-3):")
    for i in range(1, 4):  # Outer loop
        print(f"Table of {i}:")
        for j in range(1, 6):  # Inner loop
            result = i * j
            print(f"  {i} × {j} = {result}")
        print()  # Empty line after each table

# =============================================================================
# 3. COMMENT OPERATIONS
# =============================================================================

def demonstrate_comment_operations():
    """Demonstrate various ways to use comments in operations."""
    print_section("3. COMMENT OPERATIONS")
    
    print_example("Code Documentation Comments")
    
    # Variable declarations with explanatory comments
    student_name = "Alice Johnson"      # Student's full name
    student_age = 20                    # Student's age in years
    student_gpa = 3.85                  # Grade Point Average (0.0-4.0 scale)
    is_honors_student = True            # Boolean flag for honors program
    
    print(f"Student: {student_name}, Age: {student_age}, GPA: {student_gpa}")
    
    print_example("Algorithm Explanation Comments")
    
    def bubble_sort_with_comments(arr):
        """Bubble sort implementation with detailed comments."""
        n = len(arr)
        print(f"Sorting array of {n} elements: {arr}")
        
        # Outer loop: controls number of passes through the array
        for i in range(n):
            # Flag to track if any swaps occurred in this pass
            swapped = False
            print(f"Pass {i + 1}:")
            
            # Inner loop: compare adjacent elements
            for j in range(0, n - i - 1):
                print(f"  Comparing {arr[j]} and {arr[j + 1]}")
                
                # Compare adjacent elements
                if arr[j] > arr[j + 1]:
                    # Swap elements if they're in wrong order
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    print(f"    Swapped! Array: {arr}")
                else:
                    print(f"    No swap needed")
            
            # Optimization: if no swaps occurred, array is sorted
            if not swapped:
                print("  No swaps in this pass - array is sorted!")
                break
        
        return arr
    
    # Test the bubble sort with comments
    test_array = [64, 34, 25, 12]
    sorted_array = bubble_sort_with_comments(test_array.copy())
    print(f"Final sorted array: {sorted_array}")

# =============================================================================
# 4. INDENTATION OPERATIONS
# =============================================================================

def demonstrate_indentation_operations():
    """Demonstrate complex indentation in various Python constructs."""
    print_section("4. INDENTATION OPERATIONS")
    
    print_example("Class and Method Indentation")
    
    class StudentGradeCalculator:
        """A class demonstrating proper indentation in class definitions."""
        
        def __init__(self, name):
            """Initialize the grade calculator for a student."""
            self.name = name
            self.grades = []
            self.grade_count = 0
        
        def add_grade(self, grade):
            """Add a grade to the student's record."""
            if 0 <= grade <= 100:
                self.grades.append(grade)
                self.grade_count += 1
                print(f"Added grade {grade} for {self.name}")
            else:
                print(f"Invalid grade: {grade}. Must be between 0 and 100.")
        
        def calculate_average(self):
            """Calculate the average of all grades."""
            if self.grade_count > 0:
                average = sum(self.grades) / self.grade_count
                return round(average, 2)
            else:
                return 0.0
        
        def get_letter_grade(self):
            """Determine letter grade based on average."""
            average = self.calculate_average()
            
            if average >= 90:
                return 'A'
            elif average >= 80:
                return 'B'
            elif average >= 70:
                return 'C'
            elif average >= 60:
                return 'D'
            else:
                return 'F'
        
        def print_report(self):
            """Print a comprehensive grade report."""
            print(f"\nGrade Report for {self.name}:")
            print(f"  Individual grades: {self.grades}")
            print(f"  Average: {self.calculate_average()}%")
            print(f"  Letter grade: {self.get_letter_grade()}")
    
    # Test the class with proper indentation
    student = StudentGradeCalculator("Bob Smith")
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    student.add_grade(88)
    student.print_report()

# =============================================================================
# 5. COMMENT WRITING METHODS
# =============================================================================

def demonstrate_comment_methods():
    """Demonstrate different methods for writing effective comments."""
    print_section("5. COMMENT WRITING METHODS")
    
    print_example("Method 1: Explanatory Comments")
    
    def fibonacci_with_explanation(n):
        """Generate Fibonacci sequence with explanatory comments."""
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        sequence = [a, b]
        
        # Generate the remaining numbers in the sequence
        for i in range(2, n):
            # Each Fibonacci number is the sum of the previous two
            next_num = a + b
            sequence.append(next_num)
            
            # Update variables for the next iteration
            a, b = b, next_num
        
        return sequence
    
    fib_sequence = fibonacci_with_explanation(8)
    print(f"Fibonacci sequence (8 terms): {fib_sequence}")
    
    print_example("Method 2: Purpose and Intent Comments")
    
    def validate_email_with_purpose(email):
        """Validate email format with purpose-focused comments."""
        # Purpose: Ensure email format is valid before database storage
        # This prevents data corruption and improves user experience
        
        # Define email validation pattern
        # Pattern explanation: username@domain.extension format
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Perform the validation and return boolean result
        is_valid = bool(re.match(pattern, email))
        
        return is_valid
    
    # Test email validation
    test_emails = ["user@example.com", "invalid-email", "test@domain.co.uk"]
    for email in test_emails:
        result = validate_email_with_purpose(email)
        print(f"Email '{email}' is {'valid' if result else 'invalid'}")

# =============================================================================
# 6. COMMON ERRORS AND CORRECTIONS
# =============================================================================

def demonstrate_common_errors():
    """Demonstrate common comment and indentation errors with corrections."""
    print_section("6. COMMON ERRORS AND CORRECTIONS")
    
    print_example("Comment Errors - Corrected Examples")
    
    # ✅ GOOD: Comments that explain WHY, not WHAT
    def calculate_compound_interest(principal, rate, time):
        """Calculate compound interest using standard financial formula."""
        # Use compound interest formula: A = P(1 + r)^t
        # This accounts for interest earned on previously earned interest
        return principal * (1 + rate) ** time
    
    # Example usage
    investment = calculate_compound_interest(1000, 0.05, 10)
    print(f"$1000 invested at 5% for 10 years: ${investment:.2f}")
    
    # ✅ GOOD: Updated comments that match the code
    def calculate_area(radius):
        """Calculate the area of a circle using π × r²."""
        # Calculate area using the standard circle area formula
        pi = 3.14159
        area = pi * radius ** 2
        return area
    
    area = calculate_area(5)
    print(f"Circle area (radius=5): {area:.2f}")
    
    print_example("Indentation Corrections")
    
    # ✅ GOOD: Consistent 4-space indentation
    def proper_indentation_example():
        """Demonstrate correct indentation patterns."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        for num in numbers:
            if num % 2 == 0:
                print(f"{num} is even")
                if num > 5:
                    print(f"  {num} is a large even number")
                else:
                    print(f"  {num} is a small even number")
            else:
                print(f"{num} is odd")
                if num > 5:
                    print(f"  {num} is a large odd number")
                else:
                    print(f"  {num} is a small odd number")
    
    proper_indentation_example()

# =============================================================================
# 7. BEST PRACTICES DEMONSTRATION
# =============================================================================

def demonstrate_best_practices():
    """Demonstrate best practices for comments and indentation."""
    print_section("7. BEST PRACTICES DEMONSTRATION")
    
    print_example("Professional Code Structure")
    
    def advanced_data_analyzer():
        """Analyze data with professional commenting and indentation standards."""
        # Sample dataset for analysis
        sales_data = [
            {'month': 'January', 'sales': 15000, 'costs': 8000},
            {'month': 'February', 'sales': 18000, 'costs': 9500},
            {'month': 'March', 'sales': 22000, 'costs': 11000}
        ]
        
        # Initialize analysis variables
        total_revenue = 0
        total_costs = 0
        monthly_profits = []
        best_month = {'month': '', 'profit': 0}
        
        print("Monthly Analysis:")
        print("-" * 50)
        
        # Process each month's data
        for month_data in sales_data:
            month_name = month_data['month']
            monthly_sales = month_data['sales']
            monthly_costs = month_data['costs']
            
            # Calculate monthly profit
            monthly_profit = monthly_sales - monthly_costs
            monthly_profits.append(monthly_profit)
            
            # Update running totals
            total_revenue += monthly_sales
            total_costs += monthly_costs
            
            # Track best performing month
            if monthly_profit > best_month['profit']:
                best_month = {
                    'month': month_name,
                    'profit': monthly_profit
                }
            
            # Display monthly results
            profit_margin = (monthly_profit / monthly_sales) * 100
            print(f"{month_name:>10}: Sales ${monthly_sales:>6,} | "
                  f"Costs ${monthly_costs:>6,} | "
                  f"Profit ${monthly_profit:>6,} ({profit_margin:>5.1f}%)")
        
        # Calculate overall statistics
        total_profit = total_revenue - total_costs
        overall_profit_margin = (total_profit / total_revenue) * 100
        
        # Display summary results
        print("-" * 50)
        print("Summary Analysis:")
        print(f"{'Total Revenue:':<20} ${total_revenue:>8,}")
        print(f"{'Total Costs:':<20} ${total_costs:>8,}")
        print(f"{'Total Profit:':<20} ${total_profit:>8,}")
        print(f"{'Profit Margin:':<20} {overall_profit_margin:>7.1f}%")
        print(f"{'Best Month:':<20} {best_month['month']} (${best_month['profit']:,})")
        
        return {
            'total_revenue': total_revenue,
            'total_profit': total_profit,
            'best_month': best_month,
            'profit_margin': overall_profit_margin
        }
    
    # Execute the analysis
    analysis_results = advanced_data_analyzer()
    
    print_example("Code Maintenance Tips")
    print("✅ Best Practices Applied:")
    print("  • Used descriptive variable names")
    print("  • Comments explain business logic, not syntax")
    print("  • Consistent 4-space indentation throughout")
    print("  • Proper spacing around operators and after commas")
    print("  • Clear function and class documentation")
    print("  • Logical code organization and structure")
    print("  • Professional formatting and alignment")

# =============================================================================
# MAIN EXECUTION FUNCTION
# =============================================================================

def main():
    """
    Main function to execute all comment and indentation demonstrations.
    
    This function orchestrates the execution of all examples in a
    logical order, demonstrating the progression from basic concepts
    to advanced best practices.
    """
    print("🐍 COMMENTS AND INDENTATION COMPREHENSIVE EXAMPLES")
    print("=" * 70)
    print("This program demonstrates all aspects of Python comments and indentation")
    print("based on the comprehensive documentation.")
    
    try:
        # Execute all demonstration functions in logical order
        demonstrate_comment_types()
        demonstrate_indentation_basics()
        demonstrate_comment_operations()
        demonstrate_indentation_operations()
        demonstrate_comment_methods()
        demonstrate_common_errors()
        demonstrate_best_practices()
        
        # Final success message
        print(f"\n{'='*70}")
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("📚 Check the documentation for detailed explanations.")
        print("💡 Remember: Good comments explain WHY, good code explains WHAT.")
        print("📏 Always use consistent 4-space indentation!")
        print(f"{'='*70}")
        
    except Exception as e:
        print(f"\n❌ Error occurred during execution: {e}")
        print("Please check your Python installation and try again.")

# Execute the program when run directly
if __name__ == "__main__":
    main()
