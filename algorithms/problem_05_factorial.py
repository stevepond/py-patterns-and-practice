"""Problem 05: Factorial using recursion"""

def factorial(n):
    """Return factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
