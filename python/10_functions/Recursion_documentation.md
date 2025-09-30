# Python Recursion Documentation

## 1. Recursion Definition and Characteristics

### Definition

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems. A recursive function must have two essential components:

1. **Base Case**: A condition that stops the recursion
2. **Recursive Case**: The function calling itself with modified parameters

### 1.1 Basic Recursion Structure

#### Simple Recursive Function

```python
def simple_recursion_example():
    """Demonstrate basic recursion structure"""
    
    def countdown(n):
        """Count down from n to 0"""
        # Base case: stop when n reaches 0
        if n <= 0:
            print("Blast off!")
            return
        
        # Recursive case: print current number and call with n-1
        print(n)
        countdown(n - 1)
    
    print("=== Simple Countdown ===")
    countdown(5)

simple_recursion_example()
```

#### Factorial Example

```python
def factorial_example():
    """Classic factorial recursion example"""
    
    def factorial(n):
        """Calculate factorial of n using recursion"""
        # Base case: factorial of 0 or 1 is 1
        if n <= 1:
            return 1
        
        # Recursive case: n * factorial(n-1)
        return n * factorial(n - 1)
    
    print("=== Factorial Examples ===")
    for i in range(6):
        result = factorial(i)
        print(f"{i}! = {result}")

factorial_example()
```

### 1.2 Types of Recursion

#### Linear Recursion

Single recursive call in each function execution.

```python
def linear_recursion_examples():
    """Examples of linear recursion"""
    
    def sum_natural_numbers(n):
        """Sum of first n natural numbers"""
        if n <= 0:
            return 0
        return n + sum_natural_numbers(n - 1)
    
    def fibonacci_linear(n):
        """Fibonacci using linear recursion (inefficient)"""
        if n <= 1:
            return n
        return fibonacci_linear(n - 1) + fibonacci_linear(n - 2)
    
    def power(base, exponent):
        """Calculate base^exponent using recursion"""
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        return base * power(base, exponent - 1)
    
    print("=== Linear Recursion ===")
    print(f"Sum of first 10 numbers: {sum_natural_numbers(10)}")
    print(f"5^3 = {power(5, 3)}")
    print(f"Fibonacci(6) = {fibonacci_linear(6)}")

linear_recursion_examples()
```

#### Tree Recursion

Multiple recursive calls in each function execution.

```python
def tree_recursion_examples():
    """Examples of tree recursion"""
    
    def fibonacci_tree(n):
        """Fibonacci using tree recursion"""
        if n <= 1:
            return n
        return fibonacci_tree(n - 1) + fibonacci_tree(n - 2)
    
    def binary_tree_paths(node, path=""):
        """Generate all paths in a binary tree (conceptual)"""
        if node is None:
            return []
        
        current_path = path + str(node)
        
        # If leaf node, return the path
        if not hasattr(node, 'left') and not hasattr(node, 'right'):
            return [current_path]
        
        paths = []
        if hasattr(node, 'left') and node.left:
            paths.extend(binary_tree_paths(node.left, current_path + "->"))
        if hasattr(node, 'right') and node.right:
            paths.extend(binary_tree_paths(node.right, current_path + "->"))
        
        return paths
    
    def tower_of_hanoi(n, source, destination, auxiliary):
        """Solve Tower of Hanoi puzzle"""
        if n == 1:
            print(f"Move disk 1 from {source} to {destination}")
            return
        
        # Move n-1 disks from source to auxiliary
        tower_of_hanoi(n - 1, source, auxiliary, destination)
        
        # Move the largest disk from source to destination
        print(f"Move disk {n} from {source} to {destination}")
        
        # Move n-1 disks from auxiliary to destination
        tower_of_hanoi(n - 1, auxiliary, destination, source)
    
    print("=== Tree Recursion ===")
    print(f"Fibonacci(7) = {fibonacci_tree(7)}")
    
    print("\nTower of Hanoi (3 disks):")
    tower_of_hanoi(3, "A", "C", "B")

tree_recursion_examples()
```

#### Tail Recursion

Recursive call is the last operation in the function.

```python
def tail_recursion_examples():
    """Examples of tail recursion"""
    
    def factorial_tail(n, accumulator=1):
        """Tail recursive factorial"""
        if n <= 1:
            return accumulator
        return factorial_tail(n - 1, n * accumulator)
    
    def sum_tail(n, accumulator=0):
        """Tail recursive sum"""
        if n <= 0:
            return accumulator
        return sum_tail(n - 1, accumulator + n)
    
    def fibonacci_tail(n, a=0, b=1):
        """Tail recursive fibonacci"""
        if n == 0:
            return a
        if n == 1:
            return b
        return fibonacci_tail(n - 1, b, a + b)
    
    def reverse_string_tail(s, accumulator=""):
        """Tail recursive string reversal"""
        if not s:
            return accumulator
        return reverse_string_tail(s[1:], s[0] + accumulator)
    
    print("=== Tail Recursion ===")
    print(f"Factorial(5) = {factorial_tail(5)}")
    print(f"Sum(10) = {sum_tail(10)}")
    print(f"Fibonacci(10) = {fibonacci_tail(10)}")
    print(f"Reverse 'hello' = '{reverse_string_tail('hello')}'")

tail_recursion_examples()
```

### 1.3 Recursion Characteristics

#### Stack Behavior

```python
def recursion_stack_behavior():
    """Demonstrate how recursion uses the call stack"""
    
    def trace_recursion(n, depth=0):
        """Trace recursive calls"""
        indent = "  " * depth
        print(f"{indent}Entering: trace_recursion({n})")
        
        if n <= 0:
            print(f"{indent}Base case reached: returning 0")
            return 0
        
        print(f"{indent}Making recursive call with {n-1}")
        result = n + trace_recursion(n - 1, depth + 1)
        
        print(f"{indent}Returning: {result}")
        return result
    
    print("=== Stack Behavior Trace ===")
    final_result = trace_recursion(3)
    print(f"Final result: {final_result}")

recursion_stack_behavior()
```

#### Memory Usage

```python
import sys

def recursion_memory_analysis():
    """Analyze memory usage in recursion"""
    
    def get_recursion_limit():
        """Get current recursion limit"""
        return sys.getrecursionlimit()
    
    def deep_recursion(n, max_depth=0):
        """Test recursion depth"""
        if n <= 0:
            return max_depth
        return deep_recursion(n - 1, max_depth + 1)
    
    def memory_efficient_factorial(n):
        """Memory-conscious factorial"""
        if n <= 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    print("=== Memory Analysis ===")
    print(f"Default recursion limit: {get_recursion_limit()}")
    
    try:
        depth = deep_recursion(100)
        print(f"Reached depth: {depth}")
    except RecursionError as e:
        print(f"RecursionError: {e}")
    
    print(f"Iterative factorial(1000): {memory_efficient_factorial(1000) is not None}")

recursion_memory_analysis()
```

---

## 2. Recursion Operations

### 2.1 Mathematical Operations

#### Arithmetic Operations

```python
def recursive_arithmetic_operations():
    """Recursive implementations of arithmetic operations"""
    
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
        
        # Optimization: use exponent halving
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
    
    print("=== Recursive Arithmetic ===")
    print(f"5 + 3 = {recursive_addition(5, 3)}")
    print(f"7 * 4 = {recursive_multiplication(7, 4)}")
    print(f"2^10 = {recursive_power(2, 10)}")
    print(f"GCD(48, 18) = {gcd_recursive(48, 18)}")

recursive_arithmetic_operations()
```

#### Sequence Operations

```python
def recursive_sequence_operations():
    """Recursive operations on sequences"""
    
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
    
    def lucas_numbers(n):
        """Generate Lucas numbers recursively"""
        if n == 0:
            return 2
        if n == 1:
            return 1
        return lucas_numbers(n - 1) + lucas_numbers(n - 2)
    
    def tribonacci(n):
        """Tribonacci sequence (sum of previous 3 numbers)"""
        if n <= 1:
            return 0
        if n == 2:
            return 1
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    
    def catalan_numbers(n):
        """Calculate nth Catalan number"""
        if n <= 1:
            return 1
        
        result = 0
        for i in range(n):
            result += catalan_numbers(i) * catalan_numbers(n - 1 - i)
        return result
    
    print("=== Sequence Operations ===")
    
    # Fibonacci with memoization
    fib = fibonacci_memoized()
    print("Fibonacci sequence (first 10):")
    for i in range(10):
        print(f"F({i}) = {fib(i)}")
    
    print(f"\nLucas(7) = {lucas_numbers(7)}")
    print(f"Tribonacci(8) = {tribonacci(8)}")
    print(f"Catalan(5) = {catalan_numbers(5)}")

recursive_sequence_operations()
```

### 2.2 Data Structure Operations

#### List Operations

```python
def recursive_list_operations():
    """Recursive operations on lists"""
    
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
    
    def recursive_filter(predicate, lst):
        """Filter list elements using recursion"""
        if not lst:
            return []
        
        if predicate(lst[0]):
            return [lst[0]] + recursive_filter(predicate, lst[1:])
        else:
            return recursive_filter(predicate, lst[1:])
    
    def recursive_map(func, lst):
        """Apply function to all elements"""
        if not lst:
            return []
        return [func(lst[0])] + recursive_map(func, lst[1:])
    
    print("=== List Operations ===")
    numbers = [1, 2, 3, 4, 5]
    nested = [1, [2, 3], [4, [5, 6]], 7]
    
    print(f"Sum of {numbers}: {recursive_sum(numbers)}")
    print(f"Max of {numbers}: {recursive_max(numbers)}")
    print(f"Reverse of {numbers}: {recursive_reverse(numbers)}")
    print(f"Flatten {nested}: {recursive_flatten(nested)}")
    print(f"Filter evens: {recursive_filter(lambda x: x % 2 == 0, numbers)}")
    print(f"Square all: {recursive_map(lambda x: x ** 2, numbers)}")

recursive_list_operations()
```

#### String Operations

```python
def recursive_string_operations():
    """Recursive operations on strings"""
    
    def is_palindrome(s):
        """Check if string is palindrome"""
        # Remove spaces and convert to lowercase
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
    
    def string_length(s):
        """Calculate string length recursively"""
        if not s:
            return 0
        return 1 + string_length(s[1:])
    
    def remove_character(s, char):
        """Remove all occurrences of character"""
        if not s:
            return ""
        
        if s[0] == char:
            return remove_character(s[1:], char)
        else:
            return s[0] + remove_character(s[1:], char)
    
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
    
    print("=== String Operations ===")
    test_string = "hello"
    palindrome_test = "A man a plan a canal Panama"
    
    print(f"'{test_string}' reversed: '{recursive_string_reverse(test_string)}'")
    print(f"Length of '{test_string}': {string_length(test_string)}")
    print(f"Count 'l' in '{test_string}': {count_character(test_string, 'l')}")
    print(f"Remove 'l' from '{test_string}': '{remove_character(test_string, 'l')}'")
    print(f"Is '{palindrome_test}' palindrome? {is_palindrome(palindrome_test)}")
    
    # Show first few permutations
    perms = generate_permutations("abc")
    print(f"Permutations of 'abc': {perms}")

recursive_string_operations()
```

### 2.3 Tree and Graph Operations

#### Binary Tree Operations

```python
class TreeNode:
    """Simple binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recursive_tree_operations():
    """Recursive operations on binary trees"""
    
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
        
        # Search in left subtree
        left_path = find_path_to_node(root.left, target, path)
        if left_path:
            return left_path
        
        # Search in right subtree
        right_path = find_path_to_node(root.right, target, path)
        if right_path:
            return right_path
        
        # Backtrack
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
    
    print("=== Tree Operations ===")
    print(f"Tree height: {tree_height(root)}")
    print(f"Tree size: {tree_size(root)}")
    print(f"Tree sum: {tree_sum(root)}")
    print(f"Inorder: {inorder_traversal(root)}")
    print(f"Preorder: {preorder_traversal(root)}")
    print(f"Postorder: {postorder_traversal(root)}")
    print(f"Path to node 5: {find_path_to_node(root, 5)}")

recursive_tree_operations()
```

---

## 3. Recursion Methods

### 3.1 Optimization Techniques

#### Memoization

```python
def memoization_techniques():
    """Demonstrate memoization for optimization"""
    
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
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fibonacci_lru_cache(n):
        """Fibonacci with LRU cache decorator"""
        if n <= 1:
            return n
        return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)
    
    # Manual memoization decorator
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
    
    import time
    
    print("=== Memoization Techniques ===")
    
    # Compare performance
    n = 30
    
    # Memoized version
    fib_memo = fibonacci_memoized()
    start_time = time.time()
    result_memo = fib_memo(n)
    memo_time = time.time() - start_time
    
    # LRU cache version
    start_time = time.time()
    result_lru = fibonacci_lru_cache(n)
    lru_time = time.time() - start_time
    
    print(f"Fibonacci({n}):")
    print(f"  Memoized result: {result_memo} (Time: {memo_time:.6f}s)")
    print(f"  LRU cache result: {result_lru} (Time: {lru_time:.6f}s)")
    
    # Show cache info for LRU cache
    print(f"  LRU cache info: {fibonacci_lru_cache.cache_info()}")
    
    # Test custom decorator
    result_custom = expensive_recursive_function(20)
    print(f"Custom memoized function result: {result_custom}")
    print(f"Cache size: {len(expensive_recursive_function.cache)}")

memoization_techniques()
```

#### Dynamic Programming Conversion

```python
def dynamic_programming_conversion():
    """Convert recursive solutions to iterative DP"""
    
    def fibonacci_recursive(n):
        """Recursive fibonacci"""
        if n <= 1:
            return n
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
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
    
    def longest_common_subsequence_recursive(text1, text2, i=0, j=0):
        """Recursive LCS (inefficient)"""
        if i >= len(text1) or j >= len(text2):
            return 0
        
        if text1[i] == text2[j]:
            return 1 + longest_common_subsequence_recursive(text1, text2, i + 1, j + 1)
        else:
            return max(
                longest_common_subsequence_recursive(text1, text2, i + 1, j),
                longest_common_subsequence_recursive(text1, text2, i, j + 1)
            )
    
    def longest_common_subsequence_dp(text1, text2):
        """DP version of LCS"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
    
    print("=== Dynamic Programming Conversion ===")
    
    n = 20
    print(f"Fibonacci({n}):")
    print(f"  DP Bottom-up: {fibonacci_dp_bottom_up(n)}")
    print(f"  DP Optimized: {fibonacci_dp_optimized(n)}")
    
    text1, text2 = "abcde", "ace"
    print(f"\nLongest Common Subsequence of '{text1}' and '{text2}':")
    print(f"  DP version: {longest_common_subsequence_dp(text1, text2)}")

dynamic_programming_conversion()
```

### 3.2 Tail Recursion Optimization

```python
def tail_recursion_methods():
    """Demonstrate tail recursion optimization techniques"""
    
    # Non-tail recursive version
    def factorial_non_tail(n):
        """Non-tail recursive factorial"""
        if n <= 1:
            return 1
        return n * factorial_non_tail(n - 1)  # Multiplication after recursive call
    
    # Tail recursive version
    def factorial_tail_recursive(n, accumulator=1):
        """Tail recursive factorial"""
        if n <= 1:
            return accumulator
        return factorial_tail_recursive(n - 1, n * accumulator)  # No operation after recursive call
    
    # Convert non-tail to tail recursive
    def sum_non_tail(lst):
        """Non-tail recursive sum"""
        if not lst:
            return 0
        return lst[0] + sum_non_tail(lst[1:])
    
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
    
    # Example with trampoline
    def factorial_trampoline(n, acc=1):
        """Factorial using trampoline technique"""
        if n <= 1:
            return acc
        return lambda: factorial_trampoline(n - 1, n * acc)
    
    # Manual tail call optimization
    def tail_call_optimize(func):
        """Simulate tail call optimization"""
        def optimized(*args, **kwargs):
            call_stack = [(func, args, kwargs)]
            
            while call_stack:
                f, a, kw = call_stack.pop()
                result = f(*a, **kw)
                
                if isinstance(result, tuple) and len(result) == 3:
                    # Tail call detected: (function, args, kwargs)
                    call_stack.append(result)
                else:
                    return result
            
            return None
        
        return optimized
    
    def factorial_optimized(n, acc=1):
        """Factorial with manual TCO"""
        if n <= 1:
            return acc
        return (factorial_optimized, (n - 1, n * acc), {})
    
    print("=== Tail Recursion Methods ===")
    
    n = 10
    test_list = [1, 2, 3, 4, 5]
    
    print(f"Factorial({n}):")
    print(f"  Non-tail: {factorial_non_tail(n)}")
    print(f"  Tail recursive: {factorial_tail_recursive(n)}")
    
    print(f"\nSum of {test_list}:")
    print(f"  Non-tail: {sum_non_tail(test_list)}")
    print(f"  Tail recursive: {sum_tail_recursive(test_list)}")
    
    # Trampoline example
    trampoline_factorial = make_tail_recursive(factorial_trampoline)
    print(f"  Trampoline factorial(5): {trampoline_factorial(5)}")

tail_recursion_methods()
```

### 3.3 Recursion Analysis Methods

```python
import sys
import time
from functools import wraps

def recursion_analysis_methods():
    """Methods for analyzing recursive functions"""
    
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
        wrapper.reset_stats = lambda: exec('nonlocal call_count, max_depth; call_count = 0; max_depth = 0')
        
        return wrapper
    
    def time_recursive_function(func, *args, **kwargs):
        """Time a recursive function execution"""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        return result, end_time - start_time
    
    def compare_recursive_implementations(*implementations):
        """Compare multiple recursive implementations"""
        def comparator(*args, **kwargs):
            results = {}
            
            for name, func in implementations:
                try:
                    result, exec_time = time_recursive_function(func, *args, **kwargs)
                    results[name] = {
                        'result': result,
                        'time': exec_time,
                        'error': None
                    }
                    
                    if hasattr(func, 'get_stats'):
                        results[name]['stats'] = func.get_stats()
                        func.reset_stats()
                        
                except Exception as e:
                    results[name] = {
                        'result': None,
                        'time': None,
                        'error': str(e)
                    }
            
            return results
        
        return comparator
    
    # Example functions to analyze
    @recursion_profiler
    def fibonacci_naive(n):
        if n <= 1:
            return n
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
    
    @recursion_profiler
    def fibonacci_memoized(n, cache={}):
        if n in cache:
            return cache[n]
        if n <= 1:
            cache[n] = n
        else:
            cache[n] = fibonacci_memoized(n - 1, cache) + fibonacci_memoized(n - 2, cache)
        return cache[n]
    
    def fibonacci_iterative(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def analyze_recursion_depth(func, max_n=100):
        """Analyze how recursion depth grows with input"""
        depths = []
        
        for n in range(1, max_n + 1):
            try:
                func(n)
                if hasattr(func, 'get_stats'):
                    stats = func.get_stats()
                    depths.append((n, stats['max_depth']))
                    func.reset_stats()
                else:
                    depths.append((n, n))  # Estimate for simple cases
            except RecursionError:
                break
        
        return depths
    
    print("=== Recursion Analysis Methods ===")
    
    # Compare fibonacci implementations
    compare_fib = compare_recursive_implementations(
        ('Naive', fibonacci_naive),
        ('Memoized', fibonacci_memoized),
        ('Iterative', fibonacci_iterative)
    )
    
    n = 20
    comparison = compare_fib(n)
    
    print(f"Fibonacci({n}) Comparison:")
    for name, data in comparison.items():
        if data['error']:
            print(f"  {name}: Error - {data['error']}")
        else:
            print(f"  {name}: Result = {data['result']}, Time = {data['time']:.6f}s")
            if 'stats' in data:
                print(f"    Calls: {data['stats']['call_count']}, Max Depth: {data['stats']['max_depth']}")
    
    # Analyze recursion depth growth
    print(f"\nRecursion Depth Analysis (first 10 values):")
    depths = analyze_recursion_depth(fibonacci_naive, 10)
    for n, depth in depths:
        print(f"  fibonacci_naive({n}): max_depth = {depth}")

recursion_analysis_methods()
```

---

## 4. Common Errors in Recursion

### 4.1 Base Case Errors

#### Missing Base Case

```python
def base_case_errors():
    """Demonstrate common base case errors"""
    
    # ❌ WRONG: Missing base case
    def wrong_countdown(n):
        """Countdown without proper base case"""
        print(n)
        return wrong_countdown(n - 1)  # Will cause infinite recursion
    
    # ❌ WRONG: Incorrect base case
    def wrong_factorial(n):
        """Factorial with wrong base case"""
        if n == 0:  # Should also handle n == 1
            return 1
        return n * wrong_factorial(n - 1)  # Will recurse forever for n = 1
    
    # ❌ WRONG: Base case never reached
    def wrong_fibonacci(n):
        """Fibonacci that never reaches base case"""
        if n < 0:  # Base case for negative numbers only
            return 0
        return wrong_fibonacci(n - 1) + wrong_fibonacci(n - 2)  # No base for n >= 0
    
    # ✅ CORRECT: Proper base cases
    def correct_countdown(n):
        """Countdown with proper base case"""
        if n <= 0:  # Base case: stop when n is 0 or negative
            print("Done!")
            return
        print(n)
        correct_countdown(n - 1)
    
    def correct_factorial(n):
        """Factorial with proper base cases"""
        if n <= 1:  # Handles both 0 and 1
            return 1
        return n * correct_factorial(n - 1)
    
    def correct_fibonacci(n):
        """Fibonacci with proper base cases"""
        if n <= 1:  # Handles both 0 and 1
            return n
        return correct_fibonacci(n - 1) + correct_fibonacci(n - 2)
    
    print("=== Base Case Errors ===")
    
    # Test wrong functions (with limits to prevent infinite recursion)
    import sys
    original_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)  # Set low limit to catch errors quickly
    
    try:
        wrong_countdown(5)
    except RecursionError as e:
        print(f"wrong_countdown error: {e}")
    
    try:
        result = wrong_factorial(1)
        print(f"wrong_factorial(1): {result}")
    except RecursionError as e:
        print(f"wrong_factorial error: {e}")
    
    try:
        result = wrong_fibonacci(5)
        print(f"wrong_fibonacci(5): {result}")
    except RecursionError as e:
        print(f"wrong_fibonacci error: {e}")
    
    # Restore original limit
    sys.setrecursionlimit(original_limit)
    
    # Test correct functions
    print("\nCorrect implementations:")
    correct_countdown(3)
    print(f"correct_factorial(5): {correct_factorial(5)}")
    print(f"correct_fibonacci(7): {correct_fibonacci(7)}")

base_case_errors()
```

### 4.2 Stack Overflow Errors

#### Deep Recursion Issues

```python
def stack_overflow_errors():
    """Demonstrate stack overflow and deep recursion issues"""
    
    import sys
    
    def check_recursion_limit():
        """Check current recursion limit"""
        return sys.getrecursionlimit()
    
    def deep_recursion_test(n):
        """Function that may cause stack overflow"""
        if n <= 0:
            return 0
        return 1 + deep_recursion_test(n - 1)
    
    # ❌ WRONG: Deep recursion without considering limits
    def wrong_sum_large_list(lst):
        """Recursive sum that may overflow for large lists"""
        if not lst:
            return 0
        return lst[0] + wrong_sum_large_list(lst[1:])
    
    # ❌ WRONG: Inefficient recursive approach
    def wrong_power(base, exp):
        """Inefficient power calculation"""
        if exp == 0:
            return 1
        return base * wrong_power(base, exp - 1)  # O(n) instead of O(log n)
    
    # ✅ CORRECT: Iterative alternative
    def correct_sum_large_list(lst):
        """Iterative sum for large lists"""
        total = 0
        for item in lst:
            total += item
        return total
    
    # ✅ CORRECT: Tail recursive with limit checking
    def correct_sum_tail_recursive(lst, accumulator=0, depth=0, max_depth=1000):
        """Tail recursive sum with depth limit"""
        if depth > max_depth:
            # Fall back to iterative approach
            return accumulator + sum(lst)
        
        if not lst:
            return accumulator
        
        return correct_sum_tail_recursive(
            lst[1:], 
            accumulator + lst[0], 
            depth + 1, 
            max_depth
        )
    
    # ✅ CORRECT: Efficient power with optimization
    def correct_power(base, exp):
        """Efficient power calculation using divide and conquer"""
        if exp == 0:
            return 1
        if exp == 1:
            return base
        
        if exp % 2 == 0:
            half_power = correct_power(base, exp // 2)
            return half_power * half_power
        else:
            return base * correct_power(base, exp - 1)
    
    def safe_recursive_call(func, *args, max_attempts=3, **kwargs):
        """Safely call recursive function with fallback"""
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs), None
            except RecursionError as e:
                if attempt == max_attempts - 1:
                    return None, f"RecursionError after {max_attempts} attempts: {e}"
                # Try reducing problem size
                if args and isinstance(args[0], (int, float)) and args[0] > 100:
                    args = (args[0] // 2,) + args[1:]
        
        return None, "Failed all attempts"
    
    print("=== Stack Overflow Errors ===")
    print(f"Current recursion limit: {check_recursion_limit()}")
    
    # Test deep recursion
    test_values = [100, 1000, 5000]
    
    for n in test_values:
        result, error = safe_recursive_call(deep_recursion_test, n)
        if error:
            print(f"deep_recursion_test({n}): {error}")
        else:
            print(f"deep_recursion_test({n}): {result}")
    
    # Test with large list
    large_list = list(range(2000))
    
    # Wrong approach (may cause stack overflow)
    result, error = safe_recursive_call(wrong_sum_large_list, large_list)
    if error:
        print(f"wrong_sum_large_list (size {len(large_list)}): {error}")
    else:
        print(f"wrong_sum_large_list: {result}")
    
    # Correct approaches
    print(f"correct_sum_large_list: {correct_sum_large_list(large_list)}")
    print(f"correct_sum_tail_recursive: {correct_sum_tail_recursive(large_list)}")
    
    # Power calculation comparison
    base, exp = 2, 1000
    print(f"\nPower calculation {base}^{exp}:")
    
    result, error = safe_recursive_call(wrong_power, base, exp)
    if error:
        print(f"wrong_power: {error}")
    else:
        print(f"wrong_power: {result}")
    
    print(f"correct_power: {correct_power(base, exp)}")

stack_overflow_errors()
```

### 4.3 Performance Issues

#### Exponential Time Complexity

```python
def performance_errors():
    """Demonstrate performance issues in recursion"""
    
    import time
    from functools import lru_cache
    
    # ❌ WRONG: Exponential time complexity
    def wrong_fibonacci(n):
        """Naive fibonacci with exponential complexity O(2^n)"""
        if n <= 1:
            return n
        return wrong_fibonacci(n - 1) + wrong_fibonacci(n - 2)
    
    def wrong_tribonacci(n):
        """Naive tribonacci with exponential complexity"""
        if n <= 1:
            return 0
        if n == 2:
            return 1
        return wrong_tribonacci(n - 1) + wrong_tribonacci(n - 2) + wrong_tribonacci(n - 3)
    
    # ❌ WRONG: Redundant recursive calls
    def wrong_coin_change(coins, amount):
        """Inefficient coin change with overlapping subproblems"""
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        
        min_coins = float('inf')
        for coin in coins:
            result = wrong_coin_change(coins, amount - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        return min_coins
    
    # ✅ CORRECT: Memoized versions
    @lru_cache(maxsize=None)
    def correct_fibonacci(n):
        """Memoized fibonacci with O(n) complexity"""
        if n <= 1:
            return n
        return correct_fibonacci(n - 1) + correct_fibonacci(n - 2)
    
    def correct_tribonacci():
        """Memoized tribonacci"""
        cache = {}
        
        def tribonacci(n):
            if n in cache:
                return cache[n]
            
            if n <= 1:
                cache[n] = 0
            elif n == 2:
                cache[n] = 1
            else:
                cache[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
            
            return cache[n]
        
        return tribonacci
    
    def correct_coin_change():
        """Memoized coin change"""
        cache = {}
        
        def coin_change(coins, amount):
            if amount in cache:
                return cache[amount]
            
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            
            min_coins = float('inf')
            for coin in coins:
                result = coin_change(coins, amount - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)
            
            cache[amount] = min_coins
            return min_coins
        
        return coin_change
    
    # ✅ CORRECT: Iterative alternatives
    def iterative_fibonacci(n):
        """Iterative fibonacci with O(n) time, O(1) space"""
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def measure_performance(func, *args, max_time=5.0):
        """Measure function performance with timeout"""
        start_time = time.time()
        
        try:
            result = func(*args)
            end_time = time.time()
            execution_time = end_time - start_time
            
            if execution_time > max_time:
                return None, f"Timeout (>{max_time}s)"
            
            return result, execution_time
        except Exception as e:
            return None, f"Error: {e}"
    
    def performance_comparison(functions, test_cases):
        """Compare performance of multiple functions"""
        results = {}
        
        for name, func in functions.items():
            results[name] = {}
            
            for case_name, args in test_cases.items():
                result, time_or_error = measure_performance(func, *args)
                results[name][case_name] = {
                    'result': result,
                    'performance': time_or_error
                }
        
        return results
    
    print("=== Performance Errors ===")
    
    # Fibonacci comparison
    fib_functions = {
        'Naive': wrong_fibonacci,
        'Memoized': correct_fibonacci,
        'Iterative': iterative_fibonacci
    }
    
    fib_test_cases = {
        'Small (n=10)': (10,),
        'Medium (n=20)': (20,),
        'Large (n=30)': (30,)
    }
    
    print("Fibonacci Performance Comparison:")
    fib_results = performance_comparison(fib_functions, fib_test_cases)
    
    for func_name, cases in fib_results.items():
        print(f"\n{func_name}:")
        for case_name, data in cases.items():
            if isinstance(data['performance'], float):
                print(f"  {case_name}: Result={data['result']}, Time={data['performance']:.6f}s")
            else:
                print(f"  {case_name}: {data['performance']}")
    
    # Coin change comparison
    coin_functions = {
        'Naive': lambda coins, amount: wrong_coin_change(coins, amount),
        'Memoized': correct_coin_change()
    }
    
    coin_test_cases = {
        'Small': ([1, 2, 5], 11),
        'Medium': ([1, 3, 4], 15)
    }
    
    print("\n\nCoin Change Performance Comparison:")
    coin_results = performance_comparison(coin_functions, coin_test_cases)
    
    for func_name, cases in coin_results.items():
        print(f"\n{func_name}:")
        for case_name, data in cases.items():
            if isinstance(data['performance'], float):
                print(f"  {case_name}: Result={data['result']}, Time={data['performance']:.6f}s")
            else:
                print(f"  {case_name}: {data['performance']}")

performance_errors()
```

### 4.4 Logic and Implementation Errors

#### Common Implementation Mistakes

```python
def logic_implementation_errors():
    """Demonstrate common logic and implementation errors"""
    
    # ❌ WRONG: Incorrect parameter modification
    def wrong_list_sum(lst):
        """Incorrectly modifies the original list"""
        if not lst:
            return 0
        
        first = lst.pop(0)  # Modifies original list!
        return first + wrong_list_sum(lst)
    
    # ❌ WRONG: Incorrect string slicing
    def wrong_palindrome_check(s):
        """Inefficient string slicing creates many substrings"""
        s = s.lower().replace(" ", "")
        
        if len(s) <= 1:
            return True
        
        if s[0] != s[-1]:
            return False
        
        return wrong_palindrome_check(s[1:-1])  # Creates new string each time
    
    # ❌ WRONG: Missing edge case handling
    def wrong_binary_search(arr, target, left=0, right=None):
        """Binary search with missing edge case handling"""
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return wrong_binary_search(arr, target, mid + 1, right)
        else:
            return wrong_binary_search(arr, target, left, mid - 1)
        # Missing: What if arr is empty? What if target is None?
    
    # ❌ WRONG: Incorrect tree traversal
    def wrong_tree_height(root):
        """Incorrect tree height calculation"""
        if not root:
            return 0
        
        # Wrong: doesn't add 1 for current node
        return max(wrong_tree_height(root.left), wrong_tree_height(root.right))
    
    # ✅ CORRECT: Proper implementations
    def correct_list_sum(lst):
        """Sum without modifying original list"""
        if not lst:
            return 0
        return lst[0] + correct_list_sum(lst[1:])  # Use slicing instead of pop
    
    def correct_palindrome_check(s, left=0, right=None):
        """Efficient palindrome check using indices"""
        if right is None:
            s = s.lower().replace(" ", "")
            right = len(s) - 1
        
        if left >= right:
            return True
        
        if s[left] != s[right]:
            return False
        
        return correct_palindrome_check(s, left + 1, right - 1)
    
    def correct_binary_search(arr, target, left=0, right=None):
        """Binary search with proper edge case handling"""
        # Handle edge cases
        if not arr or target is None:
            return -1
        
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return correct_binary_search(arr, target, mid + 1, right)
        else:
            return correct_binary_search(arr, target, left, mid - 1)
    
    def correct_tree_height(root):
        """Correct tree height calculation"""
        if not root:
            return 0
        
        left_height = correct_tree_height(root.left)
        right_height = correct_tree_height(root.right)
        
        return 1 + max(left_height, right_height)  # Add 1 for current node
    
    # Validation and testing functions
    def validate_function_behavior(wrong_func, correct_func, test_cases, func_name):
        """Compare behavior of wrong vs correct implementations"""
        print(f"\n=== {func_name} Validation ===")
        
        for i, test_case in enumerate(test_cases):
            try:
                # Test wrong implementation
                if isinstance(test_case, tuple):
                    wrong_result = wrong_func(*test_case)
                else:
                    wrong_result = wrong_func(test_case)
                
                wrong_error = None
            except Exception as e:
                wrong_result = None
                wrong_error = str(e)
            
            try:
                # Test correct implementation
                if isinstance(test_case, tuple):
                    correct_result = correct_func(*test_case)
                else:
                    correct_result = correct_func(test_case)
                
                correct_error = None
            except Exception as e:
                correct_result = None
                correct_error = str(e)
            
            print(f"Test case {i + 1}: {test_case}")
            if wrong_error:
                print(f"  Wrong: Error - {wrong_error}")
            else:
                print(f"  Wrong: {wrong_result}")
            
            if correct_error:
                print(f"  Correct: Error - {correct_error}")
            else:
                print(f"  Correct: {correct_result}")
    
    # Simple tree node for testing
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    print("=== Logic and Implementation Errors ===")
    
    # Test list sum
    test_lists = [
        [1, 2, 3, 4, 5],
        [],
        [10]
    ]
    
    for test_list in test_lists:
        original = test_list.copy()
        wrong_result = wrong_list_sum(test_list)
        print(f"List sum test:")
        print(f"  Original: {original}")
        print(f"  After wrong_list_sum: {test_list} (modified!)")
        print(f"  Wrong result: {wrong_result}")
        
        correct_result = correct_list_sum(original)
        print(f"  Correct result: {correct_result}")
        print()
    
    # Test palindrome check
    palindrome_tests = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car",
        ""
    ]
    
    validate_function_behavior(
        wrong_palindrome_check,
        correct_palindrome_check,
        palindrome_tests,
        "Palindrome Check"
    )
    
    # Test binary search
    search_tests = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 6),
        ([], 1),
        ([1], 1)
    ]
    
    validate_function_behavior(
        lambda arr, target: wrong_binary_search(arr, target),
        lambda arr, target: correct_binary_search(arr, target),
        search_tests,
        "Binary Search"
    )
    
    # Test tree height
    # Create test tree:  1
    #                   / \
    #                  2   3
    #                 /
    #                4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    
    print(f"\nTree Height Test:")
    print(f"  Wrong implementation: {wrong_tree_height(root)}")
    print(f"  Correct implementation: {correct_tree_height(root)}")
    print(f"  Expected: 3 (root -> left -> left)")

logic_implementation_errors()
```

### 4.5 Best Practices for Error Prevention

```python
def recursion_best_practices():
    """Best practices for preventing recursion errors"""
    
    print("""
=== Recursion Error Prevention Best Practices ===

1. BASE CASE DESIGN:
   ✓ Always define clear base cases
   ✓ Ensure base cases handle all edge conditions
   ✓ Test base cases with boundary values (0, 1, empty collections)
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

6. CODE STRUCTURE:
   ✓ Keep recursive functions simple and focused
   ✓ Separate concerns (validation, computation, formatting)
   ✓ Use helper functions for complex recursive logic
   ✓ Document the recursive invariant and termination condition

7. TESTING:
   ✓ Test with small inputs first
   ✓ Test all base cases
   ✓ Test edge cases (empty inputs, single elements)
   ✓ Performance test with large inputs
   ✓ Test for stack overflow conditions
    """)
    
    # Example of a well-designed recursive function following best practices
    def robust_factorial(n, _depth=0, _max_depth=1000):
        """
        Calculate factorial with comprehensive error handling and best practices.
        
        Args:
            n: Non-negative integer
            _depth: Internal parameter for depth tracking
            _max_depth: Maximum recursion depth allowed
        
        Returns:
            int: Factorial of n
            
        Raises:
            TypeError: If n is not an integer
            ValueError: If n is negative
            RecursionError: If recursion depth exceeds limit
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
        
        Args:
            n: Non-negative integer
            _cache: Internal memoization cache
            _depth: Internal depth tracking
            _max_depth: Maximum recursion depth
        
        Returns:
            int: nth Fibonacci number
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
        import functools
        import sys
        
        @functools.wraps(func)
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
    
    # Test robust implementations
    print("\nTesting Robust Implementations:")
    
    # Test robust factorial
    test_values = [0, 1, 5, 10, 100]
    for val in test_values:
        try:
            result = robust_factorial(val)
            print(f"robust_factorial({val}) = {result}")
        except Exception as e:
            print(f"robust_factorial({val}) error: {e}")
    
    # Test with invalid inputs
    try:
        robust_factorial(-5)
    except ValueError as e:
        print(f"robust_factorial(-5) correctly raised: {e}")
    
    try:
        robust_factorial("not a number")
    except TypeError as e:
        print(f"robust_factorial('not a number') correctly raised: {e}")
    
    # Test robust fibonacci
    print(f"\nrobust_fibonacci(20) = {robust_fibonacci(20)}")
    print(f"robust_fibonacci(100) = {robust_fibonacci(100)}")

recursion_best_practices()
```

---

## Summary

This comprehensive documentation covers:

1. **Recursion Definition and Characteristics**: Basic structure, types of recursion (linear, tree, tail), and recursion characteristics including stack behavior and memory usage

2. **Recursion Operations**: Mathematical operations, sequence operations, data structure operations (lists, strings), and tree/graph operations

3. **Recursion Methods**: Optimization techniques (memoization, dynamic programming), tail recursion optimization, and recursion analysis methods

4. **Common Errors**: Base case errors, stack overflow issues, performance problems, logic/implementation mistakes, and comprehensive best practices for error prevention

The documentation provides practical, runnable examples for each concept, demonstrating both incorrect and correct approaches to help developers understand recursion thoroughly and avoid common pitfalls while writing efficient, maintainable recursive code.
