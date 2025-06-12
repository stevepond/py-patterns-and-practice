from data_structures.problem_16_toposort import topological_sort


def test_topological_sort():
    edges = [(1, 2), (1, 3), (3, 4)]
    order = topological_sort(edges)
    assert order.index(1) < order.index(2)
    assert order.index(1) < order.index(3)
    assert order.index(3) < order.index(4)
