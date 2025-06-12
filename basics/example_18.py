"""Example 18: recursion"""

def factorial(n):
    """Return factorial of n recursively."""
    return 1 if n <= 1 else n * factorial(n - 1)
