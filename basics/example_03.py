"""Example 03: **kwargs"""

def format_kwargs(**kwargs):
    """Return a formatted string of keyword arguments."""
    return ", ".join(f"{k}={v}" for k, v in kwargs.items())
