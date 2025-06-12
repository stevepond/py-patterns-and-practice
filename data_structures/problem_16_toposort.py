"""Problem 16: Topological sort"""

from collections import deque, defaultdict

def topological_sort(edges):
    graph = defaultdict(list)
    indeg = defaultdict(int)
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1
        indeg.setdefault(u, 0)
    queue = deque([n for n in indeg if indeg[n] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neigh in graph[node]:
            indeg[neigh] -= 1
            if indeg[neigh] == 0:
                queue.append(neigh)
    return order
