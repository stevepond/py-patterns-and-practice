"""Example 10: generator"""

def count_up_to(n):
    """Yield numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1
