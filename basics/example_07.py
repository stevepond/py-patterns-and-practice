"""Example 07: dict comprehension"""

def invert_dict(d):
    """Invert keys and values using dict comprehension."""
    return {v: k for k, v in d.items()}
