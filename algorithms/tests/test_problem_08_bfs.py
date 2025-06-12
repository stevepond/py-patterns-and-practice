from algorithms.problem_08_bfs import bfs


def test_bfs_algorithm():
    graph = {1:[2,3],2:[],3:[]}
    assert bfs(graph,1) == [1,2,3]

