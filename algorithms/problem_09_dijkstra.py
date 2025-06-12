"""Problem 09: Dijkstra's algorithm"""

import heapq

def dijkstra(graph, start):
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist.get(node, float('inf')):
            continue
        for neigh, weight in graph.get(node, []):
            new_cost = cost + weight
            if new_cost < dist.get(neigh, float('inf')):
                dist[neigh] = new_cost
                heapq.heappush(pq, (new_cost, neigh))
    return dist
