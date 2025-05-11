# recursion.py

# Part I – Fibonacci Sequence
def fibonacci(n):
    if n < 0:
        raise ValueError("Input should be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Part II – Euclid’s GCD Algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Part III – Recursive String Comparison
def compareTo(s1, s2):
    if s1 == "" and s2 == "":
        return 0
    if s1 == "":
        return -ord(s2[0])
    if s2 == "":
        return ord(s1[0])
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])
