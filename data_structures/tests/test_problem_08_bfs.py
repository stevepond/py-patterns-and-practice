from data_structures.problem_08_bfs import bfs


def test_bfs():
    graph = {1: [2, 3], 2: [4], 3: [], 4: []}
    assert bfs(graph, 1) == [1, 2, 3, 4]
