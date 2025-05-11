# test_recursion.py

from recursion import fibonacci, gcd, compareTo

# Test Fibonacci
print("Fibonacci Tests:")
print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(5))  # Output: 5
print(fibonacci(10)) # Output: 55

# Test GCD
print("\nGCD Tests:")
print(gcd(48, 18))   # Output: 6
print(gcd(101, 103)) # Output: 1
print(gcd(54, 24))   # Output: 6

# Test compareTo
print("\ncompareTo Tests:")
print(compareTo("apple", "apple"))   # Output: 0
print(compareTo("apple", "apples"))  # Output: negative
print(compareTo("banana", "apple"))  # Output: positive
print(compareTo("", ""))             # Output: 0
