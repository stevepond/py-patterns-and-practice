"""Problem 01: Simple stack"""

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def is_empty(self):
        return not self._data
