"""Problem 02: Queue using deque"""

from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.popleft()

    def is_empty(self):
        return not self._data
