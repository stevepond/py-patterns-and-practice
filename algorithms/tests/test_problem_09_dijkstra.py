from algorithms.problem_09_dijkstra import dijkstra


def test_dijkstra():
    graph = {1:[(2,1),(3,4)],2:[(3,1)],3:[]}
    dist = dijkstra(graph,1)
    assert dist[3] == 2

