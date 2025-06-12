from data_structures.problem_09_dfs import dfs


def test_dfs():
    graph = {1: [2, 3], 2: [4], 3: [], 4: []}
    assert dfs(graph, 1) == [1, 2, 4, 3]
