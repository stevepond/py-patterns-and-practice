"""Problem 11: Heap sort"""

import heapq

def heap_sort(iterable):
    """Return list sorted using heapq."""
    h = list(iterable)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
