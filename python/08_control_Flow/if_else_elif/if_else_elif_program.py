#!/usr/bin/env python3
"""
Python Conditional Statements Program
Demonstrates if, if..else, and if..elif statements with practical examples
"""

def main():
    print("=== Python Conditional Statements Demo ===\n")
    
    # Example 1: Simple if statement
    print("1. Simple if Statement Example:")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("✅ You are eligible to vote!")
    print()
    
    # Example 2: if..else statement
    print("2. if..else Statement Example:")
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"✅ {number} is even")
    else:
        print(f"✅ {number} is odd")
    print()
    
    # Example 3: if..elif..else statement (Grade Calculator)
    print("3. if..elif..else Statement Example (Grade Calculator):")
    try:
        score = float(input("Enter your test score (0-100): "))
        
        if score < 0 or score > 100:
            print("❌ Invalid score! Please enter a score between 0-100.")
        elif score >= 90:
            print(f"🏆 Excellent! Grade: A ({score}%)")
        elif score >= 80:
            print(f"👍 Great job! Grade: B ({score}%)")
        elif score >= 70:
            print(f"👌 Good work! Grade: C ({score}%)")
        elif score >= 60:
            print(f"📚 Keep studying! Grade: D ({score}%)")
        else:
            print(f"💪 Don't give up! Grade: F ({score}%)")
    except ValueError:
        print("❌ Invalid input! Please enter a numeric score.")
    print()
    
    # Example 4: Complex conditions with logical operators
    print("4. Complex Conditions Example (Login System):")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "secret123":
        print("🔓 Access granted! Welcome, Administrator!")
    elif username == "user" and password == "password":
        print("🔓 Access granted! Welcome, User!")
    elif username in ["admin", "user"] and password == "":
        print("🔒 Access denied! Password cannot be empty.")
    elif username == "" or password == "":
        print("🔒 Access denied! Username and password are required.")
    else:
        print("🔒 Access denied! Invalid credentials.")
    print()
    
    # Example 5: Nested if statements
    print("5. Nested if Statement Example (Weather Advisory):")
    try:
        temperature = float(input("Enter temperature in Celsius: "))
        is_raining = input("Is it raining? (yes/no): ").lower().strip()
        
        if temperature > 30:
            print("🌡️ It's hot outside!")
            if is_raining == "yes":
                print("🌧️ Hot and rainy - take an umbrella and stay hydrated!")
            else:
                print("☀️ Hot and dry - don't forget sunscreen and water!")
        elif temperature > 20:
            print("🌡️ Pleasant temperature!")
            if is_raining == "yes":
                print("🌧️ Nice and rainy - perfect for indoor activities!")
            else:
                print("☀️ Perfect weather for outdoor activities!")
        elif temperature > 0:
            print("🌡️ It's cold outside!")
            if is_raining == "yes":
                print("🌧️ Cold and rainy - dress warmly and take an umbrella!")
            else:
                print("❄️ Cold but dry - dress warmly!")
        else:
            print("🥶 It's freezing!")
            if is_raining == "yes":
                print("🌨️ Freezing rain - be very careful, roads may be icy!")
            else:
                print("❄️ Freezing cold - bundle up and stay warm!")
    except ValueError:
        print("❌ Invalid temperature! Please enter a numeric value.")
    print()
    
    # Example 6: Menu system using if..elif
    print("6. Menu System Example:")
    print("Choose an option:")
    print("1. Calculate area of rectangle")
    print("2. Calculate area of circle")
    print("3. Calculate area of triangle")
    print("4. Exit")
    
    try:
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"📐 Area of rectangle: {area} square units")
        elif choice == "2":
            import math
            radius = float(input("Enter radius: "))
            area = math.pi * radius ** 2
            print(f"⭕ Area of circle: {area:.2f} square units")
        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"🔺 Area of triangle: {area} square units")
        elif choice == "4":
            print("👋 Goodbye! Thanks for using the program!")
        else:
            print("❌ Invalid choice! Please select 1-4.")
    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")
    
    print("\n=== Program completed successfully! ===")

if __name__ == "__main__":
    main()