"""Example 05: decorator"""

from functools import wraps


def simple_decorator(func):
    """Example decorator that adds 1 to the return value."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 1
    return wrapper


@simple_decorator
def add_one(x):
    return x
