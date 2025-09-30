#!/usr/bin/env python3
"""
Python Recursion Program

This program demonstrates all concepts from Recursion_documentation.md including:
- Recursion definition and characteristics
- Recursion operations
- Recursion methods
- Common errors in recursion

Author: Generated from Recursion_documentation.md
"""

import sys
import time
from functools import lru_cache, wraps


def main():
    """Main function to run all demonstrations"""
    print("=" * 70)
    print("PYTHON RECURSION DEMONSTRATION")
    print("=" * 70)
    
    # Section 1: Recursion Definition and Characteristics
    print("\n1. RECURSION DEFINITION AND CHARACTERISTICS")
    print("-" * 50)
    demonstrate_basic_recursion()
    demonstrate_recursion_types()
    demonstrate_recursion_characteristics()
    
    # Section 2: Recursion Operations
    print("\n2. RECURSION OPERATIONS")
    print("-" * 50)
    demonstrate_mathematical_operations()
    demonstrate_data_structure_operations()
    demonstrate_tree_operations()
    
    # Section 3: Recursion Methods
    print("\n3. RECURSION METHODS")
    print("-" * 50)
    demonstrate_optimization_techniques()
    demonstrate_tail_recursion()
    demonstrate_analysis_methods()
    
    # Section 4: Common Errors
    print("\n4. COMMON ERRORS IN RECURSION")
    print("-" * 50)
    demonstrate_common_errors()
    demonstrate_best_practices()
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)


# Section 1: Recursion Definition and Characteristics

def demonstrate_basic_recursion():
    """Demonstrate basic recursion structure"""
    print("\n1.1 Basic Recursion Structure")
    
    def countdown(n):
        """Count down from n to 0"""
        if n <= 0:
            print("    Blast off!")
            return
        print(f"    {n}")
        countdown(n - 1)
    
    def factorial(n):
        """Calculate factorial of n using recursion"""
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    print("Simple Countdown:")
    countdown(5)
    
    print("\nFactorial Examples:")
    for i in range(6):
        result = factorial(i)
        print(f"  {i}! = {result}")


def demonstrate_recursion_types():
    """Demonstrate different types of recursion"""
    print("\n1.2 Types of Recursion")
    
    # Linear Recursion
    def sum_natural_numbers(n):
        """Sum of first n natural numbers"""
        if n <= 0:
            return 0
        return n + sum_natural_numbers(n - 1)
    
    def power(base, exponent):
        """Calculate base^exponent using recursion"""
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        return base * power(base, exponent - 1)
    
    # Tree Recursion
    def fibonacci_tree(n):
        """Fibonacci using tree recursion"""
        if n <= 1:
            return n
        return fibonacci_tree(n - 1) + fibonacci_tree(n - 2)
    
    def tower_of_hanoi(n, source, destination, auxiliary):
        """Solve Tower of Hanoi puzzle"""
        if n == 1:
            print(f"    Move disk 1 from {source} to {destination}")
            return
        
        tower_of_hanoi(n - 1, source, auxiliary, destination)
        print(f"    Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n - 1, auxiliary, destination, source)
    
    # Tail Recursion
    def factorial_tail(n, accumulator=1):
        """Tail recursive factorial"""
        if n <= 1:
            return accumulator
        return factorial_tail(n - 1, n * accumulator)
    
    def fibonacci_tail(n, a=0, b=1):
        """Tail recursive fibonacci"""
        if n == 0:
            return a
        if n == 1:
            return b
        return fibonacci_tail(n - 1, b, a + b)
    
    print("Linear Recursion:")
    print(f"  Sum of first 10 numbers: {sum_natural_numbers(10)}")
    print(f"  5^3 = {power(5, 3)}")
    
    print("\nTree Recursion:")
    print(f"  Fibonacci(7) = {fibonacci_tree(7)}")
    print("  Tower of Hanoi (3 disks):")
    tower_of_hanoi(3, "A", "C", "B")
    
    print("\nTail Recursion:")
    print(f"  Factorial(5) = {factorial_tail(5)}")
    print(f"  Fibonacci(10) = {fibonacci_tail(10)}")


def demonstrate_recursion_characteristics():
    """Demonstrate recursion characteristics"""
    print("\n1.3 Recursion Characteristics")
    
    def trace_recursion(n, depth=0):
        """Trace recursive calls"""
        indent = "  " * depth
        print(f"  {indent}Entering: trace_recursion({n})")
        
        if n <= 0:
            print(f"  {indent}Base case reached: returning 0")
            return 0
        
        print(f"  {indent}Making recursive call with {n-1}")
        result = n + trace_recursion(n - 1, depth + 1)
        
        print(f"  {indent}Returning: {result}")
        return result
    
    def get_recursion_limit():
        """Get current recursion limit"""
        return sys.getrecursionlimit()
    
    def deep_recursion(n, max_depth=0):
        """Test recursion depth"""
        if n <= 0:
            return max_depth
        return deep_recursion(n - 1, max_depth + 1)
    
    print("Stack Behavior Trace:")
    final_result = trace_recursion(3)
    print(f"  Final result: {final_result}")
    
    print(f"\nMemory Analysis:")
    print(f"  Default recursion limit: {get_recursion_limit()}")
    
    try:
        depth = deep_recursion(100)
        print(f"  Reached depth: {depth}")
    except RecursionError as e:
        print(f"  RecursionError: Maximum recursion depth exceeded")


# Section 2: Recursion Operations

def demonstrate_mathematical_operations():
    """Demonstrate recursive mathematical operations"""
    print("\n2.1 Mathematical Operations")
    
    def recursive_addition(a, b):
        """Add two numbers using recursion"""
        if b == 0:
            return a
        if b > 0:
            return recursive_addition(a + 1, b - 1)
        else:
            return recursive_addition(a - 1, b + 1)
    
    def recursive_multiplication(a, b):
        """Multiply two numbers using recursion"""
        if b == 0:
            return 0
        if b == 1:
            return a
        if b > 0:
            return a + recursive_multiplication(a, b - 1)
        else:
            return -recursive_multiplication(a, -b)
    
    def recursive_power(base, exponent):
        """Calculate power using recursion with optimization"""
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        
        if exponent % 2 == 0:
            half_power = recursive_power(base, exponent // 2)
            return half_power * half_power
        else:
            return base * recursive_power(base, exponent - 1)
    
    def gcd_recursive(a, b):
        """Greatest Common Divisor using Euclidean algorithm"""
        if b == 0:
            return a
        return gcd_recursive(b, a % b)
    
    def fibonacci_memoized():
        """Memoized fibonacci for efficiency"""
        cache = {}
        
        def fib(n):
            if n in cache:
                return cache[n]
            
            if n <= 1:
                return n
            
            cache[n] = fib(n - 1) + fib(n - 2)
            return cache[n]
        
        return fib
    
    print("Arithmetic Operations:")
    print(f"  5 + 3 = {recursive_addition(5, 3)}")
    print(f"  7 * 4 = {recursive_multiplication(7, 4)}")
    print(f"  2^10 = {recursive_power(2, 10)}")
    print(f"  GCD(48, 18) = {gcd_recursive(48, 18)}")
    
    print("\nSequence Operations:")
    fib = fibonacci_memoized()
    print("  Fibonacci sequence (first 10):")
    for i in range(10):
        print(f"    F({i}) = {fib(i)}")


def demonstrate_data_structure_operations():
    """Demonstrate recursive operations on data structures"""
    print("\n2.2 Data Structure Operations")
    
    # List Operations
    def recursive_sum(lst):
        """Sum all elements in a list"""
        if not lst:
            return 0
        return lst[0] + recursive_sum(lst[1:])
    
    def recursive_max(lst):
        """Find maximum element in a list"""
        if len(lst) == 1:
            return lst[0]
        
        max_of_rest = recursive_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest
    
    def recursive_reverse(lst):
        """Reverse a list recursively"""
        if len(lst) <= 1:
            return lst
        return [lst[-1]] + recursive_reverse(lst[:-1])
    
    def recursive_flatten(nested_list):
        """Flatten a nested list"""
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(recursive_flatten(item))
            else:
                result.append(item)
        return result
    
    # String Operations
    def is_palindrome(s):
        """Check if string is palindrome"""
        s = s.replace(" ", "").lower()
        
        if len(s) <= 1:
            return True
        
        if s[0] != s[-1]:
            return False
        
        return is_palindrome(s[1:-1])
    
    def recursive_string_reverse(s):
        """Reverse string recursively"""
        if len(s) <= 1:
            return s
        return s[-1] + recursive_string_reverse(s[:-1])
    
    def count_character(s, char):
        """Count occurrences of character"""
        if not s:
            return 0
        
        count = 1 if s[0] == char else 0
        return count + count_character(s[1:], char)
    
    def generate_permutations(s):
        """Generate all permutations of string"""
        if len(s) <= 1:
            return [s]
        
        permutations = []
        for i in range(len(s)):
            char = s[i]
            remaining = s[:i] + s[i+1:]
            for perm in generate_permutations(remaining):
                permutations.append(char + perm)
        
        return permutations
    
    print("List Operations:")
    numbers = [1, 2, 3, 4, 5]
    nested = [1, [2, 3], [4, [5, 6]], 7]
    
    print(f"  Sum of {numbers}: {recursive_sum(numbers)}")
    print(f"  Max of {numbers}: {recursive_max(numbers)}")
    print(f"  Reverse of {numbers}: {recursive_reverse(numbers)}")
    print(f"  Flatten {nested}: {recursive_flatten(nested)}")
    
    print("\nString Operations:")
    test_string = "hello"
    palindrome_test = "A man a plan a canal Panama"
    
    print(f"  '{test_string}' reversed: '{recursive_string_reverse(test_string)}'")
    print(f"  Count 'l' in '{test_string}': {count_character(test_string, 'l')}")
    print(f"  Is '{palindrome_test}' palindrome? {is_palindrome(palindrome_test)}")
    
    perms = generate_permutations("abc")
    print(f"  Permutations of 'abc': {perms}")


class TreeNode:
    """Simple binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def demonstrate_tree_operations():
    """Demonstrate recursive tree operations"""
    print("\n2.3 Tree Operations")
    
    def tree_height(root):
        """Calculate height of binary tree"""
        if not root:
            return 0
        
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        
        return 1 + max(left_height, right_height)
    
    def tree_size(root):
        """Count total nodes in tree"""
        if not root:
            return 0
        
        return 1 + tree_size(root.left) + tree_size(root.right)
    
    def tree_sum(root):
        """Sum all values in tree"""
        if not root:
            return 0
        
        return root.val + tree_sum(root.left) + tree_sum(root.right)
    
    def inorder_traversal(root, result=None):
        """Inorder traversal: left -> root -> right"""
        if result is None:
            result = []
        
        if root:
            inorder_traversal(root.left, result)
            result.append(root.val)
            inorder_traversal(root.right, result)
        
        return result
    
    def preorder_traversal(root, result=None):
        """Preorder traversal: root -> left -> right"""
        if result is None:
            result = []
        
        if root:
            result.append(root.val)
            preorder_traversal(root.left, result)
            preorder_traversal(root.right, result)
        
        return result
    
    def postorder_traversal(root, result=None):
        """Postorder traversal: left -> right -> root"""
        if result is None:
            result = []
        
        if root:
            postorder_traversal(root.left, result)
            postorder_traversal(root.right, result)
            result.append(root.val)
        
        return result
    
    def find_path_to_node(root, target, path=None):
        """Find path from root to target node"""
        if path is None:
            path = []
        
        if not root:
            return None
        
        path.append(root.val)
        
        if root.val == target:
            return path.copy()
        
        left_path = find_path_to_node(root.left, target, path)
        if left_path:
            return left_path
        
        right_path = find_path_to_node(root.right, target, path)
        if right_path:
            return right_path
        
        path.pop()
        return None
    
    # Create sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Binary Tree Operations:")
    print(f"  Tree height: {tree_height(root)}")
    print(f"  Tree size: {tree_size(root)}")
    print(f"  Tree sum: {tree_sum(root)}")
    print(f"  Inorder: {inorder_traversal(root)}")
    print(f"  Preorder: {preorder_traversal(root)}")
    print(f"  Postorder: {postorder_traversal(root)}")
    print(f"  Path to node 5: {find_path_to_node(root, 5)}")


# Section 3: Recursion Methods

def demonstrate_optimization_techniques():
    """Demonstrate optimization techniques"""
    print("\n3.1 Optimization Techniques")
    
    # Without memoization (inefficient)
    def fibonacci_naive(n):
        """Naive fibonacci - exponential time complexity"""
        if n <= 1:
            return n
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
    
    # With memoization using dictionary
    def fibonacci_memoized():
        """Memoized fibonacci using closure"""
        cache = {}
        
        def fib(n):
            if n in cache:
                return cache[n]
            
            if n <= 1:
                cache[n] = n
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
            
            return cache[n]
        
        return fib
    
    # Using functools.lru_cache decorator
    @lru_cache(maxsize=None)
    def fibonacci_lru_cache(n):
        """Fibonacci with LRU cache decorator"""
        if n <= 1:
            return n
        return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)
    
    # Custom memoization decorator
    def memoize(func):
        """Custom memoization decorator"""
        cache = {}
        
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        
        wrapper.cache = cache
        wrapper.cache_clear = cache.clear
        return wrapper
    
    @memoize
    def expensive_recursive_function(n):
        """Example of expensive recursive function"""
        if n <= 1:
            return n
        return expensive_recursive_function(n - 1) + expensive_recursive_function(n - 2)
    
    # Dynamic Programming Conversion
    def fibonacci_dp_bottom_up(n):
        """Bottom-up DP fibonacci"""
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def fibonacci_dp_optimized(n):
        """Space-optimized DP fibonacci"""
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1
    
    print("Memoization Techniques:")
    n = 20
    
    # Memoized version
    fib_memo = fibonacci_memoized()
    start_time = time.time()
    result_memo = fib_memo(n)
    memo_time = time.time() - start_time
    
    # LRU cache version
    start_time = time.time()
    result_lru = fibonacci_lru_cache(n)
    lru_time = time.time() - start_time
    
    print(f"  Fibonacci({n}):")
    print(f"    Memoized result: {result_memo} (Time: {memo_time:.6f}s)")
    print(f"    LRU cache result: {result_lru} (Time: {lru_time:.6f}s)")
    print(f"    LRU cache info: {fibonacci_lru_cache.cache_info()}")
    
    # Test custom decorator
    result_custom = expensive_recursive_function(15)
    print(f"    Custom memoized result: {result_custom}")
    print(f"    Cache size: {len(expensive_recursive_function.cache)}")
    
    print("\nDynamic Programming Conversion:")
    print(f"  DP Bottom-up: {fibonacci_dp_bottom_up(n)}")
    print(f"  DP Optimized: {fibonacci_dp_optimized(n)}")


def demonstrate_tail_recursion():
    """Demonstrate tail recursion optimization"""
    print("\n3.2 Tail Recursion Optimization")
    
    # Non-tail recursive version
    def factorial_non_tail(n):
        """Non-tail recursive factorial"""
        if n <= 1:
            return 1
        return n * factorial_non_tail(n - 1)
    
    # Tail recursive version
    def factorial_tail_recursive(n, accumulator=1):
        """Tail recursive factorial"""
        if n <= 1:
            return accumulator
        return factorial_tail_recursive(n - 1, n * accumulator)
    
    def sum_tail_recursive(lst, accumulator=0):
        """Tail recursive sum"""
        if not lst:
            return accumulator
        return sum_tail_recursive(lst[1:], accumulator + lst[0])
    
    # Generic tail recursion converter
    def make_tail_recursive(func):
        """Convert function to tail recursive using trampoline"""
        def trampoline(f, *args, **kwargs):
            result = f(*args, **kwargs)
            while callable(result):
                result = result()
            return result
        
        def tail_recursive_wrapper(*args, **kwargs):
            return trampoline(func, *args, **kwargs)
        
        return tail_recursive_wrapper
    
    def factorial_trampoline(n, acc=1):
        """Factorial using trampoline technique"""
        if n <= 1:
            return acc
        return lambda: factorial_trampoline(n - 1, n * acc)
    
    print("Tail Recursion Methods:")
    n = 10
    test_list = [1, 2, 3, 4, 5]
    
    print(f"  Factorial({n}):")
    print(f"    Non-tail: {factorial_non_tail(n)}")
    print(f"    Tail recursive: {factorial_tail_recursive(n)}")
    
    print(f"  Sum of {test_list}:")
    print(f"    Tail recursive: {sum_tail_recursive(test_list)}")
    
    # Trampoline example
    trampoline_factorial = make_tail_recursive(factorial_trampoline)
    print(f"    Trampoline factorial(5): {trampoline_factorial(5)}")


def demonstrate_analysis_methods():
    """Demonstrate recursion analysis methods"""
    print("\n3.3 Recursion Analysis Methods")
    
    def recursion_profiler(func):
        """Decorator to profile recursive function calls"""
        call_count = 0
        max_depth = 0
        current_depth = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count, max_depth, current_depth
            
            call_count += 1
            current_depth += 1
            max_depth = max(max_depth, current_depth)
            
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                current_depth -= 1
        
        wrapper.get_stats = lambda: {
            'call_count': call_count,
            'max_depth': max_depth
        }
        
        def reset_stats():
            nonlocal call_count, max_depth
            call_count = 0
            max_depth = 0
        
        wrapper.reset_stats = reset_stats
        
        return wrapper
    
    def time_recursive_function(func, *args, **kwargs):
        """Time a recursive function execution"""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        return result, end_time - start_time
    
    @recursion_profiler
    def fibonacci_profiled(n):
        if n <= 1:
            return n
        return fibonacci_profiled(n - 1) + fibonacci_profiled(n - 2)
    
    @recursion_profiler
    def factorial_profiled(n):
        if n <= 1:
            return 1
        return n * factorial_profiled(n - 1)
    
    print("Function Analysis:")
    
    # Test fibonacci
    n = 8
    result = fibonacci_profiled(n)
    stats = fibonacci_profiled.get_stats()
    print(f"  fibonacci_profiled({n}):")
    print(f"    Result: {result}")
    print(f"    Calls: {stats['call_count']}")
    print(f"    Max Depth: {stats['max_depth']}")
    
    fibonacci_profiled.reset_stats()
    
    # Test factorial
    n = 5
    result = factorial_profiled(n)
    stats = factorial_profiled.get_stats()
    print(f"  factorial_profiled({n}):")
    print(f"    Result: {result}")
    print(f"    Calls: {stats['call_count']}")
    print(f"    Max Depth: {stats['max_depth']}")


# Section 4: Common Errors

def demonstrate_common_errors():
    """Demonstrate common recursion errors"""
    print("\n4.1 Common Recursion Errors")
    
    # Base Case Errors
    def wrong_countdown(n):
        """Countdown without proper base case"""
        if n < 0:  # Wrong base case
            return
        print(f"    {n}")
        return wrong_countdown(n - 1)
    
    def correct_countdown(n):
        """Countdown with proper base case"""
        if n <= 0:  # Correct base case
            print("    Done!")
            return
        print(f"    {n}")
        correct_countdown(n - 1)
    
    # Performance Issues
    def wrong_fibonacci(n):
        """Naive fibonacci with exponential complexity"""
        if n <= 1:
            return n
        return wrong_fibonacci(n - 1) + wrong_fibonacci(n - 2)
    
    @lru_cache(maxsize=None)
    def correct_fibonacci(n):
        """Memoized fibonacci with linear complexity"""
        if n <= 1:
            return n
        return correct_fibonacci(n - 1) + correct_fibonacci(n - 2)
    
    # Stack Overflow Issues
    def deep_recursion_test(n):
        """Function that may cause stack overflow"""
        if n <= 0:
            return 0
        return 1 + deep_recursion_test(n - 1)
    
    def safe_recursive_call(func, *args, max_attempts=3, **kwargs):
        """Safely call recursive function with fallback"""
        original_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(100)  # Set low limit for demo
        
        try:
            return func(*args, **kwargs), None
        except RecursionError as e:
            return None, f"RecursionError: {e}"
        finally:
            sys.setrecursionlimit(original_limit)
    
    print("Base Case Errors:")
    print("  Wrong countdown (would cause infinite recursion):")
    result, error = safe_recursive_call(wrong_countdown, 3)
    if error:
        print(f"    {error}")
    
    print("  Correct countdown:")
    correct_countdown(3)
    
    print("\nPerformance Issues:")
    n = 25
    
    # Time naive fibonacci
    start_time = time.time()
    result_naive = wrong_fibonacci(n)
    naive_time = time.time() - start_time
    
    # Time memoized fibonacci
    start_time = time.time()
    result_memo = correct_fibonacci(n)
    memo_time = time.time() - start_time
    
    print(f"  Fibonacci({n}):")
    print(f"    Naive: {result_naive} (Time: {naive_time:.6f}s)")
    print(f"    Memoized: {result_memo} (Time: {memo_time:.6f}s)")
    print(f"    Speedup: {naive_time / memo_time:.2f}x")
    
    print("\nStack Overflow Issues:")
    test_values = [50, 500]
    
    for n in test_values:
        result, error = safe_recursive_call(deep_recursion_test, n)
        if error:
            print(f"  deep_recursion_test({n}): {error}")
        else:
            print(f"  deep_recursion_test({n}): {result}")


def demonstrate_best_practices():
    """Demonstrate best practices for recursion"""
    print("\n4.2 Best Practices")
    
    print("""
Recursion Best Practices Checklist:

1. BASE CASE DESIGN:
   ✓ Always define clear base cases
   ✓ Ensure base cases handle all edge conditions
   ✓ Test base cases with boundary values
   ✓ Make sure recursive calls progress toward base cases

2. PARAMETER VALIDATION:
   ✓ Validate input parameters at function entry
   ✓ Handle None, empty, and negative inputs appropriately
   ✓ Use type hints for clarity
   ✓ Document parameter constraints

3. PERFORMANCE OPTIMIZATION:
   ✓ Use memoization for overlapping subproblems
   ✓ Consider iterative alternatives for deep recursion
   ✓ Implement tail recursion when possible
   ✓ Profile recursive functions for performance bottlenecks

4. STACK MANAGEMENT:
   ✓ Be aware of recursion depth limits
   ✓ Use sys.setrecursionlimit() carefully if needed
   ✓ Implement depth limiting in recursive functions
   ✓ Consider trampolines for tail recursion optimization

5. ERROR HANDLING:
   ✓ Use try-except blocks for recursive calls that might fail
   ✓ Provide meaningful error messages
   ✓ Implement graceful degradation to iterative solutions
   ✓ Test with edge cases and large inputs
    """)
    
    def robust_factorial(n, _depth=0, _max_depth=1000):
        """
        Calculate factorial with comprehensive error handling.
        
        Args:
            n: Non-negative integer
            _depth: Internal parameter for depth tracking
            _max_depth: Maximum recursion depth allowed
        
        Returns:
            int: Factorial of n
        """
        # Parameter validation
        if not isinstance(n, int):
            raise TypeError(f"Expected integer, got {type(n).__name__}")
        
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        # Depth limiting
        if _depth > _max_depth:
            # Fallback to iterative solution
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        
        # Base cases
        if n <= 1:
            return 1
        
        # Recursive case with depth tracking
        return n * robust_factorial(n - 1, _depth + 1, _max_depth)
    
    def robust_fibonacci(n, _cache=None, _depth=0, _max_depth=1000):
        """
        Calculate fibonacci number with memoization and error handling.
        """
        # Initialize cache on first call
        if _cache is None:
            _cache = {}
        
        # Parameter validation
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        
        # Check cache first
        if n in _cache:
            return _cache[n]
        
        # Depth limiting with fallback to iterative
        if _depth > _max_depth:
            # Iterative fibonacci
            if n <= 1:
                return n
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        
        # Base cases
        if n <= 1:
            _cache[n] = n
            return n
        
        # Recursive case with memoization
        result = (robust_fibonacci(n - 1, _cache, _depth + 1, _max_depth) + 
                 robust_fibonacci(n - 2, _cache, _depth + 1, _max_depth))
        
        _cache[n] = result
        return result
    
    def safe_recursive_wrapper(func):
        """
        Decorator that adds safety features to recursive functions.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            original_limit = sys.getrecursionlimit()
            
            try:
                # Set a reasonable recursion limit
                sys.setrecursionlimit(min(original_limit, 2000))
                return func(*args, **kwargs)
            
            except RecursionError as e:
                raise RecursionError(
                    f"Recursion limit exceeded in {func.__name__}. "
                    f"Consider using an iterative approach or memoization."
                ) from e
            
            finally:
                # Restore original limit
                sys.setrecursionlimit(original_limit)
        
        return wrapper
    
    print("Testing Robust Implementations:")
    
    # Test robust factorial
    test_values = [0, 1, 5, 10, 20]
    for val in test_values:
        try:
            result = robust_factorial(val)
            print(f"  robust_factorial({val}) = {result}")
        except Exception as e:
            print(f"  robust_factorial({val}) error: {e}")
    
    # Test with invalid inputs
    try:
        robust_factorial(-5)
    except ValueError as e:
        print(f"  robust_factorial(-5) correctly raised: {e}")
    
    try:
        robust_factorial("not a number")
    except TypeError as e:
        print(f"  robust_factorial('not a number') correctly raised: {e}")
    
    # Test robust fibonacci
    print(f"  robust_fibonacci(20) = {robust_fibonacci(20)}")
    print(f"  robust_fibonacci(100) = {robust_fibonacci(100)}")


if __name__ == "__main__":
    main()
