"""Example 11: context manager"""

from contextlib import contextmanager

@contextmanager
def open_file(path, mode="r"):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
