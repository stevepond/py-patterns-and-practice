"""Problem 08: BFS graph traversal"""

from collections import deque

def bfs(graph, start):
    """Return BFS order starting from node."""
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neigh in graph.get(node, []):
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)
    return order
