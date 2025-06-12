"""Example 12: environment variables"""

import os

def get_env(var, default=None):
    """Return environment variable value or default."""
    return os.getenv(var, default)
