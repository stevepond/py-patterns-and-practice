from data_structures.problem_15_union_find import UnionFind


def test_union_find():
    uf = UnionFind(3)
    uf.union(0, 1)
    assert uf.find(0) == uf.find(1)
    assert uf.find(2) != uf.find(0)
