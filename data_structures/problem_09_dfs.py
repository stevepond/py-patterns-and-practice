"""Problem 09: DFS graph traversal"""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neigh in graph.get(start, []):
        if neigh not in visited:
            order += dfs(graph, neigh, visited)
    return order
