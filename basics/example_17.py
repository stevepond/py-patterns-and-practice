"""Example 17: filter"""

def even_numbers(nums):
    """Return list of even numbers using filter."""
    return list(filter(lambda x: x % 2 == 0, nums))
